# GEO Audit Skill — English summary

**GEO-SEO Audit Skill** by Victor Zaitsev / Discovery System — the most comprehensive open-source AEO + GEO audit methodology for AI search visibility.

## What it does

Audits any website for **AI-engine discoverability** — how likely ChatGPT, Perplexity, Claude, Google AI Overviews, Gemini, Grok, and Copilot are to **find, parse, quote, and cite** your content.

## Key features

- **92 Linter Rules** across 4 categories (GEO-specific, SEO foundation, content quality, i18n)
- **6 Intelligence Dimensions** (Answer Readiness, Quotability, Evidence Density, Content Depth, Freshness, Structural Clarity) with 0-5 rubric
- **7 AI Search Engine Spec Sheets** — per-platform citation mechanics, crawler names, optimization priorities
- **22 Research-Backed Data Points** with primary sources (Aggarwal KDD 2024, Ahrefs, SE Ranking, Kevin Indig, AirOps, Authoritas, BrandCited)
- **A-F Grading** — letter grade on top of numeric score (50% foundational + 50% intelligence)
- **Framework-Specific Fix Patterns** — Next.js, Astro, WordPress, SvelteKit, Plain HTML
- **9 AI Crawler Access** — ready-to-use robots.txt template
- **Execution Flow v3** — 8-step pipeline from bot access check to longitudinal tracking

## Рыночный прогон (16.09.2026)

5 RU sites scored live: skyeng.ru 81/B+, oldboybarbershop.com 64/C+, tbank.ru 58/C, wildberries.ru 42/D (JS-shell), discovery-system.ru 87/A-. Average 66.4. See [`examples/geo-battle-2026-09-16.md`](../../examples/geo-battle-2026-09-16.md).

## Scoring model

```
Final Score = 50% Foundational (92 rules) + 50% Intelligence (6 dimensions)
→ Grade: A+ (95-100) · A (90-94) · B+ (80-84) · ... · F (<40)
```

## Quick start

1. Download the repo
2. Copy `SKILL.md` into Claude Code / Hermes
3. Run: `audit <your-site>`
4. Get score 0-100 + action plan

Russian is authoritative — this is a summary. Full methodology: [`SKILL.md`](../../SKILL.md).

## License

MIT — free to use, modify, distribute. Attribution appreciated.

## Author

**Victor Zaitsev** — Discovery System
- Telegram: [@discoverysystem](https://t.me/discoverysystem)
- GitHub: [r0undm1dn1ghty-star](https://github.com/r0undm1dn1ghty-star)
