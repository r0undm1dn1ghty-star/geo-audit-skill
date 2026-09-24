# Changelog

## v1.7.0 — 2026-09-20 (межсегментный рыночный прогон + факт-чек)

- Межсегментный рыночный прогон: банки / медиа / B2B-сервисы РФ (16 URL, 11 скоренных, 3 «не наблюдали»). Средние: медиа 64.2 (C+), банки 63.3 (C), B2B 61.0 (C). Лидеры: bitrix24.ru 76/B, kommersant.ru 72/B−, psbank.ru 71/B−. `examples/competition-2026-09-20.md`
- **Межсегментная шкала интерпретации** в SKILL.md: сравнение readiness по сегментам, правила чтения (внутрисегментный разброс > межсегментного; «не наблюдали» искажает средние; готовность не коррелирует с размером)
- **Факт-чек Research-Data Table по первоисточникам**: каждая цифра получила статус (потолок/среднее/конфликт/нет методологии). Princeton GEO +41%/+33% — потолок на отзывчивом подмножестве, не среднее; SE Ranking «3x для 2000+ слов» конфликтует с Ahrefs Dec 2025 (53,4% цитат со страниц <1000 слов) → вывод «плотность > длины»; AirOps 3.2x headings — неподтверждено (Ahrefs Q1 2026: 1.2–1.4x); AirOps FAQ +156% — без методологии. Добавлены подтверждённые цифры Ahrefs Q1 2026: 78,4% цитат из заголовков-вопросов (G02), плотность имён собственных 20,6% vs 5–8% (G03), 53% цитат из середины абзацев
- **G01 уточнён**: answer-first = ответ в первых 30% документа; внутри абзаца ответ не обязан быть первым предложением
- **Новые паттерны сегментов** (в README): половина банков невидима без JS; JSON-LD без `@id` у всех банков; llms.txt soft-404 (200 + HTML-заглушка); TLS на RU-корневом УЦ как слой невидимости; FAQ-контент без FAQPage-схемы
- Adversarial Self-Check присутствует во всех трёх сегментных отчётах цикла
- Ре-база на v1.6.1: все 7 epistemic-правок v1.6.1 (readiness proxy, SSR-формулировки, статус-колонка Market Context, Adversarial Self-Check в Output Format) сохранены и объединены с факт-чеком v1.7.0

## v1.6.1 — 2026-09-20 (fix: SKILL.md content of v1.6.0)

- **Фикс доставки:** правки v1.6.0 в SKILL.md не попали в коммит cdac61b (запись ушла в README из-за бага скрипта). Коммит содержал только version bump. В v1.6.1 все 7 epistemic-правок реально в SKILL.md: readiness proxy в таблице rating, SSR-формулировка с отсылкой к спецификациям ботов, статус-колонка Market Context, пометки в Research-Data Table, обязательный Adversarial Self-Check в Output Format.
- README v1.6.0 был корректен — не менялся.

## v1.6.0 — 2026-09-19 (adversarial cycle)

- Epistemic-правки по официальным источникам (Google AI features docs, Anthropic/OpenAI/Perplexity crawler docs): абсолютное «AI-краулеры не исполняют JS» заменено на проверяемую формулировку с отсылкой к спецификациям ботов
- Score явно помечен как **readiness proxy** — техническая готовность, не вероятность цитирования (таблица rating переписана)
- Market Context: все 10 цифр помечены статусом (оценка/прогноз/вендорская метрика), слабые строки Research-Data Table помечены
- Добавлен обязательный раздел **Adversarial Self-Check** в формат отчёта: что curl не увидел, что score не утверждает, какое наблюдение изменило бы вывод
- README hero переформулирован: «не видят → не процитируют» вместо «не цитируют → теряешь клиентов»

## v1.5.0 — 2026-09-17

- Конкурентный рыночный прогон e-commerce РФ: 5 сайтов одной отрасли (vkusvill.ru 68/C, market.yandex.ru 52/F, detmir.ru 51/F, citilink.ru 34/F, holodilnik.ru 23/F). Средний score 45.6 (F) — сегмент отстаёт от среднего рынка на ~21 пункт
- `examples/competition-ecommerce-2026-09-17.md` — сравнительная таблица конкурентов, intelligence по каждому сайту, 5 паттернов сегмента, лидер сегмента (vkusvill.ru)
- Сценарий «сайт закрыт → альтернатива из той же отрасли» отработан: ozon.ru (307-loop), megamarket.ru/lamoda.ru (403), dns-shop.ru (401) зафиксированы как закрытые; wildberries.ru повторно подтверждён JS-shell (1 132 B)

## v1.4.0 — 2026-09-16

- рыночный прогон на 5 сайтах РФ: skyeng.ru 81/B+, oldboybarbershop.com 64/C+, tbank.ru 58/C, wildberries.ru 42/D, discovery-system.ru 87/A−. Средний score 66.4 (C+)
- `examples/geo-battle-2026-09-16.md` — метод, таблица результатов, измерения intelligence по каждому сайту, 4 валидных паттерна рынка РФ
- README: таблица рыночного прогона заменена на новый прогон (предыдущие артефакты сохранены)

## v1.3.0 — 2026-09-10

- 7 AI search engine spec sheets: ChatGPT, Perplexity, Claude, Google AI Overviews, Gemini, Grok, Copilot — citation mechanics, crawler names, optimization priorities
- 22 research-backed data points with primary sources (Aggarwal KDD 2024, Ahrefs, SE Ranking, Kevin Indig, AirOps, Authoritas, BrandCited)
- A-F grading on top of numeric score (50% foundational + 50% intelligence)
- Examples: 5 real sites audited (`examples/geo-battle-report.html`)

## v1.0.0 — 2026-09-09

- Initial release
- 92 linter rules across 4 categories (GEO-specific, SEO foundation, content quality, i18n)
- 6 intelligence dimensions with 0-5 rubric (Answer Readiness, Quotability, Evidence Density, Content Depth, Freshness, Structural Clarity)
- Framework-specific fix patterns (Next.js, Astro, WordPress, SvelteKit, Plain HTML)
- 9 AI crawler access — ready-to-use robots.txt template
- Execution Flow v3 — 8-step pipeline from bot access check to longitudinal tracking
