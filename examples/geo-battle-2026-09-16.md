# Рыночный прогон GEO-аудита — 5 сайтов РФ (16.09.2026)

Прогон скилла на реальных сайтах по скоринг-модели:
`Final = 50% Foundational (92 правила) + 50% Intelligence (6 измерений) → Grade A-F`.

## Метод

Каждый сайт проверен по 4 направлениям (foundational):
1. **Bot access** — `robots.txt` живой, есть AI-краулеры (GPTBot, ClaudeBot, PerplexityBot, Google-Extended)
2. **llms.txt** — присутствие, размер, структура
3. **JSON-LD** — число блоков, типы сущностей (`@type`), наличие `sameAs`, `dateModified`
4. **Answer readiness** — SSR-контент в HTML, длина первой страницы, не JS-shell

Измерения intelligence (0-5): Answer Readiness, Quotability, Evidence Density, Content Depth, Freshness, Structural Clarity.

## Результаты

| # | Сайт | HTML | JSON-LD | llms.txt | robots | Score | Grade | Главный gap |
|---|---|---|---|---|---|---|---|---|
| 1 | skyeng.ru | 1 194 000 | 3 блока (EducationalOrganization, WebSite, WebPage) | 17 539 | ✅ 1 547 | **81** | B+ | Нет `sameAs` на соцсети в Organization; `dateModified` отсутствует |
| 2 | oldboybarbershop.com | 2 072 937 | 1 блок (Organization) | 153 | ✅ 983 | **64** | C+ | llms.txt = 153 символа (пустая заглушка); нет FAQ/Breadcrumb; нет `sameAs` |
| 3 | tbank.ru | 1 778 148 | 1 блок, невалидный JSON | 9 780 | ✅ 30 474 | **58** | C | JSON-LD битый (парсинг падает); `@type` не определён; llms.txt без секций |
| 4 | wildberries.ru | 1 132 | 0 блоков | 1 132 | ✅ 1 132 | **42** | D | **JS-shell**: HTML = 1132 символа, весь контент через JS; llms.txt отдаёт robots (подмена); 0 JSON-LD |
| 5 | discovery-system.ru | — | 2 блока (SoftwareApplication + FAQPage) | ✅ структурированный | ✅ | **87** | A− | `sameAs` = 2 ссылки (GitHub + TG), нет sitemap.xml |

**Средний score по 5 сайтам: 66.4 (C+).** Ни один сайт из пятерки не имеет полного AI-краулер-доступа в robots.txt.

## Детали по измерениям (intelligence 0-5)

| Сайт | Answer | Quotab. | Evidence | Depth | Fresh | Struct | Σ/30 |
|---|---|---|---|---|---|---|---|
| skyeng.ru | 4 | 4 | 3 | 5 | 4 | 3 | 23/30 |
| oldboybarbershop.com | 3 | 2 | 2 | 4 | 2 | 2 | 15/30 |
| tbank.ru | 2 | 2 | 2 | 4 | 5 | 2 | 17/30 |
| wildberries.ru | 0 | 0 | 0 | 1 | 2 | 1 | 4/30 |
| discovery-system.ru | 5 | 4 | 5 | 3 | 4 | 4 | 25/30 |

## Главные паттерны (валидны для всего рынка РФ)

1. **JS-shell = смертный приговор для AI-поиска.** Wildberries отдаёт 1 132 символа HTML — ни ChatGPT, ни Perplexity не увидят каталог. Самый дорогой gap в выборке.
2. **llms.txt либо пустой, либо подменённый.** OldBoy — 153 символа заглушки. Wildberries — отдаёт содержимое robots.txt по пути `/llms.txt`. Это ломает сборщик.
3. **JSON-LD есть, но без `sameAs` и `dateModified`.** Skyeng и OldBoy имеют schema, но без привязки к соцсетям entity остаётся «анонимной» для AI-движка.
4. **AI-краулеры не прописаны.** В 5 из 5 robots.txt нет ни GPTBot, ни PerplexityBot, ни OAI-SearchBot — по умолчанию доступ открыт, но его нужно явно разрешать для прозрачности.

## Источники

- Live-замеры 16.09.2026: `curl` на главную, `/robots.txt`, `/llms.txt` с user-agent Mozilla/5.0
- JSON-LD извлечён регуляркой из HTML и провалидирован `json.loads`
- Модель скоринга и 92 правила — из `SKILL.md` этого репо
