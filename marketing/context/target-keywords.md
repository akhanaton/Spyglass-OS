# Target Keywords

Last updated: 2026-05-16

## How this file works

This is the living keyword register for ExamPilot's SEO content programme. Update it after every `/research-keywords` run and every time an article is published. The `/write-article`, `/seo-audit`, and `/research-gaps` skills all reference this file.

Keyword difficulty (KD) estimates are sourced from DataForSEO. Many entries below are still estimates based on topic difficulty signals and competitor domain authority — refresh them with real data via:

```bash
python3 marketing/data_sources/modules/keyword_volume.py --file <keywords.txt> --kd
```

Pull worldwide first (default), then a core-market cut (`--location pakistan` etc.) where geo matters. Promote a keyword to a higher tier if real KD comes in below the estimate.

---

## Tier 1: Priority (KD ≤20 — publish in Month 1-2)

Low-competition, high-specificity keywords. Paper code + topic combinations that larger sites don't bother targeting because the volumes look small, but the intent is extremely high.

| Keyword | Intent | Est. KD | Exam Board | Status | Article URL |
|---------|--------|---------|------------|--------|-------------|
| cambridge 9709 pure 1 integration questions | transactional/practice | 12 | Cambridge (9709) | planned | — |
| 9709 paper 1 past paper worked solutions | informational | 14 | Cambridge (9709) | planned | — |
| cambridge 9709 differentiation rules | informational | 11 | Cambridge (9709) | planned | — |
| cambridge 9709 binomial expansion questions | informational/practice | 13 | Cambridge (9709) | planned | — |
| cambridge 9709 statistics past papers | informational | 15 | Cambridge (9709) | planned | — |
| WMA11 past papers with worked solutions | informational | 10 | Edexcel IAL | planned | — |
| edexcel ial pure 1 integration | informational | 12 | Edexcel IAL | planned | — |
| 9709 pure 1 coordinate geometry questions | informational/practice | 13 | Cambridge (9709) | planned | — |
| cambridge 9709 trigonometry exam questions | informational/practice | 14 | Cambridge (9709) | planned | — |
| WMA12 pure 2 revision | informational | 11 | Edexcel IAL | planned | — |

---

## Tier 2: Core (KD 20-35 — publish in Month 2-3)

Moderate competition, higher volume. Mostly informational intent. These build topical authority and generate the majority of organic traffic as content matures.

| Keyword | Intent | Est. KD | Exam Board | Status | Article URL |
|---------|--------|---------|------------|--------|-------------|
| cambridge 9709 revision tips | informational | 22 | Cambridge (9709) | planned | — |
| how to revise for cambridge a level maths | informational | 24 | Cambridge (9709) | planned | — |
| 9709 paper 3 revision plan | informational | 20 | Cambridge (9709) | planned | — |
| a level maths spaced repetition | informational | 18 | Generic | planned | — |
| cambridge 9709 grade boundaries 2024 | informational/seasonal | 25 | Cambridge (9709) | planned | — |
| edexcel ial maths revision strategy | informational | 23 | Edexcel IAL | planned | — |
| savemyexams vs past papers | informational/commercial | 28 | Generic | planned | — |
| how many past papers for cambridge 9709 | informational | 21 | Cambridge (9709) | planned | — |
| 9709 statistics probability questions | informational/practice | 26 | Cambridge (9709) | planned | — |
| cambridge a level maths knowledge gaps | informational | 22 | Cambridge (9709) | planned | — |

---

## Tier 3: Competitive (KD 35+ — build towards in Month 3+)

High competition, high volume. These are dominated by SaveMyExams, PapaCambridge, and Physics & Maths Tutor. Targeting them requires strong topical authority built from Tier 1 and Tier 2 content first.

| Keyword | Intent | Est. KD | Exam Board | Status | Article URL |
|---------|--------|---------|------------|--------|-------------|
| cambridge a level maths revision | informational | 42 | Cambridge (9709) | planned | — |
| a level maths past papers | informational | 55 | Generic | planned | — |
| cambridge 9709 past papers | informational | 48 | Cambridge (9709) | planned | — |
| best a level maths revision app | commercial/transactional | 38 | Generic | planned | — |
| savemyexams alternative | commercial | 35 | Generic | planned | — |
| a level maths revision notes | informational | 52 | Generic | planned | — |
| edexcel ial past papers | informational | 44 | Edexcel IAL | planned | — |
| cambridge international a level maths | informational | 47 | Cambridge (9709) | planned | — |

---

## Pillar Keywords (long-term topical authority)

Hub pages that anchor pillar/spoke clusters. Each pillar article links out to 8-12 spoke articles.

| Keyword | Cluster | Status | Article URL |
|---------|---------|--------|-------------|
| cambridge 9709 pure mathematics 1 | Pure 1 cluster | planned | — |
| cambridge 9709 pure mathematics 3 | Pure 3 cluster | planned | — |
| cambridge 9709 statistics | Statistics cluster | planned | — |
| cambridge 9709 mechanics | Mechanics cluster | planned | — |
| edexcel ial pure mathematics wma11 | Edexcel Pure 1 cluster | planned | — |
| edexcel ial pure mathematics wma12 | Edexcel Pure 2 cluster | planned | — |
| a level maths revision strategy | Strategy/methodology cluster | planned | — |

---

## Keyword Status Legend

- `planned` — in topics pipeline, not yet written
- `in-progress` — being written (article exists in drafts/)
- `published` — live with URL (add URL to table)
- `ranking` — appearing in top 10 (add position in parentheses: `ranking (P4)`)
- `excluded` — see Excluded Keywords section below

---

## Recently Published (track for 90-day ranking trajectory)

Update this table weekly by checking GSC data. Articles rank within 2-8 weeks of publishing for low-KD targets; 8-16 weeks for mid-KD.

| Keyword | Published Date | Current Position | 30-day Trend | 90-day Target |
|---------|---------------|-----------------|--------------|---------------|
| — | — | — | — | — |

*No articles published yet. Update this table after first publish.*

---

## Seasonal Keyword Windows

Keywords with time-sensitive search spikes. Plan content 6-8 weeks before the window opens.

| Keyword | Peak window | Est. KD | Priority |
|---------|-------------|---------|----------|
| cambridge 9709 grade boundaries [year] | Aug (results day) | 25 | High |
| 9709 resit preparation | Sep-Oct | 20 | High |
| cambridge maths mock exam preparation | Dec-Jan | 18 | Medium |
| a level maths exam technique tips | Apr-May | 28 | High |
| edexcel ial results 2026 grade boundaries | Aug | 22 | High |

---

## Excluded Keywords

Keywords reviewed and explicitly rejected. Kept here to avoid revisiting.

| Keyword | Rejected reason | Date |
|---------|----------------|------|
| a level maths tutor | Implies we're a tutoring service — against positioning | 2026-05-16 |
| online maths tutoring | Same as above | 2026-05-16 |
| gcse maths revision | Wrong audience (GCSE, not A-Level) | 2026-05-16 |
| maths homework help | Wrong intent (homework vs exam prep) | 2026-05-16 |

---

## Maintenance protocol

- Update `Status` column every time an article moves through the pipeline (planned → in-progress → published → ranking)
- Add the live URL to the `Article URL` column when published
- Add new keywords discovered by `/research-keywords` or `/research-gaps` to the appropriate tier
- Move keywords from Tier 2/3 to Tier 1 if DataForSEO data shows lower actual KD than estimated
- Run a quarterly audit to remove or move stale keywords (planned for 3+ months with no action)
