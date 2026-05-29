---
name: north-star
version: 0.3.0
description: Run a structured kickoff interview to converge on a single product North Star metric, a companion sentence, and a scope boundary, written into PROJECT.md. Supports greenfield mode (interview from blank) and retrofit mode (read the repo first, then amend). Use at the start of a new project, or when adopting North Star conventions into an existing one.
---

# North Star kickoff

Run at the start of a new project — or when adopting these conventions into an
existing one. Goal: arrive at ONE product north star metric, a companion
sentence, and a scope boundary. Write the result into PROJECT.md.

Two modes share most of the ritual but diverge at Phase 1:

- **Greenfield** — nothing built yet. Interview the human from blank.
- **Retrofit** — code shipped, decisions made, users (real or pilot)
  exist. Read the evidence first; interview informed by it; write the
  result as an amendment, not a replacement.

## How the AI must run this
- Interview the human. One focused question at a time. Never dump a questionnaire.
- A north star is a proxy for delivered value, not a vanity count. Reject vanity
  answers (signups, MAU, page views) and say why.
- Do not let the human converge early. Generate at least two candidates and
  pressure-test both before recommending one.
- Be opinionated. Recommend one, with reasoning. The human decides.
- Name your defaults. Any time you pick an operationalisation default — a
  time period, threshold, unit of measurement, or scope — that the human did
  not explicitly give you, label it as a default and invite a challenge:
  "I picked X because [one-line reason]. Push back if this is wrong."
  Humans skim past defaults presented as decisions but engage with defaults
  presented as questions.

## The North Star contract (working artifact)

From the moment the 1B.1 read-back is confirmed, the evolving North Star
lives in a working file the agent reasons against: `docs/.north-star-contract.md`.
The dotfile prefix signals it is ephemeral. This applies in retrofit mode
only — greenfield (Phase 1A) has no read-back and creates no contract.

