---
name: cluster
description: Builds a pillar/spoke topic cluster for one exam topic area. Creates the architecture for topical authority, with a 3-phase execution plan.
---

## Input

$ARGUMENTS

Expect: a topic area to build a cluster around. Examples:
- "Cambridge 9709 Integration"
- "Edexcel WMA11 Statistics"
- "Cambridge 9709 Pure 3 complete"
- "A Level Maths differentiation techniques"

If not provided, ask: "Which topic area should I build a cluster for? (e.g. 'Cambridge 9709 Integration', 'Edexcel WMA11')"

## Execution

### Step 1: Read SEO strategy and existing coverage

Read `marketing/references/seo-strategies.md` for hub-and-spoke architecture guidelines and internal linking rules.

Fetch the wiki SEO strategy for URL architecture and KD targets:
```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/seo/seo-strategy.md --jq '.content' | base64 -d
```

```bash
ls marketing/pipelines/published/
ls marketing/pipelines/topics/
```

Read frontmatter from each file to map current keyword coverage. Note which spokes may already exist.

### Step 2: Classify the topic area

Based on the input, determine:
- **Exam board:** Cambridge 9709 | Edexcel IAL | Both
- **Paper/module:** P1/P3/S1/S2/M1 (Cambridge) or WMA11/WMA12/WST01/WME01 (Edexcel)
- **Topic breadth:** Broad (full module) → use pillar + 10-12 spokes | Narrow (single technique) → use mini-cluster with pillar + 4-6 spokes
- **Funnel alignment:** Most cluster content is TOFU. Product/comparison spokes are MOFU.

### Step 3: Define the pillar article

The pillar is a comprehensive guide covering the full topic area at a high level, with internal links to all spokes.

Pillar spec:
```
Keyword: "[exam board] [topic] complete guide" or "[topic] [paper code] revision"
Target: KD 25-35 (competitive but achievable)
Word count: 3000-5000 words
Format: Comprehensive guide with H2 sections linking out to each spoke
URL: /blog/[exam-board]-[topic-slug]-complete-guide
SERP target: Featured snippet (People Also Ask) + AI Overview
GEO priority: High — answer-first, Key Takeaways, 4+ FAQ
Status: [published | planned | gap — check existing coverage]
```

### Step 4: Design 8-12 spoke articles

For the given topic, generate spoke articles covering each sub-topic or technique.

Use the exam board syllabus structure to ensure complete coverage. Each spoke:
- Targets a specific technique, concept, or application
- Links to the pillar article as its "parent"
- Can also link laterally to adjacent spokes

For each spoke, specify:
```
Spoke [N]:
  Keyword: "[technique/topic] [paper code] a level"
  Estimated KD: [≤25 for spokes — lower = higher priority]
  Content type: technique guide | worked example walkthrough | common mistakes | comparison
  Word count: 1500-2500 words
  URL: /blog/[technique-slug]-[paper-code]
  Internal link to pillar: anchor text "[pillar topic] revision"
  Lateral links: [adjacent spokes if any]
  Status: published | planned | gap
  Priority: [1 = highest — lowest KD + highest intent + exam-calendar aligned]
```

**Topic-specific spoke templates:**

For integration topics (Cambridge 9709 P1/P3):
- Integration by substitution
- Integration by parts
- Definite integrals and area under curve
- Volumes of revolution
- Numerical integration
- Reduction formulas (P3)
- Differential equations (P3)

For differentiation topics:
- Rules of differentiation (product, quotient, chain)
- Implicit differentiation
- Parametric differentiation
- Applications: tangents, normals, stationary points
- Second derivatives and curve sketching
- Connected rates of change

For statistics topics (S1/WST01):
- Probability rules and Venn diagrams
- Binomial distribution
- Normal distribution and standardisation
- Hypothesis testing basics
- Correlation and regression

For mechanics topics (M1/WME01):
- Kinematics equations and graphs
- Newton's laws application
- Forces in equilibrium
- Energy, work, and power
- Momentum and impulse

For algebra/pure topics:
- Partial fractions
- Logarithms and exponentials
- Trigonometric identities
- Vectors (2D and 3D)
- Complex numbers (P3)
- Sequences and series

### Step 5: Map internal linking

Build the internal link map:

```
Pillar → links to ALL spokes (one link per spoke, descriptive anchor)
Each spoke → links back to pillar (anchor: "[Topic] complete guide")
Adjacent spokes → link laterally where logically connected:
  e.g. "integration by parts" ↔ "integration by substitution"
  e.g. "normal distribution" ↔ "hypothesis testing"
```

Show as a visual map:
```
[Pillar: Topic Complete Guide]
  ├── → Spoke 1: [keyword] — anchor: "[technique] for 9709"
  ├── → Spoke 2: [keyword] — anchor: "[technique] a level"
  ├── → Spoke 3: [keyword] — anchor: "[technique] cambridge"
  ... etc
[Spoke 1] ←→ [Spoke 2] (lateral link if related)
```

### Step 6: Prioritize spoke execution sequence

Rank spokes using:
1. Status = gap (must be gap, not already published/planned)
2. KD estimate (lowest first)
3. Student intent (technique how-to > general revision > background theory)
4. Exam calendar alignment (topics in active exam window first)

Label each spoke: P1 (highest), P2, P3 in execution order.

### Step 7: 3-phase execution plan

**Phase 1 — Foundation (Week 1-2):**
- Write pillar article (establishes cluster authority)
- Write top 2 spoke articles (P1 and P2 priority)
- Set up internal links between all three

**Phase 2 — Expansion (Week 3-6):**
- Write spokes P3-P7
- Add lateral links between published spokes
- Update pillar with new internal links as spokes publish

**Phase 3 — Complete coverage (Month 2-3):**
- Write remaining spokes
- Add comparison/product angle spoke (MOFU)
- Submit cluster for GSC indexing check

### Step 8: Save cluster plan

Save to `marketing/pipelines/research/cluster-[topic-slug]-YYYY-MM-DD.md`

```yaml
---
type: topic-cluster
topic: ""
exam_board: cambridge-9709 | edexcel-ial | both
paper_module: ""
pillar_keyword: ""
pillar_status: published | planned | gap
spokes_total: 0
spokes_published: 0
spokes_planned: 0
spokes_gap: 0
cluster_completion: "0%"
created: YYYY-MM-DD
---

## Topic Cluster: [Topic Name]

### Pillar Article
[Pillar spec]

### Spoke Articles
[All spokes with priority, KD, status]

### Internal Link Map
[Visual map]

### Phase Execution Plan
[3 phases]

### Recommended first actions
1. `/write-article "[pillar keyword]"` — write the pillar
2. `/research-serp "[spoke 1 keyword]"` — validate spoke 1
3. `/write-article "[spoke 1 keyword]"` — write spoke 1
```

### Step 9: Offer next step

Show cluster summary (pillar + top 3 spokes) and ask:
- "Cluster built for [topic]. [X] spokes, [Y]% coverage from current content."
- "Phase 1 plan: pillar + [spoke 1] + [spoke 2]. Want to start with `/write-article '[pillar keyword]'`?"
- "Or run `/research-keywords` on each spoke first to build out briefs?"
