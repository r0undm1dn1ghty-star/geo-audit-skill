# -*- coding: utf-8 -*-
"""Реализация GEO Audit (readiness-proxy!) для skillkit.
Вход: {"html": "...", "url": "..."} или {"signals": {...}}. Выход: score 0-100 + находки.
ВАЖНО: score — прокси готовности, НЕ вероятность цитирования (v1.6+)."""
import html as _h
import re

SKILL_NAME = "geo-audit"
SKILL_VERSION = "1.7.0"
SKILL_DESCRIPTION = ("Прокси-аудит готовности сайта к AI-поиску (GEO/AEO): структура, "
                     "разметка Schema.org, доступность для AI-краулеров. Score — не вероятность цитирования.")
INPUT_SCHEMA = {"type": "object", "properties": {
    "input": {"type": "object", "properties": {"html": {"type": "string"}, "url": {"type": "string"}}}},
    "required": ["input"]}
OUTPUT_SCHEMA = {"type": "object", "properties": {
    "score": {"type": "integer", "minimum": 0, "maximum": 100},
    "grade": {"type": "string"}, "checks": {"type": "object"},
    "not_observed": {"type": "array", "items": {"type": "string"}},
    "boundary": {"type": "string"}}}
SYSTEM_PROMPT = """Ты — аудитор GEO/AEO. Оцени готовность страницы к цитированию в AI-поиске.
ЖЁСТКОЕ ПРАВИЛО: score — прокси готовности, НЕ вероятность цитирования. Никогда не утверждай,
что сайт «будет цитироваться». Если JS-контент недоступен без исполнения — пиши «не наблюдаю», не выдумывай.
Формат: score 0-100 + что подтверждено / чего нет / границы."""

RULES = [
    ("title", 8, lambda h: bool(re.search(r"<title[^>]*>[^<]{10,}", h, re.I)), "заголовок документа"),
    ("h1", 8, lambda h: bool(re.search(r"<h1[^>]*>\s*[^<]{8,}", h, re.I)), "один явный H1"),
    ("headings", 10, lambda h: len(re.findall(r"<h[23][^>]*>", h, re.I)) >= 3, "3+ подзаголовка H2/H3"),
    ("schema_org", 18, lambda h: "application/ld+json" in h and "schema.org" in h, "Schema.org JSON-LD"),
    ("faq", 10, lambda h: bool(re.search(r"FAQPage|вопросы и ответы|частые вопросы", h, re.I)), "FAQ-блок"),
    # ссылка на llms.txt, а не просто упоминание слова (иначе статья О llms.txt засчитывается)
    ("llms_txt", 8, lambda h: bool(re.search(r'href=["\'][^"\']*llms\.txt["\']', h, re.I)), "ссылка на llms.txt"),
    ("semantic", 8, lambda h: bool(re.search(r"<(article|main|section|nav)\b", h, re.I)), "семантические теги"),
    ("meta_desc", 8, lambda h: bool(re.search(r'name=["\']description["\'][^>]*content=["\'][^"\']{40,}', h, re.I)), "meta description 40+"),
    ("readable_blocks", 8, lambda h: len(re.findall(r"<p[^>]*>", h, re.I)) >= 5, "5+ абзацев текста"),
    ("no_js_shell", 14, lambda h: len(re.sub(r"<[^>]+>", "", h)) > 1500, "текст в HTML (не пустой JS-shell)"),
]


def run(input_value=None, **kw):
    if isinstance(input_value, dict):
        raw = input_value.get("html") or input_value.get("text") or ""
        url = input_value.get("url", "")
        if not raw and input_value.get("signals"):
            sig = input_value["signals"]
            hits = {k: bool(v) for k, v in sig.items()}
            score = sum(w for n, w, _f, _d in RULES if hits.get(n))
            return {"score": score, "grade": grade(score), "checks": hits,
                    "not_observed": [n for n, _w, _f, _d in RULES if not hits.get(n)],
                    "boundary": "Оценка по переданным сигналам. Score — прокси, не вероятность цитирования.", "url": url}
    else:
        raw = str(input_value or "")
    checks, not_observed = {}, []
    for name, _w, fn, _desc in RULES:
        try:
            ok = bool(fn(raw)) if raw else False
        except Exception:
            ok = False
        checks[name] = ok
        if not ok:
            not_observed.append(name)
    score = sum(w for n, w, _f, _d in RULES if checks[n])
    return {"score": score, "grade": grade(score), "checks": checks,
            "not_observed": not_observed, "url": (input_value or {}).get("url", "") if isinstance(input_value, dict) else "",
            "boundary": ("Score — прокси готовности, НЕ вероятность цитирования. "
                         "Если контент собирался JS — правило no_js_shell даёт «не наблюдаю».")}


def grade(score):
    """Буква готовности. Верхняя полоса достижима только со Schema.org + llms.txt + текстом."""
    return "A" if score >= 80 else "B" if score >= 60 else "C" if score >= 40 else "D" if score >= 20 else "E"
