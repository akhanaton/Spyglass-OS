---
name: research-topics
description: Topic clustering for topical authority. Groups related keywords into pillar/spoke clusters mapped to ExamPilot's exam board structure.
---

## Input

$ARGUMENTS

Optional: an exam board or topic area to focus on. Examples:
- "cambridge 9709 pure 1" — cluster only around P1 topics
- "edexcel ial" — cluster all Edexcel IAL modules
- (no input) — full cluster map across Cambridge 9709 and Edexcel IAL

## Execution

### Step 1: Read SEO strategy

Fetch the wiki SEO strategy for pillar/spoke architecture guidelines:

```bash
gh api repos/akhanaton/spyglass-wiki/contents/wiki/marketing/seo/seo-strategy.md --jq '.content' | base64 -d
```

Also read `marketing/references/seo-strategies.md` for local pillar/spoke guidance.

### Step 2: Map current coverage

```bash
ls marketing/pipelines/published/
ls marketing/pipelines/topics/
```

Read each published article and topic brief frontmatter to extract `keyword:` and `target-segment:` fields.

Build current coverage map:
- Published articles: [list of keywords]
- Planned (in topics/): [list of keywords]
- Combined coverage: [deduplicated list by topic cluster]

### Step 3: Build topic clusters

Map all keywords around ExamPilot's two exam board tracks.

**Track 1: Cambridge International AS & A Level Mathematics 9709**

Cluster A: Pure Mathematics 1 (Paper 1)
- Pillar: "Cambridge 9709 Pure 1 complete guide"
- Spokes: functions, quadratics, coordinate geometry, circular measure, trigonometry, sequences and series, differentiation, integration (definite + indefinite)

Cluster B: Pure Mathematics 3 (Paper 3)
- Pillar: "Cambridge 9709 Pure 3 complete guide"
- Spokes: algebra (partial fractions), logarithms and exponentials, trigonometry (compound angles, double angles), differentiation (implicit, parametric), integration (by parts, substitution), vectors, complex numbers, numerical methods, differential equations

Cluster C: Statistics 1 (Paper 5)
- Pillar: "Cambridge 9709 Statistics 1 revision guide"
- Spokes: data representation, measures of central tendency, probability, discrete random variables, binomial distribution, normal distribution

Cluster D: Statistics 2 (Paper 6) [if in scope]
- Pillar: "Cambridge 9709 Statistics 2 complete guide"
- Spokes: Poisson distribution, continuous random variables, sampling and estimation, hypothesis testing

Cluster E: Mechanics 1 (Paper 4)
- Pillar: "Cambridge 9709 Mechanics 1 revision guide"
- Spokes: forces in equilibrium, kinematics, Newton's laws, energy/work/power, momentum

**Track 2: Edexcel International Advanced Level Mathematics**

Cluster F: WMA11 Pure Mathematics 1
- Pillar: "Edexcel WMA11 complete revision guide"
- Spokes: algebra, coordinate geometry, calculus introduction, exponentials and logarithms

Cluster G: WMA12 Pure Mathematics 2
- Pillar: "Edexcel WMA12 complete revision guide"
- Spokes: proof, algebra (binomial), trigonometry, calculus (further differentiation, integration), parametric equations

Cluster H: WST01 Statistics 1
- Pillar: "Edexcel WST01 statistics revision guide"
- Spokes: sampling, data presentation, probability, discrete distributions, normal distribution, hypothesis testing

Cluster I: WME01 Mechanics 1
- Pillar: "Edexcel WME01 mechanics revision guide"
- Spokes: kinematics, dynamics, statics, momentum

**Track 3: Cross-board comparison and decision content**

Cluster J: Product/comparison cluster
- Pillar: "ExamPilot review and features"
- Spokes: "ExamPilot vs SaveMyExams", "ExamPilot vs PapaCambridge", "best revision tool for Cambridge 9709", "best maths revision app A Level"

### Step 4: Status each cluster

For each cluster, mark every spoke with one of:
- **Published** — article exists in `marketing/pipelines/published/`
- **Planned** — topic brief exists in `marketing/pipelines/topics/`
- **Gap** — not covered anywhere

Calculate cluster completion: [published + planned] / total spokes.

### Step 5: Identify priority spoke for each cluster

For each cluster, select the priority spoke to write next:
- Must be a Gap (not published or planned)
- Lowest estimated KD (paper-code specific > broad topic)
- Highest student intent (technique how-to > general revision)
- Exam-calendar aligned (prioritize topics tested in upcoming exam windows)

### Step 6: Recommend cluster to build out first

Rank clusters by:
1. Exam calendar urgency (active or upcoming season gets priority)
2. Completion gap (cluster with fewest published spokes gets priority)
3. SEO opportunity (cluster where competitors dominate less)
4. ExamPilot product alignment (topics where adaptive practice is most differentiated)

Output recommendation: "Build out Cluster [X] first. [Reason in 2 sentences]."

### Step 7: Visual cluster map

Output in this format for each cluster:

```
## Cluster [Letter]: [Cluster Name]
Completion: [X/Y spokes] ([%])
Priority spoke to write next: [keyword]

Pillar: [pillar keyword] → [status: published|planned|gap]
  ├── [spoke 1 keyword] → [status]
  ├── [spoke 2 keyword] → [status]
  ├── [spoke 3 keyword] → [status]
  ... (all spokes)
```

### Step 8: Save report

Save to `marketing/pipelines/research/topic-clusters-YYYY-MM-DD.md`

```yaml
---
type: topic-cluster-map
clusters_total: 0
clusters_with_pillar: 0
spokes_published: 0
spokes_planned: 0
spokes_gap: 0
priority_cluster: ""
analysis_date: YYYY-MM-DD
---

## Topic Cluster Map — [Date]

### Priority Cluster Recommendation
[Cluster name + reason]

### Cluster Overview
[Completion table: Cluster | Published | Planned | Gaps | % Complete]

### Cluster Detail Maps
[Full cluster maps]

### Priority Spokes to Write (Top 5 across all clusters)
[Ranked list with commands]
```

### Step 9: Prompt

Show cluster completion table and say: "Cluster [X] has [Y] gaps — highest priority based on [reason]. Top next spoke: '[keyword]'. Run `/research-keywords '[keyword]'` to build a brief, or `/write-article '[keyword]'` to start drafting?"