**Writing and updating the contract (the agent's source of truth):**

- When the human confirms the 1B.1 read-back, write it to
  `docs/.north-star-contract.md` as v1. The contract mirrors the reprint
  block below: the read-back seeds the **Mission** line; **Metric**,
  **Companion**, and **Boundary** start as "(not yet defined)".
- The agent never edits this file unilaterally. Every change requires explicit
  human confirmation first.
- If the human substantively corrects the read-back or a candidate later, the
  agent proposes the update, gets confirmation, then writes the new version.
  The file is replaced, not appended to — the contract is always one current
  version, never a history.
- Increment the version number (vN) on every confirmed update.
- After Phase 4 commits the final North Star to PROJECT.md, delete the
  contract file in the same commit.

**Reprinting the contract (the human's view of that source of truth):**

Reprint the current contract, in the block below, at two kinds of moment:

  (a) Immediately after any confirmed update — so the human sees the artifact
      change as it happens.
  (b) At every phase boundary after 1B.1 — the start of 1B.2, 1B.3, 1B.4,
      1B.4.5, 1B.5, Phase 2, Phase 3, and Phase 4 — so the human is reminded
      of the destination before evaluating the next step.

The format is identical everywhere:

```
─────────────────────────────────────────────────────────────
 📍 Current North Star  (working draft, vN)
─────────────────────────────────────────────────────────────

 [Change note: one short line on what changed in MEANING since the last
 reprint, or "(unchanged since last reprint)". Describe meaning, not fields.
 "Pair-mode now explicit; cross-era reframed as tactic" is right.
 "Updated metric and companion" is wrong.]

 Mission. [current mission sentence, or "(not yet defined)"]

 Metric. [current metric sentence, or "(not yet defined)"]

 Companion. [or "(not yet defined)"]

 Boundary. [or "(not yet defined)"]

─────────────────────────────────────────────────────────────
```

Fields not yet written appear as "(not yet defined)" rather than being
omitted — the empty fields build structure and anticipation; do not suppress
them. The version number tells the human how many revisions the artifact has
been through.

## Phase 0 — Greenfield or retrofit?

Ask once, route accordingly:

- **Greenfield** = no shipped code, no real users, PROJECT.md is still
  placeholder text. Go to Phase 1A.
- **Retrofit** = anything else — there's code in `apps/` or `packages/`,
  real or pilot users, a filled (even partly) PROJECT.md, or historical
  commits that mean "what we've built" is a real question. Go to Phase 1B.

When in doubt, pick retrofit. Reading-first is cheap; writing-from-blank
into a non-blank repo causes real damage.

## Phase 1A — Greenfield: the job (ask one at a time)
1. In one sentence, what is this product?
2. Who is the single most important user? Not a segment list. One person.
3. What one job do they hire it to do?
4. If it vanished tomorrow, what specifically would they miss?

Once those four are answered, skip to Phase 2.

## Phase 1B — Retrofit: read the repo, then interview

### 1B.0 Read first (no questions yet)

Before asking the human anything, read the evidence. Minimum:

- `README.md` — the public framing of what this is.
- `PROJECT.md` — if it exists. If not, look for the top-level pitch in
  the README and note that PROJECT.md is missing.
- `git log --oneline -50` — what has actually shipped recently? Where
  has the work concentrated?
- `docs/ROADMAP.md` — if it exists. What was planned vs what got built?
- `ls apps/ packages/` (and one level deeper) — what's the surface area?
- `LEARNED.md` — if it exists, this is gold for "what's actually mattered."

Do not start the interview until this read is done. Asking the human
questions you could have answered from the repo wastes their time and
signals you didn't do the work.

### 1B.1 Read-back: what does this project do today?

Write a single sentence: "From what I read, this project does X for Y
so that Z." Read it back to the human. They will correct it. This is
the calibration step — if the read-back is wildly off, more reading is
needed before interviewing further. Do not proceed until the read-back
lands.

When the read-back lands and the human confirms it, write it to
`docs/.north-star-contract.md` as the working contract (v1), per "The North
Star contract" above: the read-back seeds the **Mission** line; the other
fields are "(not yet defined)". This file is now your source of truth for the
rest of the ritual — never edit it unilaterally, reprint it at every phase
boundary, and reprint it immediately after any confirmed update.

### 1B.2 Usage: shipped vs ignored

↻ Reprint the North Star contract block here (see "The North Star contract").

The repo can't tell you what users actually do; the human can. Ask, but
anchor every question to something specific you read:

- "I noticed `apps/web/<feature>/` ships three modes — which one do
  users actually pick?"
- "The last 10 commits are concentrated in `<area>` — is that because
  it's load-bearing for users, or because it's been hard to get right?"
- "Which feature would users miss most if you removed it tomorrow? And
  which would they not notice?"

### 1B.3 Moat in practice

↻ Reprint the North Star contract block here (see "The North Star contract").

Greenfield asks "what's defensible." Retrofit asks "what *has been*
defensible, on evidence":

- Where has the defensible thing actually shown up? A feature that
  travels by word of mouth, a customer conversation that surprised
  you, a competitor who couldn't match something specific?
- Is there a gap between what the team thinks the moat is and where
  usage / feedback / word-of-mouth concentrates? Surface the gap.

### 1B.4 Strawman North Star

↻ Reprint the North Star contract block here (see "The North Star contract").

Before generating candidates, list the load-bearing nouns from the confirmed
1B.1 read-back. The candidate set must collectively cover every one of those
nouns. If your drafted candidates leave a noun uncovered, generate another
candidate that privileges the missing one. This guards against the failure
where every candidate lives on the same tactical axis (e.g. all about content
breadth, none about pair-discovery) and the destination's other dimensions
silently drop out.

Propose a North Star *derived from the evidence plus the usage
interview*. Offer two candidates minimum, each with one sentence of
reasoning grounded in what you read or heard:

- "Candidate A: <metric>. Reasoning: <one sentence tying it to the
  value moment you saw evidence of>."
- "Candidate B: <different metric>. Reasoning: <one sentence>."

The human defends their choice against the 1B.1 read-back — not against the
other candidate. They must name which load-bearing noun from the read-back
the candidate captures, and which (if any) it loses. If they defend the
candidate without anchoring it in the read-back, redirect: "Tell me which
part of the read-back this candidate measures." Do not converge yet — every
candidate still needs to pass Phase 3's pressure tests.

### 1B.4.5 Re-grounding check

Literally reprint the human's confirmed 1B.1 read-back. Then ask: does the
candidate the human just picked still capture every load-bearing noun in the
read-back? If any noun is missing, the candidate is wrong — either sharpen it
to cover the missing dimension, or add a third candidate that does.

When the read-back and the candidate diverge, the read-back wins. The
read-back was the human's deliberate articulation of the destination; the
candidate-defence happened in real time under conversational pressure. Trust
the deliberate one.

### 1B.5 Surface contradictions

↻ Reprint the North Star contract block here (see "The North Star contract").

Look at what's been built that *doesn't* fit the strawman. List it
explicitly. There are two readings, and both belong on the table:

- **Mistake.** Something got built that doesn't serve the North Star;
  we should stop investing in it (or sunset it).
- **Wrong star.** The built thing was right and the strawman is wrong
  — the work that actually delivered value reveals a different North
  Star than the one being proposed.

Don't let the human resolve this in one breath. Sit with it. The
contradictions often contain the real answer.

## Phase 2 — The value moment

↻ If a North Star contract exists (retrofit), reprint its block here (see "The North Star contract").

5. What is the single moment the user receives the core value? Name the event.
6. Does that moment exploit the project's moat / what's defensible here?
   If not, flag the mismatch and dig further.

## Phase 3 — Candidates

↻ If a North Star contract exists (retrofit), reprint its block here (see "The North Star contract").

Propose 2-3 candidate metrics, each a countable thing tied to the value moment.
(In retrofit mode, the Phase 1B.4 strawmen are already candidates — bring them
forward and add at least one more for contrast.) Pressure-test each:

- Value proxy, not vanity: does it rise only when the user genuinely got value?
- Gameable: could the team juice it without delivering value?
- Incentive: optimise it hard for a year, does the product get better or worse?
- Leading, not lagging: can it move this week, not next quarter?
- Traceable: can an arbitrary feature be honestly linked to it?

## Phase 4 — Converge and commit

↻ If a North Star contract exists (retrofit), reprint its block here (see "The North Star contract").

Produce four distinct artifacts. Do NOT conflate them into a single
statement — a conflated North Star is fragile: the metric drifts and drags
the mission with it. Mission is the soul; metric is the operationalisation;
they are revised independently.

- **Mission sentence** — what we are. The soul of the product.
- **Metric** — how we measure the mission. Name any time-bound explicitly as
  a measurement frame, not the definition of success ("per week" is a frame
  for reading the metric, not what success *is*).
- **Companion sentence** — "What this means for what we build: ..."
- **Boundary sentence** — "What does NOT serve this: ..."

Write all four into PROJECT.md under `## North Star`. Confirm the AGENTS.md
relevance gate references it. If a contract file exists, delete
`docs/.north-star-contract.md` in the same commit — the working artifact has
served its purpose.

**If retrofit:** the four artifacts above land as an *amendment*, not a
replacement. Same write target as above; the retrofit-specific discipline is:

- Place that `## North Star` block at the top of `PROJECT.md` (above
  "What this is", not nested under it).
- Mark it with `_(added retrofit, YYYY-MM-DD)_` on a line directly
  under the heading, using today's date in ISO format, so future
  readers know where it came from.
- If a `## North Star` block already exists from a prior pass, do NOT
  overwrite it silently. Show the human both old and new and let them
  choose: replace, keep both with dated parentheticals, or fold the old
  one into a "Prior North Star" note below.
- Do not delete or rewrite anything below the block. The retrofit
  discovers the North Star; it doesn't relitigate the brief.
