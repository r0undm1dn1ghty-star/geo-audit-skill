# Changelog

## v1.4.0 — 2026-09-16

- Баттлтест на 5 сайтах РФ: skyeng.ru 81/B+, oldboybarbershop.com 64/C+, tbank.ru 58/C, wildberries.ru 42/D, discovery-system.ru 87/A−. Средний score 66.4 (C+)
- `examples/geo-battle-2026-09-16.md` — метод, таблица результатов, измерения intelligence по каждому сайту, 4 валидных паттерна рынка РФ
- README: таблица баттлтеста заменена на новый прогон (предыдущие артефакты сохранены)

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