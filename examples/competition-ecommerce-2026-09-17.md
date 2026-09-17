# Конкурентный баттлтест GEO-аудита — e-commerce РФ (17.09.2026)

Второй цикл баттлтеста: **5 сайтов одной отрасли (e-commerce РФ)** с сравнительной разбивкой по конкурентам. Прогон скилла по модели:

`Final = 50% Foundational (92 правила) + 50% Intelligence (6 измерений) → Grade A-F`

## Метод

Каждый сайт проверен по 5 направлениям (foundational):
1. **HTML/SSR** — размер главной, реальный текст в HTML (без JS-исполнения)
2. **JSON-LD** — число блоков, типы сущностей (`@type`), валидность `json.loads`
3. **llms.txt** — присутствие, размер, структура (заголовок, ссылки)
4. **robots.txt** — живой ли, sitemap, доступ AI-краулеров (GPTBot, ClaudeBot, PerplexityBot, OAI-SearchBot, Google-Extended)
5. **Meta/структура** — title, description, OG, canonical, H1-H3

Измерения intelligence (0-5): Answer Readiness, Quotability, Evidence Density, Content Depth, Freshness, Structural Clarity.

**Доступность целевых сайтов (curl, 25с, UA Mozilla/5.0):**

| Запланированный | Статус | Что отдаёт |
|---|---|---|
| ozon.ru | 🔒 307 redirect-loop (`/?__rr=1` → 307 → …) | закрыт для curl |
| wildberries.ru | 🔒 498, 1132 B — JS-shell | повторно подтверждён JS-shell (как в цикле 16.09) |
| market.yandex.ru | ✅ 200, 2.0 МБ | SSR |
| megamarket.ru | 🔒 403, JS-spinner | закрыт |
| lamoda.ru | 🔒 403, JS-spinner | закрыт |
| _альтернативы_: dns-shop.ru (401) · sbermegamarket.ru (403) | 🔒 | закрыты |
| **→ взяты из той же отрасли** | **citilink.ru · vkusvill.ru · holodilnik.ru · detmir.ru** | ✅ |

Итоговая пятёрка: **market.yandex.ru, citilink.ru, vkusvill.ru, holodilnik.ru, detmir.ru**.

## Результаты — сравнительная таблица

| Сайт | HTML (B) | JSON-LD | llms.txt | robots | Score | Grade | Главный gap |
|---|---|---|---|---|---|---|---|
| market.yandex.ru | 2 057 102 | 1 блок: WebSite + SearchAction | 404 (soft, SPA) | ✅ 16 488, sitemap, AI-боты открыты | **52** | F | **0 заголовков H1-H6 в HTML**, нет description/OG/canonical; JSON-LD = только WebSite; llms отсутствует |
| citilink.ru | 1 011 427 | 0 блоков | 404 | ✅ 5 071, sitemap | **34** | F | 0 JSON-LD (ни microdata), llms нет, нет H1, видимый текст = 812 слов |
| vkusvill.ru | 421 351 | 2 блока: Organization/GroceryStore + WebSite + OfferCatalog (валидные) | ✅ 5 365, 48 ссылок | ✅ 2 101, sitemap | **68** | C | Нет FAQ/answer-блоков и дат; H2/H3 почти нет (1 H1) |
| holodilnik.ru | 565 569 | 1 блок: Organization | 404 (soft, SPA) | ✅ 2 686, sitemap | **23** | F | Видимый текст = 189 слов (меню/иконки), битый `<title>`, нет canonical |
| detmir.ru | 2 250 068 | 0 блоков | 404 | ✅ 6 306, но **без sitemap** | **51** | F | 0 JSON-LD, нет sitemap в robots, нет H1 |

**Средний score: 45.6 (F).** Худший средний результат из двух циклов — e-commerce РФ заметно менее AI-ready, чем средний рынок (66.4 в цикле 16.09).

## Детали по измерениям (intelligence 0-5)

