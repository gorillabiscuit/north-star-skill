# Worked example — abbreviated retrofit run

A condensed transcript of a CODE-shape retrofit run, showing what correct
behaviour looks like at each step. Elisions are marked `[…]`. This is a
reference for the agent running the ritual: read it when unsure how a step
should *feel* in practice — how opinionated to be, when to reprint, what a
read-back sounds like. It is not a script to copy verbatim.

The example project: "Plot", a small self-hosted tool a solo developer
built for tracking vegetable-garden beds, plantings, and harvests.

---

**Agent:** Running north-star v0.5.0.

Two quick routing questions before anything else.

Is this primarily a CODE project (repo, app, library), a DOCUMENT project
(notes, decks, strategy in a workspace), or MIXED?

**Human:** Code.

**Agent:** And is it GREENFIELD (nothing built yet) or does work already
EXIST that I should read first?

**Human:** It exists — been building it for about six months.

**Agent:** Retrofit, then. I'll read the evidence before asking you
anything.

*[Agent reads README.md, PROJECT.md (absent — noted), `git log --oneline
-50`, ls of the app structure, LEARNED.md]*

**Agent:** Read done. Here's my read-back — correct me:

From what I read, Plot tracks garden beds, plantings, and harvest yields
for a home gardener so that next season's planting decisions are based on
what actually grew, not memory.

**Human:** Close. It's not just "what grew" — half the value is the
timing. When I planted, when I harvested. Knowing carrots from bed 3 took
11 weeks here, not the 9 the packet says.

**Agent:** Revised read-back: Plot records what was planted where and
when, and what came out and when, so that a home gardener's next-season
decisions — what, where, and *when* to plant — are based on their own
garden's real history rather than seed-packet averages or memory.

**Human:** That's it.

**Agent:** Confirmed. Seeding the contract as v1.

```
─────────────────────────────────────────────────────────────
 📍 Current North Star  (working draft, v1)
─────────────────────────────────────────────────────────────

 [Change note: seeded from the confirmed read-back.]

 Mission. Plot records what was planted where and when, and what
 came out and when, so next-season decisions are based on this
 garden's real history rather than packet averages or memory.

 Metric. (not yet defined)

 Companion. (not yet defined)

 Boundary. (not yet defined)

─────────────────────────────────────────────────────────────
```

I'm writing this to `docs/.north-star-contract.md` — it's the working
draft I'll reason against until Phase 4 commits the real thing.

*[1B.2 usage questions, anchored to evidence — e.g. "The last 15 commits
are all in the photo-upload feature; is that load-bearing for you or has
it just been hard to get right?" Human reveals photos are barely used but
the planting-date views get opened constantly. 1B.3 hard-to-copy: the
accumulated multi-season timing data for THIS garden's soil and light —
no seed database can replicate it. Contract updated to v2 along the way
when the human sharpens "real history" to "multi-season history";
reprinted immediately.]*

**Agent (1B.4):** Load-bearing nouns from the read-back: *planted
(what/where/when)*, *harvested (what/when)*, *next-season decisions*,
*this garden's multi-season history*. Candidates must cover all of them.

- Candidate A: **planting decisions made from a Plot record** — count of
  times a new planting's what/where/when was chosen while viewing prior
  seasons' data. Reasoning: it's the exact value moment your usage
  answers pointed at, and it covers *decisions* + *history*.
- Candidate B: **complete plant-to-harvest records per season** — a
  planting with both its dates logged. Reasoning: covers
  *planted*/*harvested*, and the record IS the hard-to-copy asset.

My recommendation is A — B measures the asset accumulating, but the
mission's payoff noun is *decisions*, and B can grow while nobody ever
consults it. Push back if this is wrong.

**Human:** A feels right. B is just data entry.

**Agent (1B.4.5 re-grounding):** Before we lock anything, here's your
confirmed read-back again, verbatim: *"Plot records what was planted where
and when, and what came out and when, so that next-season decisions are
based on this garden's multi-season history rather than packet averages
or memory."* Does Candidate A capture every load-bearing noun? Checking
myself: it captures *decisions* and *history*… but nothing in A requires
the *harvest* side to be recorded — you could make planting decisions
from planting dates alone and A still counts it. Is harvest data
load-bearing, or a nice-to-have?

**Human:** Load-bearing. The whole point is knowing what the yield
actually was.

**Agent:** Then A sharpens to: **planting decisions made while consulting
a prior season's complete plant-to-harvest record.** […]

*[Phase 2 confirms the value moment — the winter-planning session where
next season gets decided. Phase 3 pressure-tests: gameable? traceable?
leading? A third contrast candidate is added and rejected. Phase 4
converges.]*

**Agent (Phase 4):** Four artifacts, landing as a dated retrofit
amendment at the top of `PROJECT.md`:

- **Mission.** Plot turns one garden's real multi-season history into
  next season's planting decisions.
- **Metric.** Planting decisions made while consulting a prior season's
  complete plant-to-harvest record. (Per-season is the measurement frame,
  not the definition of success — push back if wrong.)
- **Companion.** What this means for what we build: anything that gets a
  complete record consulted at decision time — capture friction, recall
  views, season comparison.
- **Boundary.** What does NOT serve this: features for sharing, browsing
  other people's gardens, or plant encyclopedias — Plot is about *this*
  garden's history, not gardening content.

Committing this to `PROJECT.md` under `## North Star` marked
`_(added retrofit, 2026-07-05)_`, and deleting
`docs/.north-star-contract.md` in the same commit — the working draft has
served its purpose.

---

## What this example is demonstrating

- The version announcement is the literal first line.
- Phase 0's two routing questions come before any reading or interviewing.
- The read-back is corrected by the human, and the *corrected* version
  seeds the contract — then the contract is reprinted immediately and at
  every phase boundary (elided here after the first).
- 1B.2 questions are anchored to something specifically read ("the last
  15 commits are all in photo-upload"), not generic.
- Candidates are defended against the read-back's load-bearing nouns, and
  1B.4.5 catches a noun (*harvest*) the chosen candidate silently
  dropped — that catch is the step's entire purpose.
- The agent recommends one candidate with reasoning and names its
  defaults ("per-season is the measurement frame") as challengeable.
- Phase 4 produces four separate artifacts, lands them as a dated
  amendment, and retires the working contract in the same commit.
