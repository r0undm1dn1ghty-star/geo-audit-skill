# GEO-аудит: увидит ли ChatGPT твой сайт

Если ChatGPT, Perplexity и Gemini не видят твой сайт — они его не процитируют. Этот скилл проверяет 92 правила технической готовности и даёт score 0-100 за 10 минут. Score — это readiness proxy, а не вероятность цитирования.

![MIT License](https://img.shields.io/badge/license-MIT-blue) ![v1.7.0](https://img.shields.io/badge/version-1.7.0-green) ![92 rules](https://img.shields.io/badge/rules-92-orange)

## Quick Start

1. Скачай репо
2. Скопируй `SKILL.md` в Claude Code / Hermes
3. Запусти: `аудит <твой-сайт>`
4. Получи score 0-100 + action plan

> Бесплатный аудит → [t.me/discoverysystem](https://t.me/discoverysystem)

---

## GEO-Audit Skill — AEO + GEO for AI Search (2026)

> **GEO-SEO Audit Skill** by Victor Zaitsev / Discovery System
>
> The most comprehensive open-source AEO + GEO audit methodology for AI search visibility — 92 linter rules, 6 intelligence dimensions, 7 AI search engine spec sheets, 22 research-backed data points, framework-specific fix patterns, and a full execution pipeline.

## What this does

Audits any website for **AI-engine discoverability** — how likely ChatGPT, Perplexity, Claude, Google AI Overviews, Gemini, Grok, and Copilot are to **find, parse, quote, and cite** your content.

## Key features

- **92 Linter Rules** across 4 categories (GEO-specific, SEO foundation, content quality, i18n)
- **6 Intelligence Dimensions** (Answer Readiness, Quotability, Evidence Density, Content Depth, Freshness, Structural Clarity) with 0-5 rubric
- **7 AI Search Engine Spec Sheets** — per-platform citation mechanics, crawler names, and optimization priorities
- **22 Research-Backed Data Points** with primary sources (Aggarwal KDD 2024, Ahrefs, SE Ranking, Kevin Indig, AirOps, Authoritas, BrandCited)
- **A-F Grading** — letter grade on top of numeric score (50% foundational + 50% intelligence)
- **Framework-Specific Fix Patterns** — Next.js, Astro, WordPress, SvelteKit, Plain HTML
- **9 AI Crawler Access** — ready-to-use robots.txt template
- **Execution Flow v3** — 8-step pipeline from bot access check to longitudinal tracking

## Scoring model

```
Final Score = 50% Foundational (92 rules) + 50% Intelligence (6 dimensions)
→ Grade: A+ (95-100) · A (90-94) · B+ (80-84) · ... · F (<40)
```

## Examples

Real audit reports shipped with this skill — see [`examples/`](./examples/):

- [`competition-2026-09-20.md`](./examples/competition-2026-09-20.md) — межсегментный Рыночный прогон 20.09.2026: банки vs медиа vs B2B-сервисы, 16 URL, межсегментная шкала, Adversarial Self-Check
- [`competition-ecommerce-2026-09-17.md`](./examples/competition-ecommerce-2026-09-17.md) — конкурентный рыночный прогон e-commerce РФ 17.09.2026: 5 конкурентов одной отрасли, таблица лидеров, паттерны сегмента
- [`geo-battle-2026-09-16.md`](./examples/geo-battle-2026-09-16.md) — Рыночный прогон 5 сайтов РФ 16.09.2026: метод, таблица scores, 4 паттерна рынка
- [`adversarial-2026-09-19.md`](./examples/adversarial-2026-09-19.md) — adversarial-прогон 19.09.2026: 5 сложных входов (статический минимум, энциклопедия, JS-schema, бот-защита, redirect-loop) — проверка, что скилл говорит «не наблюдали» вместо score
- `geo-battle-report.html` — rendered battle report (предыдущий прогон)
- `geo-battle-results.json` — structured results (предыдущий прогон)

## Research references

| Claim | Source |
|---|---|
| Quotations = +41% visibility | Aggarwal et al., GEO paper, KDD 2024 |
| Statistics = +33% citation | Aggarwal et al., KDD 2024 |
| 44.2% ChatGPT citations from first 30% | Kevin Indig, Growth Memo 2026 |
| Comparison tables = 2.8x citations | AirOps, 2025 |
| 76% top-cited pages updated within 30 days | Ahrefs, 2025 (17M citations) |
| Perplexity citation rate = 97% | AuthorityTech, 2026 |
| ChatGPT citation rate = 16% | ThatDevPro, 2026 |

## Changelog

See [CHANGELOG.md](./CHANGELOG.md).

## Конкурентный рыночный прогон e-commerce (17.09.2026)

**5 e-commerce РФ одной отрасли, сравнительный прогон по модели `50% foundational + 50% intelligence`:**

| Сайт | HTML (B) | JSON-LD | llms | robots | Score | Grade | Главный gap |
|---|---|---|---|---|---|---|---|
| vkusvill.ru | 421 351 | 2 (Organization/GroceryStore, WebSite, OfferCatalog) | ✅ 5 365 | ✅ +sitemap | **68** | C | нет FAQ/answer-блоков и дат |
| market.yandex.ru | 2 057 102 | 1 (WebSite) | 404 | ✅ +sitemap | **52** | F | 0 heading'ов H1-H6, нет meta/OG |
| detmir.ru | 2 250 068 | 0 | 404 | ✅ без sitemap | **51** | F | 0 JSON-LD, sitemap не прописан |
| citilink.ru | 1 011 427 | 0 | 404 | ✅ +sitemap | **34** | F | 0 JSON-LD, нет H1, 812 слов текста |
| holodilnik.ru | 565 569 | 1 (Organization) | 404 | ✅ +sitemap | **23** | F | 189 слов видимого текста, битый title |

**Средний score сегмента: 45.6 (F)** — e-commerce РФ отстаёт от среднего рынка (66.4) на ~21 пункт. **Лидер сегмента — vkusvill.ru**: единственный с валидным llms.txt и полным мета-набором; побеждает структура, а не трафик.

Закрытые для curl (зафиксировано): ozon.ru (307-loop), wildberries.ru (498 JS-shell), megamarket.ru / lamoda.ru (403), dns-shop.ru (401) — защита от ботов блокирует и AI-краулеров. Полный отчёт: [`examples/competition-ecommerce-2026-09-17.md`](./examples/competition-ecommerce-2026-09-17.md)

**Бесплатный аудит вашего сайта →** [t.me/discoverysystem](https://t.me/discoverysystem) · [discovery-system.ru](https://discovery-system.ru)

## License

MIT — free to use, modify, distribute. Attribution appreciated.

## Author

**Victor Zaitsev** — Discovery System
- Telegram: [@discoverysystem](https://t.me/discoverysystem)
- GitHub: [r0undm1dn1ghty-star](https://github.com/r0undm1dn1ghty-star)

<!-- JSON-LD: structured data for AI crawlers -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "GEO Audit Skill",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Cross-platform",
  "softwareVersion": "1.7.0",
  "description": "GEO-аудит для AI-поиска: 92 правила, score 0-100, 7 AI-движков. Проверяет, увидит ли ChatGPT, Perplexity и Gemini твой сайт.",
  "license": "https://opensource.org/license/mit",
  "author": {
    "@type": "Person",
    "name": "Victor Zaitsev",
    "url": "https://t.me/discoverysystem",
    "sameAs": [
      "https://github.com/r0undm1dn1ghty-star",
      "https://t.me/discoverysystem"
    ]
  }
}
</script>

## Проверка на реальных рыночных данных

Скилл прогнан на реальных данных рынка — не на синтетике. Полный разбор с
цифрами, покрытием и воспроизводимыми командами: **[EVAL.md](EVAL.md)**.

Бенчмарк против наивного метода на реальных данных: **[BENCHMARK.md](BENCHMARK.md)**.
