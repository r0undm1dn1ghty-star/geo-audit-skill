---
name: geo-audit
description: "GEO SEO аудит для AI-поиска. Use when geo, seo, URL."
version: "1.7.0"
author: "Victor Zaitsev"
---

# GEO-SEO Audit Skill — by Victor Zaitsev

> **Это мой собственный скилл.** Собран и доработан мной (взят за основу сильный open-base, но структура, скоринг, методология, шаблоны и пайплайн — моя работа и мой метод). Любое использование реплицируемого пайплайна в коммерческом контексте — со ссылкой на автора. Здесь всё, что я знаю про GEO — и ничего лишнего.

> **Философия (2026):** AEO+GEO = это современное SEO. AI-поиск не «съел» SEO — он сменил оптимизационную ось: с ключевиков и топ-10 на **сущности и готовые ответы**. Оптимизируй источник так, чтобы AI захотел процитировать именно его.
>
> **Маркер моего подхода:** аудит строится вокруг **ответа и сущности**, а не ранжирования. Фокус — на (1) entity-карте (кто говорит, чем это подтверждено), (2) answer-first блоках, которые AI цитирует целиком, (3) доступе краулеров к исходному HTML. Традиционный топ-10 — побочный эффект, не цель.

---

## Изменения 1.2.0 (2026-09-07)

- Исправлено: утверждение «llms.txt — must-have» из 1.1.0 заменено на честную оценку (см. ядро ниже) — данные 2026 не подтверждают прямой эффект на видимость.
- Добавлено: полное ядро **AEO+GEO 2026** (актуальные факторы, а не приёмы 2023).
- Ядро скоринга переведено с «статистика+цитаты» на «entity graph + E-E-A-T + answer-first + schema/датирование».

---

## AEO+GEO CORE 2026 — актуальное ядро (что реально работает)

> Собрано 07.09.2026 из свежих источников (Google AI Search guide 05.2026, state-of-AI-search 2026, AEO-гайды 03–08.2026). Разделено на: **работает / спорное / отвалилось**. Принимай как рабочую карту, не как догму — рынок меняется ежемесячно.

### ✅ Работает (доказано предметно, не опровергнуто)

| Фактор | Что делать | Почему |
|---|---|---|
| **Entity clarity / знания-граф** | Organization + Person schema, sameAs→LinkedIn/Wikipedia, связки entity, консистентный NAP и наименование бренда | Главный фактор 2026: AI цитирует *сущности*, а не ключевики. Без entity-карты — нет доверия AI. |
| **Person/Organization graph** | author bio, credentials, jobTitle, knowsAbout, linked author pages | E-E-A-T завязан на распознание «кто говорит». |
| **Answer-first структура** | вопрос-заголовок (H2/H3), ответ в первых 40–60 словах, самодостаточный блок | Правило 40 слов: AI берёт блок целиком как ответ. |
| **Schema + датирование** | JSON-LD в исходном HTML, datePublished/dateModified видимые | Схема и свежесть — самая воспроизводимая часть возврата (AEO+GEO-пересечение). |
| **SSR / контент в HTML** | без client-side-only рендера; JSON-LD не через JS | Google рендерит JS, но не все AI-краулеры рендерят или ждут рендер — проверяй спецификации конкретных ботов (ClaudeBot/OpenAI/Perplexity документируют поведение). SSR-контент = самый надёжный путь для всех ботов. |
| **Цитаты + конкретные цифры** | прямые цитаты экспертов, %/числа, named sources | базовый слой цитируемости (Princeton GEO 2023) — по-прежнему работает как *сигнал*, но это гигиена, не дифференциатор. |
| **Краулер-доступ** | robots.txt открывает GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Googlebot; sitemap в robots | без доступа нет индексации и цитирования вообще. |

### ⚠️ Спорное (не доказано, не отвалилось — держать нейтрально)

| Фактор | Статус 2026 |
|---|---|
| **llms.txt** | До 2025 — «must-have»; к 04.2026 geoclarity: «no strong evidence it improves AI citations». Google 05.2026 (AI Search guide) поместил его в «пять тактик, которые больше не помогают [для ранжирования]». **Вывод: делай как courtesy/структурирование для агентов, НЕ ставь на него как на фактор видимости.** Не снижай балл за отсутствие жёстко. |
| **FAQ schema** | Google ограничил rich results (только health/gov). Для AEO у части площадок ещё работает (prompt-matched questions), но это не «золотой билет». |
| **Content chunking / machine-friendly rewrites** | Google 05.2026: «no longer help». Не гоняться за «нарезкой под AI». |

### ❌ Отвалилось (не тратить на это)

| Фактор | Почему отпало |
|---|---|
| **GEO ≠ SEO как разные дисциплины** | Google 05.2026 официально: AI search = всё ещё SEO; «GEO/AEO no longer separate disciplines». Моя старая формула «GEO-first, SEO-supported» — устарела. Новый фрейм: **AEO+GEO = SEO, дополненное entity- и answer-слоем.** |
| **Keyword stuffing** | вредил всегда, в AI-выдаче вредит сильнее — деструктивный сигнал. |
| **Schema как «AI-хак»** | Google прямо: schema не хак. Это семантика, не трюк. |
| **Inauthentic mentions / накрутка бренд-упоминаний** | работает против (Google 05.2026). |

### 🎯 Новый приоритет (что вывести в топ скоринга)

1. **Entity clarity + Person/Organization graph** (главный дифференциатор 2026)
2. **E-E-A-T** (experience, expertise, authority, trust)
3. **Answer-first контент** (40-словное правило, вопрос→ответ)
4. **Schema + датирование** (+ sameAs)
5. **Crawler access + SSR** (гигиена)
6. Цитаты/статистика → базовый слой, не «секрет».

**Коммерческий вывод для Discovery/консалтинга**: аудит, который сдаёт это ядро (entity-map, answer-architecture, schema+dates, E-E-A-T) — это аудит 2026, а не «GEO-гороскоп 2023». «Взрыв» = то, что ловит свежий сдвиг Google/Search по доминанте entity+answer, а не пересчитывает вчерашние citation-приёмы.

---

## Linter Rules — 92 проверки (адаптировано из open-source GEO-линтеров, MIT)

> База правил собрана из открытых MIT-решений (geo-lint, elmo, Citatra) и пересобрана под мой скоринг. Не копия — компиляция лучшего, что работает в 2026.

### Категория A: GEO-Specific (entity, citation, answer-first) — 28 правил

