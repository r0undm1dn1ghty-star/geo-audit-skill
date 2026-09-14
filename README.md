# GEO-аудит: увидит ли ChatGPT твой сайт

Если ChatGPT, Perplexity и Gemini не цитируют твой сайт — ты теряешь клиентов. Этот скилл проверяет 92 правила и даёт score 0-100 за 10 минут.

![MIT License](https://img.shields.io/badge/license-MIT-blue) ![v1.3.0](https://img.shields.io/badge/version-1.3.0-green) ![92 rules](https://img.shields.io/badge/rules-92-orange)

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

Real audit reports of 5 sites shipped with this skill — see [`examples/`](./examples/):

- `geo-battle-report.html` — rendered battle report
- `geo-battle-results.json` — structured results

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
  "softwareVersion": "1.3.0",
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