| Сайт | Answer | Quotab. | Evidence | Depth | Fresh | Struct | Σ/30 |
|---|---|---|---|---|---|---|---|
| market.yandex.ru | 2 | 2 | 2 | 4 | 4 | 1 | 15/30 |
| citilink.ru | 1 | 1 | 1 | 2 | 2 | 2 | 9/30 |
| vkusvill.ru | 2 | 2 | 2 | 3 | 3 | 3 | 15/30 |
| holodilnik.ru | 0 | 1 | 1 | 2 | 1 | 1 | 6/30 |
| detmir.ru | 2 | 2 | 2 | 3 | 3 | 3 | 15/30 |

## Лидер сегмента

**vkusvill.ru (68/C) — единственный сайт из пятёрки, готовый к AI-поиску.** Он выигрывает не за счёт трафика, а за счёт AI-гигиены: единственный с валидным llms.txt (5 365 B, 48 ссылок), самым богатым JSON-LD (Organization/GroceryStore + OfferCatalog — сущность магазина распознаётся напрямую) и полным мета-набором (description, OG×7, canonical, H1). **market.yandex.ru (52/F)** отдаёт самый большой SSR-контент в РФ (2 МБ, ~18 тыс. слов) — AI-краулеры *видят* его, — но 0 заголовков, 0 мета и 1 блок схемы обнуляют извлекаемость: краулер получает «стену текста без карты». Вывод: в e-commerce РФ побеждает не лидер по выручке, а сайт с базовой структурой — объём контента без headings/schema не конвертируется в цитируемость.

## Главные паттерны сегмента e-commerce РФ

1. **Каталог ≠ контент.** Все 5 сайтов — каталоги с ценами и карточками, но ни у одного нет answer-first блоков, FAQ или определений — AI-поиску нечего цитировать *дословно*.
2. **JSON-LD либо минимален, либо отсутствует.** 2 из 5 (citilink, detmir) — 0 блоков; market.yandex — только WebSite. Продуктовой схемы (Product/Offer) на главных нет ни у кого.
3. **llms.txt = 0/5 у крупных, 1/1 у среднего.** Только vkusvill имеет llms.txt; у market.yandex и holodilnik путь `/llms.txt` отдаёт SPA-страницу 404 (soft-404 — ломает сборщики).
4. **Защита от ботов съедает AI-доступ.** Ozon (307-loop), Megamarket/Lamoda/Sber (403-JS-spinner), DNS-shop (401) — топ-игроки недоступны даже обычному curl с браузерным UA; их защита блокирует и AI-краулеры.
5. **Wildberries повторно подтверждён как JS-shell (1 132 B)** — тот же результат, что в цикле 16.09: детерминированная метрика, не флуктуация.

## Вердикт баттлтеста

- **Бенчмарк выполнен.** 5 сайтов одной отрасли оценены конкурентно за один прогон; сравнительная таблица по 5 foundational-направлениям + 6 intelligence-измерениям.
- **Модель различима на конкурентах:** vkusvill (68/C) vs citilink (34/F) — разрыв 34 пункта в одной отрасли интерпретируем через конкретные gaps (llms, schema, meta).
- **Новый вывод по рынку:** e-commerce РФ (45.6) отстаёт от среднего рынка (66.4) на ~21 пункт — сегмент с самым большим трафиком наименее готов к AI-поиску.
- **Ограничение:** 5 из 10 запланированных топ-доменов закрыты для curl; сценарий «сайт закрыт → альтернатива из той же отрасли» отработан и зафиксирован.

## Источники

- Live-замеры 17.09.2026: `curl -sL --max-time 25 -A "Mozilla/5.0..."` на главную, `/robots.txt`, `/llms.txt`
- JSON-LD извлечён регуляркой из HTML и провалидирован `json.loads` (валидные/битые блоки)
- Модель скоринга и 92 правила — из `SKILL.md` этого репо