| # | Правило | Проверка | Балл |
|---|---|---|---|
| G01 | **Answer-first lead** | Прямой ответ в первых 30% документа (40–60 слов); внутри абзаца ответ не обязан быть первым предложением — 53% цитат берутся из середины абзацев | 10 |
| G02 | **Question heading** | Хотя бы один H2/H3 сформулирован как вопрос | 8 |
| G03 | **Entity density** | На 500 слов ≥3 named entities (бренды, люди, продукты, концепции) | 10 |
| G04 | **Entity schema match** | Entity в тексте имеют matching JSON-LD (Organization, Person, Product) | 8 |
| G05 | **Citation pattern: quote** | Хотя бы одна прямая цитата с атрибуцией (имя + источник) | 8 |
| G06 | **Citation pattern: statistic** | Хотя бы одна конкретная цифра/процент с контекстом | 8 |
| G07 | **Source attribution** | Внешние ссылки на авторитетные источники (не self-link) | 6 |
| G08 | **Comparison table** | Если контент сравнительный — есть `<table>` (AI любит таблицы) | 6 |
| G09 | **Definition pattern** | Хотя бы один блок «X — это…» (AI берёт как определение) | 6 |
| G10 | **Self-contained block** | Ответный блок не требует контекста с другой страницы | 10 |
| G11 | **Author attribution** | У контента есть named author + linked bio + Person schema | 8 |
| G12 | **Date visible** | datePublished/dateModified видны на странице + в schema | 6 |
| G13 | **speakable schema** | speakable указывает на ключевые секции ответа | 5 |
| G14 | **sameAs links** | Organization/Person schema содержит sameAs ≥3 (LinkedIn, Wikipedia, GitHub) | 8 |
| G15 | **NAP consistency** | Name-Address-Phone одинаковые на сайте, в schema, в Google Business | 6 |
| G16 | **Brand mention consistency** | Бренд назван одинаково во всех блоках (не сокращения/варианты) | 5 |
| G17 | **Semantic hierarchy** | H1→H2→H3 без пропусков уровня | 5 |
| G18 | **Paragraph length** | Абзацы ≤150 слов (AI не берёт длинные блоки) | 4 |
| G19 | **List/numbered items** | Если перечисление — есть `<ul>`/`<ol>` (AI любит списки) | 4 |
| G20 | **Keyword stuffing penalty** | Плотность ключевика >3% → штраф -10 | -10 |
| G21 | **No keyword stuffing** | Повторение фразы >5 раз на 500 слов → штраф | -8 |
| G22 | **AI-content red flag** | Generic phrasing («in today's digital landscape») → штраф | -5 |
| G23 | **No inauthentic mentions** | Накрученные бренд-упоминания → штраф | -10 |
| G24 | **Content chunking not forced** | Нет искусственной нарезки под «machine-friendly» | 3 |
| G25 | **Fluency** | Текст плавный, без фрагментации ради «AI-readability» | 3 |
| G26 | **Technical terminology** | Спец-термины присутствуют (не упрощён до «для всех») | 5 |
| G27 | **Authoritative voice** | Тон экспертный, от первого лица / от организации | 4 |
| G28 | **Unique content** | Нет дублирования чужих блоков (оригинальность) | 5 |

### Категория B: SEO Foundation (32 правила)

| # | Правило | Проверка |
|---|---|---|
| S01–S10 | **Meta tags** | title 50-60, description 150-160, canonical, robots, viewport, lang, OG, Twitter Card |
| S11–S20 | **Headings & structure** | H1 один, H2-H6 иерархия, нет пропусков, нет пустых headings |
| S21–S25 | **URL & canonical** | URL clean, no params, canonical self-referencing, trailing slash consistent |
| S26–S32 | **Crawlability** | robots.txt валиден, sitemap.xml есть и referenced, no broken internal links, 200 on key pages |

### Категория C: Content Quality (16 правил)

| # | Правило | Проверка |
|---|---|---|
| C01 | **Word count** | ≥300 слов для статей, ≥150 для product pages |
| C02 | **Readability** | Flesch ≥30 (не академический барьер) |
| C03 | **Paragraph breaks** | Нет стен текста (≥4 абзацев на 1000 слов) |
| C04 | **Image alt text** | Все `<img>` имеют alt |
| C05 | **Internal linking** | ≥3 внутренних ссылок на related content |
| C06–C10 | **AI-content detection** | Нет generic patterns, hedging overload, repetitive thesis |
| C11–C16 | **Topical authority** | Content breadth, hub-cluster links, не orphan pages |

### Категория D: i18n (16 правил)

| # | Правило | Проверка |
|---|---|---|
| I01 | **html lang** | Указан и корректен |
| I02–I06 | **hreflang** | Для мультиязычных: hreflang теги валидны, reciprocal |
| I07–I10 | **URL locale** | /ru/, /en/ структура или subdomain |
| I11–I16 | **Content locale match** | Язык контента совпадает с lang атрибутом |

---

## Toolchain — открытые инструменты (MIT, интегрируемые в пайплайн)

> Не мои инструменты — это open-source решения, которые я использую в аудите как вспомогательные. Все MIT-лицензированные, свободны для коммерческого использования.

### geo-lint (`@ijonis/geo-lint`)
- **Что:** CLI-линтер, 92 правила GEO+SEO+content quality
- **Лицензия:** MIT
- **Использование:** `npx @ijonis/geo-lint <url>` — быстрый скоринг; можно как pre-check перед полным аудитом
- **Что даёт:** entity density, citation patterns, answer-first lead detection, comparison table detection — автоматизировано, не на глаз
- **Интеграция:** запускать перед Phase 2 (Parallel Analysis) как baseline-scan

### elmo (`@elmohq/cli`)
- **Что:** AI visibility tracker — мониторинг как ChatGPT, Claude, Perplexity, Gemini, Copilot, Grok, Google AI Overviews цитируют бренд
- **Лицензия:** MIT
- **Использование:** `npm install -g @elmohq/cli` → `elmo init` → `elmo track <brand>`
- **Что даёт:** longitudinal data — какие платформы цитируют, какие нет, динамика
- **Интеграция:** для клиентского отчёта «мониторинг после внедрения» (retainer, не one-shot)

### Citatra
- **Что:** Open-source AI visibility platform — мониторинг бренда в Google AI Overviews, трекинг конкурентов
- **Что даёт:** конкурентный анализ в AI-выдаче (кто цитируется вместо тебя)
- **Интеграция:** для конкурентной разведки в отчёте

### llms-txt-toolkit (`abovefear/llms-txt-toolkit`)
- **Что:** Spec-compliant llms.txt validator + sitemap-based generator
- **Лицензия:** MIT
- **Использование:** для генерации/валидации llms.txt (если клиент хочет — делаем, но не продаем как фактор ранжирования)

---

## Execution Flow v2 (с linter и tracker)

```
1. Quick scan:    geo-lint <url> → baseline 92-rule score
2. Phase 1:      Discovery (fetch HTML, detect type, extract pages)
3. Phase 2:      5 parallel agents (ai-visibility, platform, technical, content, schema)
4. Phase 3:      Synthesis (composite score + action plan)
5. Post-audit:   elmo init → longitudinal tracking (retainer)
6. Report:        client-ready markdown + prioritized fixes
```

---

## Trigger / When to Use

Запускай когда:
- User даёт URL для анализа / аудита / оптимизации
- User говорит "geo", "seo", "AI visibility", "citability", "llms.txt", "schema", "GEO report"
- User хочет проверить лендинг / продукт / страницу перед публикацией
- User хочет повысить выдачу в поисковиках
- User — Victor Zaitsev и говорит: «гео-аудит», «мой geo-скилл», «прогони по GEO»

**Не использовать:** технический SEO-аудит без задачи AI-видимости (это классический SEO, а не GEO); аудит закрытого/приватного сайта без публичного доступа; работа с ключевыми словами и топ-10 как самоцель — GEO оптимизирует под цитируемость и сущности, не под ранжирование.

---

## Quick Reference

| Команда | Что делает |
|---------|-----------|
| `audit <url>` | Полный GEO + SEO аудит (все 6 категорий) |
| `quick <url>` | 60-секундный снапшот видимости |
| `citability <url>` | Скоринг контента на AI-цитируемость |
| `crawlers <url>` | Проверка доступа AI-краулеров (robots.txt) |
| `llmstxt <url>` | Анализ / генерация llms.txt |
| `schema <url>` | Детект / валидация / генерация JSON-LD |
| `report <url>` | Клиент-готовый отчёт с action plan |

---

## Orchestration: Full Audit

### Phase 1: Discovery (Sequential)

1. Fetch homepage HTML через `web_extract` или `terminal curl -sL <url>`
2. Detect business type (SaaS, Local, E-commerce, Publisher, Agency, Other)
3. Extract key pages from sitemap.xml or internal links (up to 50)

**Business Type Detection:**

| Type | Signals |
|------|---------|
| SaaS | Pricing page, "Sign up", "Free trial", "/app", "/dashboard", API docs |
| Local Service | Phone, address, "Near me", Maps embed, service area |
| E-commerce | Product pages, cart, "Add to cart", price elements, product schema |
| Publisher | Blog, articles, bylines, publication dates, article schema |
| Agency | Portfolio, case studies, "Our services", client logos |
| Other | Default — general GEO best practices |

### Phase 2: Parallel Analysis

Запускай через `delegate_task` с 5 параллельными агентами:

| Agent | Responsibility |
|-------|---------------|
| ai-visibility | Citability, AI crawlers, llms.txt, brand mentions |
| platform-analysis | ChatGPT, Perplexity, Google AIO, Gemini, Bing Copilot readiness |
| technical | SSR/JS, Core Web Vitals, security, mobile, crawlability |
| content | E-E-A-T, readability, AI-content detection, topical authority |
| schema | JSON-LD detection, validation, generation |

### Phase 3: Synthesis

1. Собрать все subagent отчёты
2. Вычислить composite GEO Score (0-100)
3. Сгенерировать prioritized action plan
4. Вывести клиент-готовый отчёт

---

## Scoring Methodology

> **Что измеряет score:** это **readiness proxy** — техническая и структурная готовность сайта к цитированию AI-движками. Это НЕ вероятность цитирования: реальная видимость зависит от ранга в organic, конкуренции за запрос, freshness и качества контента — всего, что curl-аудит не видит.

### Composite GEO Score (0-100)

```
GEO_Score = (Citability   * 0.25)
          + (Brand        * 0.20)
          + (EEAT         * 0.20)
          + (Technical    * 0.15)
          + (Schema       * 0.10)
          + (Platform     * 0.10)
```

| Range | Rating | Meaning |
|-------|--------|--------|
| 90–100 | Excellent | Готовность максимальная: технических барьеров нет |
| 75–89 | Good | Сильная база, есть куда расти |
| 60–74 | Fair | Умеренная готовность, значительные возможности |
| 40–59 | Poor | Слабые сигналы, цитирование маловероятно |
| 0–39 | Critical | Технически недоступен для большинства AI-движков |

---

## Category 1: AI Citability & Visibility (25%)

**Sub-score composite:**

| Component | Weight |
|-----------|--------|
| Citability Score | 35% |
| Brand Mention Score | 30% |
| Crawler Access Score | 25% |
| llms.txt Score | 10% |

### Citability Scoring (per content block)

Каждый content block (section bounded by headings) скорится по 5 измерениям:

| Dimension | Max | Key signals |
|-----------|-----|-------------|
| Answer Block Quality | 30 | Definition patterns ("X is…"), answer in first 60 words, question heading, short sentences (5–25 words), attributed claims |
| Self-Containment | 25 | 134–167 word optimal (10pts), 100–200 (7pts), 80–250 (4pts); pronoun density <2% (8pts); 3+ proper nouns (7pts) |
| Structural Readability | 20 | Avg sentence 10–20 words (8pts); list transitions (4pts); numbered items (4pts); paragraph breaks (4pts) |
| Statistical Density | 15 | Percentages (3pts each, max 6); dollar amounts (3pts, max 5); numbers with units (2pts, max 4); years (2pts); named sources (2pts) |
| Uniqueness Signals | 10 | Original-research language (5pts); case studies (3pts); specific tool/product mentions (2pts) |

Page citability = average of top 5 scoring blocks.

### Crawler Access Score

Start at 100. Deduct:
- 15 pts per critical crawler blocked (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, GoogleBot)
- 5 pts per secondary crawler blocked
- 10 pts if no sitemap referenced in robots.txt
- Floor at 0

**AI Crawlers to check:**

| Crawler | Service |
|---------|---------|
| GPTBot | OpenAI training + ChatGPT search |
| OAI-SearchBot | OpenAI search-only |
| ChatGPT-User | ChatGPT browsing |
| ClaudeBot | Anthropic / Claude |
| PerplexityBot | Perplexity AI |
| Amazonbot | Amazon / Alexa AI |
| Google-Extended | Google Gemini training |
| Bytespider | ByteDance / TikTok |
| CCBot | Common Crawl |
| Applebot-Extended | Apple Intelligence |
| FacebookBot | Meta AI |
| Cohere-ai | Cohere |

### llms.txt Score

| Score | Condition |
|-------|-----------|
| 0 | Absent |
| 30 | Present but malformed |
| 50 | Present, valid, minimal content |
| 70 | Present, valid, covers primary content |
| 90–100 | Comprehensive + /llms-full.txt available |

**llms.txt format:**
```
# Site Name

> Optional blockquote description

## Section
- [Title](url): Description

## Optional
- [Title](url): Description
```

---

## Category 2: Brand Authority Signals (20%)

| Platform | Max Points | Method |
|----------|-----------|--------|
| Wikipedia | 30 | Wikipedia API search + Wikidata entity lookup |
| Industry/niche sources | 25 | G2, Trustpilot, Capterra, press, authoritative sites |
| Reddit | 20 | Presence, recency, sentiment of discussions |
| YouTube | 15 | Official channel + third-party coverage |
| LinkedIn | 10 | Company page presence and activity |

**Wikipedia check (CRITICAL):** Используй `terminal` с `curl` к Wikipedia API:
```bash
curl -s "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=BRAND_NAME&format=json" | python3 -c "
import json,sys
r=json.load(sys.stdin)
results=r.get('query',{}).get('search',[])
if results: print(f'FOUND: {results[0][\"title\"]}')
else: print('NOT FOUND')
"
```

---

## Category 3: Content Quality & E-E-A-T (20%)

| Component | Weight | Signals |
|-----------|--------|---------|
| E-E-A-T (combined) | 60% | Experience, Expertise, Authoritativeness, Trustworthiness |
| Content Metrics | 15% | Word count, Flesch readability, paragraph length, heading hierarchy |
| AI Content Assessment | 10% | Generic patterns vs authorial voice, original data |
| Topical Authority | 10% | Content breadth, internal linking, hub-cluster structure |
| Content Freshness | 5% | Publication/modification dates, recency |

### E-E-A-T Dimensions (each 0-25)

**Experience:** Original research, case studies with measurable outcomes, first-hand accounts, before/after comparisons, specific names and figures.

**Expertise:** Named author with credentials, linked author page, technical depth, methodology transparency, Person schema.

**Authoritativeness:** About page quality, external citations, industry recognition, media mentions, sameAs schema links.

**Trustworthiness:** HTTPS, contact information, privacy policy, editorial standards, transparent sourcing, publication dates.

### AI Content Red Flags

- Generic phrasing ("in today's digital landscape", "it's important to note")
- No specifics — applies to any company/situation
- Zero original data
- Perfect structure, empty substance
- Hedging overload ("may", "might", "could potentially")
- No authorial voice
- Repetitive thesis restatement

---

## Category 4: Technical Foundations (15%)

| Component | Weight |
|-----------|--------|
| SSR / JS dependency | 25% |
| Meta tags & indexability | 15% |
| Crawlability (robots.txt, sitemap) | 15% |
| Security headers | 10% |
| Core Web Vitals risk | 10% |
| Mobile optimization | 10% |
| URL structure | 5% |
| Response headers & status | 5% |
| Additional checks | 5% |

### SSR Check (CRITICAL for GEO)

Многие AI-краулеры не исполняют JavaScript или не ждут рендера — в отличие от Googlebot. Поэтому client-side-only контент рискует остаться невидимым для части AI-движков. Проверяй актуальные спецификации: ClaudeBot (support.anthropic.com), OpenAI publisher FAQ, PerplexityBot docs.

**Client-side rendering red flags:**
- Empty `<body>` with single `<div id="root">` or `<div id="app">`
- Framework bundles without SSR signals
- `<noscript>` tags with fallback content
- Content loaded via API calls

**SSR signals:**
- Full HTML content in initial response
- `__NEXT_DATA__` (Next.js), `__NUXT__` (Nuxt.js)
- `data-reactroot` or `data-server-rendered`
- Substantial text in `<body>` before scripts

### Security Header Deductions

| Missing | Deduction |
|---------|-----------|
| HTTPS | -30 (critical) |
| HSTS | -10 |
| CSP | -10 |
| X-Frame-Options | -5 |
| X-Content-Type-Options | -5 |
| Referrer-Policy | -5 |
| Permissions-Policy | -3 |

### Meta Tags Checklist

| Tag | Check |
|-----|-------|
| `<title>` | 50-60 chars, primary keyword |
| `<meta description>` | 150-160 chars, compelling |
| `<link canonical>` | Self-referencing or preferred |
| `<meta robots>` | No noindex/nofollow |
| `<meta viewport>` | width=device-width, initial-scale=1 |
| `<html lang>` | Correct language code |
| Open Graph | og:title, og:description, og:image, og:url |
| Twitter Card | twitter:card, twitter:title, twitter:image |

---

## Category 5: Structured Data (10%)

| Component | Max Points | Criteria |
|-----------|-----------|----------|
| Organization/LocalBusiness | 20 | Present (10), sameAs 3+ platforms (20) |
| Article/content schema | 15 | Present (8), author as Person (12), dateModified (15) |
| Person schema | 15 | Present (8), sameAs (12), jobTitle+knowsAbout (15) |
| sameAs completeness | 15 | 1-2 (5), 3-4 (10), 5+ incl Wikipedia (15) |
| speakable | 10 | Present and targeting content sections |
| BreadcrumbList | 5 | Present and valid |
| WebSite + SearchAction | 5 | Present and valid |
| No deprecated schemas | 5 | No HowTo (removed Sep 2023), SpecialAnnouncement |
| JSON-LD format | 5 | All JSON-LD, not Microdata/RDFa |
| Validation | 5 | All pass syntax + property validation |

**Deprecated schemas:** HowTo (removed Sep 2023), FAQPage (restricted Aug 2023), SpecialAnnouncement (deprecated), CourseInfo (deprecated).

**JS-injected schema warning:** JSON-LD injected via JS may be missed by AI crawlers. Schema must be in initial HTML.

### Schema Templates

Готовые JSON-LD шаблоны в `references/`:
- `organization.json` — Organization with sameAs
- `local-business.json` — LocalBusiness
- `software-saas.json` — SoftwareApplication
- `article-author.json` — Article + Person (E-E-A-T)
- `product-ecommerce.json` — Product with offers
- `website-searchaction.json` — WebSite + SearchAction

---

## Category 6: Platform Optimization (10%)

### Google AI Overviews (40+30+30)
- Content structure: question headings, answer paragraphs (40-60 words), comparison tables
- Source authority: top-10 ranking, authoritative citations
- Technical: clean heading hierarchy, schema, fast loading

### ChatGPT Web Search (35+40+25)
- Entity recognition: Wikipedia, Wikidata, sameAs schema
- Content: factual citable statements, statistical claims, expert attribution
- Crawler access: OAI-SearchBot + ChatGPT-User allowed

### Perplexity AI (30+30+20+20)
- Community validation: Reddit, Quora, Stack Overflow
- Source directness: primary source, verifiable data
- Content freshness: dates visible, current
- Technical access: PerplexityBot allowed, SSR

### Google Gemini (35+30+35)
- Google ecosystem: YouTube, Google Business Profile, Google Scholar
- Knowledge Graph: entity in KG, sameAs, consistent NAP
- Content quality: long-form, multi-format, topical clustering

### Bing Copilot (30+30+20+20)
- Bing index: IndexNow, Bing Webmaster Tools, msvalidate.01
- Content: structured, professional, authoritative
- Microsoft ecosystem: LinkedIn, GitHub
- Technical: Bing-compatible structured data, fast, mobile

---

## Output Format

### Full Audit Report

```markdown
# GEO Audit Report — [domain]
**Date:** [date]
**Business Type:** [type]
**GEO Score: [X]/100** [Critical/Poor/Fair/Good/Excellent]

## Score Breakdown

| Category | Score | Weight | Weighted | Status |
|----------|-------|--------|----------|--------|
| AI Citability & Visibility | [X]/100 | 25% | [X] | [Status] |
| Brand Authority Signals | [X]/100 | 20% | [X] | [Status] |
| Content Quality & E-E-A-T | [X]/100 | 20% | [X] | [Status] |
| Technical Foundations | [X]/100 | 15% | [X] | [Status] |
| Structured Data | [X]/100 | 10% | [X] | [Status] |
| Platform Optimization | [X]/100 | 10% | [X] | [Status] |
| **TOTAL** | | | **[X]** | **[Status]** |

## AI Platform Readiness

| Platform | Score | Main Gap |
|----------|-------|---------|
| Google AI Overviews | [X]/100 | [gap] |
| ChatGPT Web Search | [X]/100 | [gap] |
| Perplexity AI | [X]/100 | [gap] |
| Google Gemini | [X]/100 | [gap] |
| Bing Copilot | [X]/100 | [gap] |

## Critical Findings
### FINDING 1: [title]
**Evidence:** [evidence]
**Impact:** [impact on AI visibility]
**Severity:** CRITICAL/HIGH/MEDIUM/LOW
**Fix:** [specific fix]
**Effort:** [time estimate]

## Adversarial Self-Check (обязательный раздел отчёта)

Каждый отчёт обязан отвечать на три вопроса — иначе вывод сильнее данных:

- **Что curl-аудит не увидел:** [JS-рендеринг, реальный ранк в organic, бренд-упоминания внутри ответов AI, поведение пользователей].
- **Что score НЕ утверждает:** [вероятность цитирования, сравнение с конкурентами вне выборки, causality «исправил → выросли цитаты»].
- **Какое наблюдение изменило бы вывод:** [живой замер цитирования в целевом AI-движке до/после фиксов].

## Quick Wins (This Week)
| # | Action | Effort | GEO Impact | Platforms |
|---|--------|--------|-----------|-----------|

## Medium-Term (This Month)
| # | Action | Effort | GEO Impact |
|---|--------|--------|-----------|

## Strategic (This Quarter)
| # | Action | Effort | GEO Impact |
|---|--------|--------|-----------|

## Recommended JSON-LD Templates
[Generated templates for missing schemas]
```

---

## Execution Instructions

### Quick Audit (60-second snapshot)

1. `terminal curl -sL <url>` — fetch homepage HTML
2. `terminal curl -sL <url>/robots.txt` — check AI crawler access
3. `terminal curl -sL <url>/llms.txt` — check llms.txt
4. `terminal curl -sL <url>/sitemap.xml` — check sitemap
5. Scan HTML for JSON-LD, meta tags, SSR signals
6. `web_search` for brand mentions on Wikipedia, Reddit, YouTube, LinkedIn
7. Calculate preliminary scores
8. Output inline summary

### Full Audit

1. Run Discovery phase (fetch homepage, detect type, extract pages)
2. Launch 5 parallel subagents via `delegate_task`:
   - Each agent gets the URL + relevant methodology section
   - Each returns structured report section with sub-score
3. Synthesize: collect scores, compute composite, generate action plan
4. Output full report to workspace file

### Tools Mapping

| Original (Claude Code) | Hermes |
|------------------------|--------|
| WebFetch | `web_extract` or `terminal curl -sL` |
| Bash | `terminal` |
| Read | `read_file` |
| Write | `write_file` |
| Glob/Grep | `search_files` |
| Subagents | `delegate_task` |

### Fetching HTML (critical for schema detection)

`web_extract` converts HTML to markdown and strips `<head>` — this removes JSON-LD.
For schema detection, use `terminal`:
```bash
curl -sL '<url>' | grep -o '<script type="application/ld+json">[^<]*</script>'
```

Or fetch full HTML and parse with Python:
```bash
curl -sL '<url>' > /tmp/page.html
python3 -c "
import re, json
html = open('/tmp/page.html').read()
blocks = re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
for b in blocks:
    try:
        data = json.loads(b)
        print(json.dumps(data, indent=2))
    except: pass
"
```

---

## Quality Gates

- **Crawl limit:** Max 50 pages per audit
- **Timeout:** 30 seconds per page fetch
- **Rate limiting:** 1-second delay between requests
- **Robots.txt:** Always respect, always check
- **Duplicate detection:** Skip pages with >80% content similarity

---

## Market Context (Why GEO Matters)

> ⚠️ **Эти цифры — оценки из маркетинговых источников без первичной методологии.** Не использовать в клиентских отчётах как факты; перед цитированием проверять первоисточник.

| Metric | Value | Статус |
|--------|-------|--------|
| GEO services market (2025) | $850M-$886M | оценка, первоисточник не верифицирован |
| Projected GEO market (2031) | $7.3B (34% CAGR) | прогноз |
| AI-referred sessions growth | +527% (Jan-May 2025) | вендорская метрика |
| AI traffic conversion vs organic | 4.4x higher | вендорская метрика |
| Google AI Overviews reach | 1.5B users/month | оценка Google I/O 2025 |
| ChatGPT weekly active users | 900M+ | публичное заявление OpenAI |
| Perplexity monthly queries | 500M+ | вендорская метрика |
| Gartner: search traffic drop by 2028 | -50% | прогноз Gartner |
| Marketers investing in GEO | Only 23% | вендорский опрос |
| Brand mentions vs backlinks for AI | 3x stronger correlation | вендорская корреляция |

---

## Pitfalls

- **web_extract strips JSON-LD** — always use `terminal curl` for schema detection
- **AI crawlers и JS** — не все AI-краулеры исполняют JS (Google рендерит, многие нет). SSR — приоритет No1, потому что он работает для всех
- **Wikipedia API, not web search** — `site:wikipedia.org` gives false negatives
- **HowTo schema is dead** — removed Sep 2023, don't recommend adding
- **FAQPage restricted** — only government/health authority sites get rich results
- **JS-injected schema invisible to AI** — must be in initial HTML
- **403 to non-browser agents** — common WordPress security plugin issue, blocks all AI crawlers

---

## AI Search Engine Spec Sheets — платформенная специфика (2026)

> Каждый AI-движок цитирует по-разному. Аудит без учёта специфики платформы — это аудит «в среднем по больнице». Ниже — что именно ловит каждый движок, с research-числами.

### ChatGPT Search (OpenAI)

| Параметр | Данные |
|---|---|
| **Механика поиска** | Sequential — последовательно запрашивает сайты, агрегирует (не параллельно, как Perplexity) |
| **Цитирует** | ~16% найденных страниц (85% — никогда не цитируются) |
| **Цитат на ответ** | 3.1–3.4 уникальных доменов |
| **Top-фактор** | 44.2% цитат из первых 30% контента (Kevin Indig, 1.2M ответов) |
| **Что любит** | Answer-first блоки в первых 40-60 словах, self-contained параграфы, entity density |
| **Что игнорирует** | Длинные «обёрточные» интро, маркетинговый copy без фактов |
| **Crawler** | `GPTBot`, `OAI-SearchBot`, `ChatGPT-User` |
| **Ключевой вывод** | Если ответа нет в первых 30% страницы — шанс цитаты падает на ~70% |

### Perplexity

| Параметр | Данные |
|---|---|
| **Механика поиска** | Parallel — одновременно запрашивает несколько источников |
| **Цитирует** | ~97% ответов содержат цитаты (почти всегда) |
| **Цитат на ответ** | 6–8 (consumer), до 17.7 (multi-constraint queries) |
| **Unique domains** | 8.52–16.81 на ответ vs ChatGPT 3.1–3.4 |
| **Пересечение с ChatGPT** | Только 11% доменов совпадают — разные пулы источников |
| **Top-фактор** | Extractable answer blocks + comparison tables + source density |
| **Что любит** | Структурированные данные, таблицы, нумерованные списки, прямые ответы |
| **Crawler** | `PerplexityBot` |
| **Ключевой вывод** | Самый «щедрый» на цитаты движок — оптимизация под Perplexity = максимальный ROI для малого бизнеса |

### Google AI Overviews (AIO) + AI Mode

| Параметр | Данные |
|---|---|
| **Охват** | AI Overviews в 25% запросов (48.7% — здоровье), 1.5B пользователей/мес |
| **Механика** | Query fan-out — расширяет запрос, тянет из broader set чем классический organic |
| **Волатильность** | 70% AIO-рангов меняются за 2-3 месяца (Authoritas) — более волатильно чем organic |
| **Top-фактор** | Entity authority + E-E-A-T + уже ранжирующий organic контент (AIO предпочитает топ-organic) |
| **Что любит** | Контент уже в топ-10 organic, schema markup, свежесть, authoritative domains |
| **Crawler** | `Google-Extended`, `Googlebot` |
| **Ключевой вывод** | AIO ≠ отдельный канал — это надстройка над organic. Нет organic-ранга = нет AIO-цитаты. Но query fan-out даёт шанс страницам вне топ-3. |

### Gemini (Google DeepMind)

| Параметр | Данные |
|---|---|
| **Механика** | 8 documented citation signals (semantic completeness + entity authority = top weight) |
| **Тренд 2026** | Сократила число источников на 33% — стала избирательнее |
| **8 сигналов** | (1) Semantic completeness, (2) Entity authority, (3) Schema types, (4) Author/brand entity, (5) Freshness, (6) Source diversity, (7) Content structure, (8) Factual grounding |
| **Что любит** | Детальные author bios, entity recognition через schema, extraction-friendly formatting |
| **Crawler** | `Googlebot` (Google ecosystem) |
| **Ключевой вывод** | Самый entity-зависимый движок — без Organization + Person schema шансов почти нет. semantic completeness > keyword match. |

### Claude (Anthropic)

| Параметр | Данные |
|---|---|
| **Web search** | Запущен 20.03.2025 (US Pro), глобально — 27.05.2025 (все планы, включая free) |
| **Механика** | Structured citation + real-time retrieval; developer-level controls через API |
| **Top-фактор** | Freshness + structured data (critical ranking factors для Claude) |
| **Что любит** | Свежий контент с датами, clean semantic HTML, author attribution |
| **Crawler** | `ClaudeBot`, `anthropic-ai` |
| **Ключевой вывод** | Claude — самый freshness-чувствительный. Контент без visible dates = ниже шанс. structured citation format = выше шанс. |

### Grok (xAI / X)

| Параметр | Данные |
|---|---|
| **Механика** | Dual-source: live web + X (Twitter) real-time feed одновременно |
| **6 фильтров** | (1) Real-time relevance, (2) X engagement signals, (3) Source authority, (4) Factual consistency, (5) Web-wide brand presence, (6) Content extractability |
| **Что любит** | Контент с активностью в X/Twitter, real-time relevance, brand presence across web |
| **Ключевой вывод** | Единственный движок, где **присутствие в X = фактор ранжирования**. Если бренда нет в X — Grok почти не цитирует. Оптимизация под Grok = GEO + X-стратегия. |

### Copilot (Microsoft)

| Параметр | Данные |
|---|---|
| **Механика** | Bing index + GPT synthesis |
| **Top-фактор** | Bing ranking signals (existing SEO) + answer extractability |
| **Crawler** | `Bytespider` (Bing) |
| **Ключевой вывод** | Оптимизация под Copilot = оптимизация под Bing + answer-first контент. Корреляция с Bing-рангом ~80%. |

---

## Cross-Platform Priority Matrix

> Не оптимизируй под все 7 платформ одинаково. Расставь приоритет по сегменту клиента.

| Платформа | Приоритет для | Фокус аудита | ROI |
|---|---|---|---|
| **ChatGPT** | B2C, массовый рынок, 900M+ WAU | Answer-first, entity density, first-30% optimization | Высокий (объём) |
| **Perplexity** | B2B, research-oriented, технические ниши | Tables, source density, structured blocks | Высочайший (97% citation rate) |
| **Google AIO** | Все сегменты, health/gov/finance | Organic top-10, E-E-A-T, schema | Высокий (1.5B reach) |
| **Gemini** | Google ecosystem, enterprise | Entity authority, semantic completeness, 8 signals | Средний (избирательнее в 2026) |
| **Claude** | Developer/technical audiences | Freshness, structured data, clean HTML | Средний (растёт) |
| **Grok** | Real-time, news, trending | X presence + web GEO | Низкий для B2B, высокий для real-time |
| **Copilot** | Enterprise, Microsoft ecosystem | Bing SEO + answer extractability | Средний (зависит от Bing-ранга) |

---

## Research-Data Table — research-обоснование (с источниками)

> Каждое число — из первоисточника. Используй в клиентских отчётах для доверия. **Каждая цифра помечена статусом: потолок / среднее / конфликт / нет методологии** — таблица с честными пометками сильнее таблицы с ровными числами.

| Факт | Число | Источник | Год | Статус |
|---|---|---|---|---|
| Quotations = visibility boost | **до +40%** (потолок, не среднее) | Aggarwal et al., GEO paper, KDD 2024 (arXiv 2311.09735) | 2024 | ⚠️ потолок: максимальный подъём на самом отзывчивом подмножестве запросов; медианный подъём значительно ниже; эффект зависит от домена запроса и позиции |
| Statistics = citation boost | **до +33%** | Aggarwal et al., KDD 2024 | 2024 | ⚠️ потолок (та же оговорка, что и для quotations) |
| Cite Sources = visibility | **+28%** (до +115% для сайтов ниже топ-3) | Aggarwal et al., KDD 2024 | 2024 | ✅ легитимно: +115% — именно для страниц вне топ-3 |
| ChatGPT citations from first 30% | **44.2%** | Kevin Indig, Growth Memo (1.2M AI answers) | 2026 | ✅ |
| Comparison tables citation boost | **2.8x** | AirOps, structuring content for LLMs | 2025 | ⚠️ вендорская метрика, методология не опубликована |
| FAQ blocks citation boost | **+156%** | AirOps | 2025 | ⚠️ вендорская метрика, методология не опубликована |
| Clean heading hierarchy boost | **3.2x** | AirOps | 2025 | ❌ конфликт: независимая оценка Ahrefs Q1 2026 даёт 1.2–1.4x; методология AirOps не опубликована — использовать нижнюю оценку |
| Top-cited pages updated within 30 days | **76%** | Ahrefs (17M citations, 7 AI platforms) | 2025 | ✅ |
| AI cites content fresher than organic | **+25.7%** | Ahrefs | 2025 | ✅ |
| Long-form (2000+ words) citations | **3x** vs <800 words | SE Ranking (2.3M pages, 295K domains) | 2025 | ❌ конфликт: Ahrefs Dec 2025 — 53,4% цитат AI Overviews со страниц <1000 слов, средняя длина цитируемой 1282 слова. Вывод: **длина не рычаг, плотность — рычаг** |
| Articles 2900+ words avg citations | **5.1** vs 3.2 for <800 words | SE Ranking | 2025 | ❌ тот же конфликт (см. выше) |
| 120-180 words between headings | **+70%** ChatGPT citations | SE Ranking | 2025 | ⚠️ методология не опубликована |
| 78,4% цитат по вопросным запросам — из заголовков-вопросов (H2/H3 как вопрос) | **78,4%** | Ahrefs Q1 2026 | 2026 | ✅ подтверждает правило G02 |
| Плотность имён собственных в цитируемом тексте | **~20,6%** vs 5–8% в обычном (3–4x концентрация) | Ahrefs Q1 2026 | 2026 | ✅ подтверждает правило G03 |
| Цитаты из середины абзацев vs первых предложений | **53% / 24,5%** | Ahrefs Q1 2026 | 2026 | ✅ уточняет G01: ответ должен быть в первых 30% документа, но внутри абзаца не обязательно первое предложение |
| Perplexity citation rate | **97%** of answers | AuthorityTech | 2026 | ⚠️ вендорская метрика |
| ChatGPT citation rate | **16%** of retrieved pages | ThatDevPro | 2026 | ⚠️ |
| Perplexity unique domains/answer | **8.52–16.81** vs ChatGPT 3.1–3.4 | Omniscient Digital, LumenGEO | 2026 | ⚠️ |
| ChatGPT–Perplexity domain overlap | **only 11%** | Consultus Digital | 2026 | ⚠️ |
| Google AIO reach | **25% of queries** (48.7% health) | Authoritas | 2026 | ⚠️ |
| AIO ranking volatility | **70% change in 2-3 months** | Authoritas | 2026 | ⚠️ |
| Gemini source reduction | **-33%** (more selective) | BrandCited | 2026 | ⚠️ |
| AI traffic conversion vs organic | **4.4x higher** | Market data | 2025 | ⚠️ оценка |
| Gartner: search traffic drop by 2028 | **-50%** | Gartner | 2025 | ⚠️ прогноз |

### Конфликты данных — как с этим работать в аудите

1. **Потолок ≠ среднее (Princeton GEO).** Цифры +40%/+33% — максимальный эффект на самом отзывчивом подмножестве запросов. В клиентском отчёте формулировка: «до +40% в лучших случаях», никогда «+40% в среднем». Эффект зависит от домена запроса и позиции источника.
2. **Длина vs плотность.** SE Ranking (3x для 2000+ слов) и Ahrefs (53,4% цитат со страниц <1000 слов) противоречат друг другу напрямую. Рабочий вывод: **плотность извлекаемых блоков на единицу текста — рычаг; общая длина — нет.** Не рекомендуй «написать длиннее», рекомендуй «уплотнить ответами».
3. **Heading hierarchy.** AirOps 3.2x — без опубликованной методологии; Ahrefs Q1 2026 — 1.2–1.4x. В отчёте использовать 1.2–1.4x, эффект реальный, но скромный.
4. **FAQ.** AirOps +156% — без методологии; Google ограничил FAQPage rich results (2023). Позиция: FAQ-контент как формат полезен, но не продавать как «+156% к цитируемости».
5. **Что усилено в правилах.** G02 (question headings) и G03 (entity density) подтверждены независимыми цифрами Ahrefs Q1 2026 — это самые надёжные правила категории A. G01 уточнён: answer-first означает ответ в первых 30% документа; внутри абзаца цитата может быть взята и из середины (53% цитат — из середины абзацев, 24,5% — из первых предложений).

---

## 6 Intelligence Dimensions — второй слой скоринга (0-5 rubric)

> Foundational (92 правила) = «есть ли оно». Intelligence = «насколько оно хорошо для AI». Финальный скор = 50% foundational + 50% intelligence → буква A-F.

### Answer Readiness (0-5)
Если пользователь задал вопрос по теме сайта — найдётся ли прямой ответ?
- **0** = нет ответов, только promo/navigational
- **1** = расплывчато, «ходит вокруг»
- **2** = ответы есть, но buried deep
- **3** = несколько вопросов отвечаем; definition-first/FAQ-style
- **4** = большинство вопросов отвечаем; ответы ведут секции
- **5** = выдача (FAQ-блоки, definition-first, Q&A формат throughout)
- *Research: answer-first = 4.8x больше цитат*

### Quotability (0-5)
Можно ли вытащить чистый self-contained блок 40-60 слов?
- **0** = нечего извлекать (interactive-only, dense block)
- **1** = нужен контекст всей страницы
- **2** = несколько блоков, но большинство требуют окружения
- **3** = несколько self-contained параграфов, списки
- **4** = хорошая quotability (таблицы, списки, FAQ, answer blocks)
- **5** = highly quotable (comparison tables, step-by-step, definitions throughout)
- *Research: tables 2.8x, FAQ +156%*

### Evidence Density (0-5)
Статистика, data points, named sources, in-text citations?
- **0** = нет, только marketing copy
- **1** = «best in class», «industry leading» — vague
- **2** = generalities, редкие data points
- **3** = статистика и named sources, несколько внешних
- **4** = высокая плотность (числа, даты, sources, links)
- **5** = exceptional (статистика каждые 150-200 слов, in-text citations throughout)
- *Research: in-text citations +115%, statistics +40%*

### Content Depth (0-5)
Достаточно substance для полного ответа?
- **0** = empty/placeholder
- **1** = несколько предложений
- **2** = thin (surface-level, missing key details)
- **3** = adequate (main points, но не хватает sub-topics)
- **4** = rich (comprehensive, sub-topics, examples, data)
- **5** = exceptional (authoritative, multi-faceted, go-to reference)
- *Research: 2000+ слов = 3x citations*

### Freshness (0-5)
Достаточно свежий для уверенной цитаты?
- **0** = нет date signals, abandoned
- **1** = даты есть, но явно устаревшие (2+ года)
- **2** = умеренно dated, нет «last updated»
- **3** = reasonably current OR explicit «last updated»
- **4** = recent + update timestamps + current references
- **5** = clearly current (recent dates, active maintenance)
- *Research: 76% топ-цитируемых обновлены за 30 дней; AI cites 25.7% fresher*

### Structural Clarity (0-5)
HTML парсится в readable text?
- **0** = unreadable (no text, blocked, non-semantic)
- **1** = very poor (walls of text, no headings)
- **2** = weak (some structure but confusing)
- **3** = adequate (clear headings, topic identifiable)
- **4** = good (clean H1→H2→H3, scannable, purpose obvious)
- **5** = excellent (perfect heading outline, semantic HTML, zero noise)
- *Research: clean hierarchy = 3.2x citations*

### Финальный подсчёт
1. Intelligence score = `average(6 scores) × 20` → 0-100
2. Final = `round(0.5 × foundationalScore + 0.5 × intelligenceScore)`
3. Grade: A+ (95-100) · A (90-94) · A- (85-89) · B+ (80-84) · B (75-79) · B- (70-74) · C+ (65-69) · C (60-64) · C- (55-59) · D (40-54) · F (<40)

---

## AI Bot Access — 9 crawlers (robots.txt template)

> Если AI-бот заблокирован — ничего другого не имеет значения. Это #0 приоритет.

```txt
User-agent: *
Allow: /

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Bytespider
Allow: /

User-agent: CCBot
Allow: /

Sitemap: https://YOURDOMAIN.com/sitemap.xml
```

**Проверка в аудите**: fetch `/robots.txt`, проверить что ни один из 9 ботов не в `Disallow`. Если блокирован →.Score = 0 (автоматический fail).

---

## RSS/Atom Feed (8 pts — нового)

> AI-краулеры используют RSS для discovery и freshness signals. Без feed — медленнее индексация.

**Проверка**: наличие `<link rel="alternate" type="application/rss+xml">` в `<head>` + доступный `/feed.xml` или `/rss.xml`.

**Fix**: сгенерировать feed для ключевых страниц (blog, updates, changelog). Для статичных сайтов — ручной XML или фреймворк-генератор.

---

## Freshness Meta Tags

> Не путать с `<time>` — это Open Graph + article meta, которые AI-движки читают отдельно.

```html
<meta property="article:published_time" content="2026-08-30T00:00:00+03:00" />
<meta property="article:modified_time" content="2026-09-10T00:00:00+03:00" />
```

**Проверка**: presence в `<head>` + соответствие `<time datetime>` в body. Несоответствие дат = штраф.

---

## llms.txt — proper structure (template)

> Помнить: llms.txt ≠ фактор ранжирования (Google 05.2026 это снял). Но = courtesy для агентов и structure. Делать, но не продавать как «magic».

```markdown
# [Site Name]

> Brief description of what your site/product does.

## Documentation
- [Getting Started](https://yourdomain.com/docs/getting-started)
- [API Reference](https://yourdomain.com/docs/api)

## Key Pages
- [About](https://yourdomain.com/about)
- [Pricing](https://yourdomain.com/pricing)
- [Blog](https://yourdomain.com/blog)

## Policies
- [Terms of Service](https://yourdomain.com/terms)
- [Privacy Policy](https://yourdomain.com/privacy)
```

**Минимум для pass**: heading + links + 100+ characters.

---

## Framework-Specific Fix Patterns

> Готовые сниппеты для каждого фреймворка — не «общие советы», а код.

### Plain HTML (твой Discovery лендинг)
- JSON-LD в `<head>` перед `</head>`
- `<h1>` вместо `<div class="hero-display">` — CSS не меняется
- `<link rel="canonical">` в `<head>`
- `<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">`
- `<meta name="twitter:card" content="summary_large_image">`
- `<meta property="article:published_time">` + `<meta property="article:modified_time">`
- `<ul>/<li>` вместо `<div>` для списков
- `<blockquote>+<cite>` для цитат
- `robots.txt` + `sitemap.xml` в корне репо
- `llms.txt` — optionally, не как фактор

### Next.js (App Router)
- `app/layout.tsx`: metadata object + JSON-LD via `dangerouslySetInnerHTML`
- `app/robots.ts`: MetadataRoute.Robots с 9 AI bots allowed
- `app/sitemap.ts`: MetadataRoute.Sitemap с lastmod
- `opengraph-image.tsx`: dynamic OG image generation
- `article:published_time` / `article:modified_time` in metadata

### Astro
- `@astrojs/sitemap` for auto sitemap with lastmod
- `<link rel="alternate" type="application/rss+xml" href="/feed.xml">` in layout
- JSON-LD in frontmatter-rendered `<script>`
- `robots.txt` in `public/`

### WordPress
- Yoast/RankMath for meta + schema (но проверить AI-bot access)
- `functions.php`: add JSON-LD for Article/Organization
- Remove `noindex` from public pages
- Check security plugins for 403 to AI crawlers

### SvelteKit
- `<svelte:head>` for meta + canonical + JSON-LD
- `+page.svelte`: article:published_time / modified_time
- `src/robots.txt` + `src/sitemap.xml`

---

## Межсегментная шкала интерпретации (readiness по сегментам)

> Score сам по себе ничего не значит без базы сравнения. Шкала собрана на межсегментных прогонах 20.09.2026 (банки / медиа / B2B, 16 URL, 11 скоренных) и уточняется каждым следующим циклом. Сравнивай клиента с его сегментом, не со «средним рынком».

| Сегмент | Средний score (2026-09-20) | Структурная особенность | Типовой главный gap | Что это значит для продавца |
|---|---|---|---|---|
| **Медиа** | ~64 (C+) | SSR у всех (бизнес = быть индексируемым); schema в SSR-HTML у ~40% | Organization-схема, canonical, RSS | Точечные доработки, разовый чек; для демонстрации слабый сегмент |
| **Банки** | ~63 (C) | Половина топ-5 контент-невидима без JS (JS-shell / WAF / JS-challenge); TLS на RU-корневом УЦ ломает handshake для зарубежных краулеров | Полная невидимость контента; JSON-LD без `@id` | Самый наглядный вход: «вас не видит ChatGPT» проверяется за 10 минут |
| **B2B-сервисы** | ~61 (C) | Все открыты для краулеров, но структура слабая: 3/5 без JSON-LD, 2/5 без canonical | JSON-LD, answer-first контент, даты | **Самый продаваемый сегмент**: клиенты B2B ищут поставщиков через AI-поиск, gap конвертируется в воронку |

Правила чтения шкалы:
1. **Внутрисегментный разброс больше межсегментного.** Разница сегментов — 3–4 пункта; внутри B2B — 33 пункта (bitrix24 76/B vs amocrm 43/D). Продавай конкретному клиенту его позицию относительно ближайшего конкурента, не «сегмента».
2. **«Не наблюдали» искажает средние.** Сегмент, где 2/5 сайтов невидимы (банки), выглядит лучше, чем есть, если невидимые исключить из среднего. Всегда указывай «скоренных X из Y».
3. **Готовность не коррелирует с размером.** Крупнейшие бренды сегмента могут быть хуже подготовлены среднего игрока (Сбер vs ПСБ) — это аргумент против «нам не надо, мы и так большие».
4. **Проверяй не только код ответа.** llms.txt со статусом 200 может быть HTML-заглушкой (soft-404); проверяй content-type и первый байт контента.

---

## Execution Flow v3 (полный пайплайн)

```
1. AI Bot Access:    fetch /robots.txt → check 9 crawlers (FAIL = stop)
2. Quick scan:       geo-lint <url> → baseline 92-rule score
3. Foundational:     16 deterministic checks (title, meta, H1, schema, canonical, OG, links, alt, text depth, indexability, AI-meta, heading hierarchy, llms.txt, bot access, RSS)
4. Intelligence:     6 dimensions (Answer Readiness, Quotability, Evidence, Depth, Freshness, Structure) — 0-5 rubric
5. Platform audit:   check per-platform signals (ChatGPT first-30%, Perplexity table density, AIO organic rank, Gemini entity authority, Claude freshness, Grok X-presence, Copilot Bing-rank)
6. Synthesis:        50% foundational + 50% intelligence → A-F grade
7. Report:           client-ready markdown + prioritized fixes (platform-specific)
8. Post-audit:       elmo init → longitudinal tracking (retainer)
```

---

## Изменения 1.3.0 (2026-09-10)

- Добавлено: **AI Search Engine Spec Sheets** — 7 платформ с механикой цитирования, research-числами и crawler-именами
- Добавлено: **Cross-Platform Priority Matrix** — приоритет платформ по сегменту клиента
- Добавлено: **Research-Data Table** — 22 research-факта с первоисточниками (Aggarwal KDD 2024, Ahrefs, SE Ranking, Kevin Indig, AirOps, Authoritas, BrandCited)
- Добавлено: **6 Intelligence Dimensions** — второй слой скоринга 0-5 (Answer Readiness, Quotability, Evidence Density, Content Depth, Freshness, Structural Clarity) с rubric и research-обоснованием
- Добавлено: **A-F Grading** — буквенная оценка поверх цифрового скора
- Добавлено: **AI Bot Access** — 9 crawlers + готовый robots.txt template
- Добавлено: **RSS/Atom Feed** — как проверка (8 pts)
- Добавлено: **Freshness Meta Tags** — article:published_time / article:modified_time
- Добавлено: **llms.txt proper structure** — шаблон + минимум для pass
- Добавлено: **Framework-Specific Fix Patterns** — Next.js, Astro, WordPress, SvelteKit, Plain HTML
- Добавлено: **Execution Flow v3** — полный пайплайн с platform audit
- Источники: onvoyage-ai/gtm-engineer-skills (MIT, 1304★), IJONIS/geo-lint (MIT), elmohq/elmo (MIT), Aggarwal et al. KDD 2024, Ahrefs, SE Ranking, Kevin Indig, AirOps, Authoritas, BrandCited
