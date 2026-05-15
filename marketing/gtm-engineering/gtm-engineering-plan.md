# GTM Engineering: Implementation Plan

**Owner:** Enitan  
**Created:** 2026-05-15  
**Status:** Phase 0 — active

---

## What GTM Engineering is

GTM Engineering is Enitan's function within Spyglass OS. It sits parallel to Teresa's Marketing Machine (content, community execution). Where the Marketing Machine creates and distributes content, GTM Engineering captures intent signals, scores them, and routes them to action.

The signal architecture is adapted from B2B intent-signal patterns for a B2C edtech context: no CRM deals, no SDR sequences, no firmographic data. Instead: student behavioral signals, community demand signals, and SEO intelligence signals.

**The activation chain:**
```
PostHog (behavioral) ──┐
Reddit Monitor (community) ──┤──→ signal_processor.py ──→ scored report
GSC / DataForSEO (SEO) ──┤                                    │
Calendar (exam dates) ──┘                          ┌──────────┴──────────┐
                                                   ↓                     ↓
                                         Coda Signals table        Attio CRM contact
                                         (operational view)        (enriched profile)
                                                                         │
                                                                         ↓
                                                               Brevo sequence (manual now,
                                                               auto Phase 1)
```

---

## Files in this function

| File | Purpose |
|---|---|
| `signal-registry.md` | All signals — source, category, weight |
| `scoring-model.md` | Scoring logic, tier definitions, threshold triggers |
| `trigger-playbook.md` | If→then rules per signal threshold |
| `../data_sources/modules/signal_processor.py` | Python module: aggregate, score, output |
| `../../.claude/commands/signal-review.md` | `/signal-review` command |

---

## Phase-gate roadmap

| Phase | Condition | Automation level |
|---|---|---|
| **Phase 0 (now)** | Pre-launch, low data volume | `/signal-review` command, manual action, weekly cadence |
| **Phase 1** | Post-Brevo + Attio API connected | signal_processor → Attio auto-enrich; Attio → Brevo sequence triggers |
| **Phase 2** | 8-12 weeks post-launch data | Empirical weight adjustment based on signal-to-conversion correlation |

---

## Attio CRM fields per contact

- Email / PostHog User ID
- Exam board (Cambridge 9709 / Edexcel IAL)
- Acquisition source (Reddit / Organic / Tutor referral)
- Current tier (Hot / Warm / Cold / Churning)
- Signal score (rolling, updated each `/signal-review` run)
- Last active date
- Topic focus (from PostHog session data)
- Brevo sequence status (Enrolled / Completed / None)

Attio enrichment is manual in Phase 0: `signal_processor.py` outputs a contact update report; Enitan applies it.

---

## Coda Signals table columns

- Signal ID (auto)
- Source (PostHog / Reddit / GSC / DataForSEO / Calendar)
- Type (Behavioral / Community / SEO / Campaign)
- User or Entity ID
- Score / Weight
- Tier (Hot / Warm / Cold / Churning / SEO / Demand)
- Recommended Action
- Status (Pending / Actioned / Dismissed)
- Date logged
