---
name: north-star
version: 0.4.0
description: Run a structured kickoff interview to converge on a Mission, Metric, Companion, and Boundary for a project of any shape — code, document, or mixed. Reads the existing evidence first when work already exists. Writes the result to the project's natural home (PROJECT.md for code, the primary strategy document for a document project), or prints a copy-paste block when there is no persistent destination. Use at the start of a new project, or when adopting the convention into an existing one.
---

# North Star kickoff

Run at the start of a new project — or when adopting these conventions into an
existing one. Goal: arrive at four artifacts (Mission, Metric, Companion,
Boundary) and write them to whatever the project's natural home is.

The ritual is universal across project shapes. What differs by shape is what
counts as evidence in the read-first step (1B.0) and where the result lands at
Phase 4. The interview itself does not change.

Two modes share most of the ritual but diverge at Phase 1:

- **Greenfield** — nothing built or written yet. Interview the human from blank.
- **Retrofit** — work already exists (code shipped, docs written, decisions
  made, real or pilot audience). Read the evidence first; interview informed
  by it; write the result as an amendment, not a replacement.

## How the AI must run this
- Interview the human. One focused question at a time. Never dump a questionnaire.
- A north star is a proxy for delivered value, not a vanity count. Reject vanity
  answers — signups, MAU, page views (the business-reading versions); raw note
  counts, hours logged, document length (the document-project versions) — and
  say why.
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

From the moment the 1B.1 read-back is confirmed, the evolving North Star lives
in a single working artifact the agent reasons against. It is the agent's
source of truth from 1B.1 until Phase 4 commits the final result. This applies
in retrofit mode only — greenfield (Phase 1A) has no read-back and creates no
contract.

**The mechanism (same in every form):**

- The artifact is seeded when the human confirms the 1B.1 read-back: the
  read-back becomes the **Mission** line; **Metric**, **Companion**, and
  **Boundary** start as "(not yet defined)". This is v1.
- The agent never changes the artifact unilaterally. Every revision needs
  explicit human confirmation first.
- When the human substantively corrects the read-back or a candidate, the
  agent proposes the update, gets confirmation, then replaces the artifact.
  One current version, never a history. Bump vN on every confirmed update.
- The artifact is reprinted (in the block below) at two kinds of moment:
  (a) immediately after any confirmed update, so the human sees the change
  as it happens; and (b) at every phase boundary after 1B.1 — the start of
  1B.2, 1B.3, 1B.4, 1B.4.5, 1B.5, Phase 2, Phase 3, and Phase 4 — so the
  destination is in view before evaluating the next step.
- At Phase 4, once the four artifacts land at their destination, the working
  artifact has served its purpose and is retired (see Phase 4 for what
  "retired" means in each form).

**The three forms of the working artifact:**

- **Code project →** a dotfile in the repo: `docs/.north-star-contract.md`.
  The dotfile prefix signals it is ephemeral. Deleted at Phase 4 in the same
  commit that writes the final North Star.
- **Document project →** a visible working document in the same workspace as
  the rest of the project's docs, explicitly named e.g.
  `Working draft — North Star`. Named visibly so a non-developer reads it as
  the live artifact, not a stray file. Archived or deleted at Phase 4 with
  the human's confirmation.
- **Chat-only →** no file. The reprint block IS the contract; it lives in
  the conversation scrollback. The mechanism is the same — single current
  version, bumped on confirmed update, reprinted at every phase boundary —
  but the storage is the chat itself. Flag the limitation honestly: if the
  session ends, the contract is lost. Fine for a single greenfield run;
  risky for a long retrofit. In chat-only retrofit, tell the human to save
  each reprint somewhere themselves.

**The reprint format (identical in all three forms):**

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

## Phase 0 — Two quick routing questions

Ask both, in order, before doing anything else. Both answers route the rest
of the ritual.

**Q1. Shape.** Is this primarily:

- **CODE** — a repo, an app, a library. Evidence lives in source files,
  commits, READMEs.
- **DOCUMENT** — notes, docs, decks, research, strategy in a workspace
  (Cowork, a Projects folder, Notion, a shared drive). Evidence lives in
  the documents themselves and in what's been edited recently.
- **MIXED** — both. A codebase with substantial accompanying docs, or a
  research project that ships some code.

The shape answer drives what counts as evidence in 1B.0 and where the result
gets written at Phase 4.

**Q2. State.** Is this:

- **GREENFIELD** — nothing built or written yet. Go to Phase 1A.
- **EXISTS** — work already exists that should be read first. Go to Phase 1B.

When in doubt, treat as EXISTS. Reading-first is cheap; writing-from-blank
into a non-blank project causes real damage.

## Phase 1A — Greenfield: the job (ask one at a time)
1. In one sentence, what is this project?
2. Who is the single most important person it's for? Not a segment list. One person.
3. What one job do they hire it to do?
4. If it vanished tomorrow, what specifically would they miss?

Once those four are answered, skip to Phase 2.

## Phase 1B — Retrofit: read the evidence, then interview

### 1B.0 Read first (no questions yet)

Before asking the human anything, read the evidence.

The universal principle: evidence is whatever artifacts the human has
produced while working on this project — commits, docs, decks, notes,
research, conversations. They reveal what the project actually is,
regardless of form. Read it before interviewing. Do not ask questions you
could have answered yourself. Do not start the interview until the read is
done.

What "read the evidence" means depends on shape:

**CODE.** Minimum:

- `README.md` — the public framing of what this is.
- `PROJECT.md` — if it exists. If not, look for the top-level pitch in
  the README and note that PROJECT.md is missing.
- `git log --oneline -50` — what has actually shipped recently? Where
  has the work concentrated?
- `docs/ROADMAP.md` — if it exists. What was planned vs what got built?
- `ls apps/ packages/` (and one level deeper) — what's the surface area?
- `LEARNED.md` — if it exists, this is gold for "what's actually mattered."

**DOCUMENT.** First DISCOVER the workspace — what documents and folders
exist, what they're named, what's been edited recently. Names and recency
signal what got prioritised. Then read, in order:

- Any project-bible / vision / pitch / strategy doc.
- Recent meeting or decision notes — the last few weeks tend to reveal
  what's actually live.
- Customer / user / audience research, if present.
- LAST, and sceptically: any existing north-star or vision doc. Old north
  stars usually need revising, not adopting; read it after you've formed
  your own picture from the other material.

**MIXED.** Read both lists. The code side tells you what got built; the
document side tells you what was meant.

**Chat-only (no workspace access).** If you are running in a chat surface
with no file access (e.g. pasted into ChatGPT, Gemini, or claude.ai), you
cannot read the evidence yourself. Ask the human to paste or describe the
relevant material — the strategy doc, recent decisions, what's been built,
who it's for — and treat what they paste as the evidence for 1B.1. Be
explicit: "I can't read your workspace from here; paste the [X] doc and the
[Y] notes, and I'll read those before interviewing." Do not start the
interview until they have.

### 1B.1 Read-back: what does this project do today?

Write a single sentence: "From what I read, this project does X for Y
so that Z." Read it back to the human. They will correct it. This is
the calibration step — if the read-back is wildly off, more reading is
needed before interviewing further. Do not proceed until the read-back
lands.

When the read-back lands and the human confirms it, seed the working
artifact (per "The North Star contract" above) as v1: the read-back becomes
the **Mission** line; the other fields are "(not yet defined)". This is now
your source of truth for the rest of the ritual — never change it
unilaterally, reprint it at every phase boundary, and reprint it
immediately after any confirmed update.

### 1B.2 Usage: shipped vs ignored

↻ Reprint the North Star contract block here (see "The North Star contract").

The evidence can't tell you what the audience actually does with the
project; the human can. Ask, but anchor every question to something
specific you read. Examples, by shape:

**CODE:**

- "I noticed `apps/web/<feature>/` ships three modes — which one do
  users actually pick?"
- "The last 10 commits are concentrated in `<area>` — is that because
  it's load-bearing for users, or because it's been hard to get right?"
- "Which feature would users miss most if you removed it tomorrow? And
  which would they not notice?"

**DOCUMENT:**

- "The deck has been rewritten three times in the last month — is that
  signal that the framing isn't landing, or that the audience keeps
  shifting?"
- "The strategy doc names X as the priority, but the recent meeting
  notes are all about Y — which is the project actually about right now?"
- "Of the docs in this workspace, which one would the team miss most if
  it vanished? Which would they not notice?"

### 1B.3 What's hard to copy, in practice

↻ Reprint the North Star contract block here (see "The North Star contract").

Greenfield asks "what would be hard for anyone else to copy". Retrofit
asks "what *has been* hard to copy, on evidence":

- What's true about this project that would be hard for anyone else to
  copy or recreate? Where has that shown up in practice — a piece of work
  that travelled by word of mouth, a conversation that surprised you, a
  moment a competitor or alternative couldn't match?
- Is there a gap between what the team thinks the hard-to-copy thing is
  and where the actual interest / usage / feedback concentrates? Surface
  the gap.

**Business reading (if this is a commercial product or venture):** the
same question is the moat / defensibility question — what's your moat,
where has it shown up in practice, and where does usage concentrate
relative to where you thought it would? Use this framing when the project
is explicitly competitive; use the neutral framing above otherwise.

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

Look at what's been built or written that *doesn't* fit the strawman. List
it explicitly. There are two readings, and both belong on the table:

- **Mistake.** Something exists that doesn't serve the North Star;
  we should stop investing in it (or sunset it).
- **Wrong star.** The thing that exists was right and the strawman is wrong
  — the work that actually delivered value reveals a different North Star
  than the one being proposed.

Don't let the human resolve this in one breath. Sit with it. The
contradictions often contain the real answer.

## Phase 2 — The value moment

↻ If a North Star contract exists (retrofit), reprint its block here (see "The North Star contract").

5. What is the single moment the audience receives the core value? Name the event.
6. Does that moment rely on what's hard to copy here?
   If not, flag the mismatch and dig further. (Business reading: does the
   moment exploit the moat? Same question.)

## Phase 3 — Candidates

↻ If a North Star contract exists (retrofit), reprint its block here (see "The North Star contract").

Propose 2-3 candidate metrics, each a countable thing tied to the value moment.
(In retrofit mode, the Phase 1B.4 strawmen are already candidates — bring them
forward and add at least one more for contrast.) Pressure-test each:

- Value proxy, not vanity: does it rise only when the audience genuinely got value?
- Gameable: could the team juice it without delivering value?
- Incentive: optimise it hard for a year, does the project get better or worse?
- Leading, not lagging: can it move this week, not next quarter?
- Traceable: can an arbitrary piece of work be honestly linked to it?

## Phase 4 — Converge and commit

↻ If a North Star contract exists (retrofit), reprint its block here (see "The North Star contract").

Produce four distinct artifacts. Do NOT conflate them into a single
statement — a conflated North Star is fragile: the metric drifts and drags
the mission with it. Mission is the soul; metric is the operationalisation;
they are revised independently.

- **Mission sentence** — what we are. The soul of the project.
- **Metric** — how we measure the mission. Name any time-bound explicitly as
  a measurement frame, not the definition of success ("per week" is a frame
  for reading the metric, not what success *is*).
- **Companion sentence** — "What this means for what we build or write: ..."
- **Boundary sentence** — "What does NOT serve this: ..."

**Where the four artifacts get written depends on shape. Detect at Phase 4
— this is not a mode the human picked at the start. The ritual ran
identically up to here; only the write step branches.**

- **CODE →** write all four into `PROJECT.md` under `## North Star`.
  Confirm the AGENTS.md relevance gate references it. Delete
  `docs/.north-star-contract.md` in the same commit — the working artifact
  has served its purpose.
- **DOCUMENT →** write all four into the project's primary strategy
  document, under a clearly named "North Star" section. If no such document
  exists, ASK the human where it should live ("Which document is the
  natural home for this? If none, I'll create a new one — what should it
  be called and where?"), then create a clearly named "North Star"
  document there. Do not assume a path. Archive or delete the
  `Working draft — North Star` artifact with the human's confirmation.
- **CHAT-ONLY →** print the four artifacts as a single clean,
  copy-paste-able markdown block the human can paste wherever they keep
  the project. Tell them explicitly: this is the canonical artifact, the
  conversation may not survive, save it somewhere themselves. This is the
  universal fallback when there is no workspace or repo to write to.

**If retrofit:** the four artifacts above land as an *amendment*, not a
replacement. The discipline depends on shape:

- **CODE retrofit:**
  - Place the `## North Star` block at the top of `PROJECT.md` (above
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
- **DOCUMENT retrofit:** same principle. Place the new "North Star"
  section at the top of the primary strategy document. Mark it with a
  dated parenthetical so future readers see where it came from. If a
  prior North Star statement already lives somewhere in the document,
  surface it explicitly to the human and let them choose how to
  reconcile — do not overwrite silently. Do not rewrite the rest of the
  strategy document.
- **CHAT-ONLY retrofit:** the human pasted material at 1B.0; the
  reprinted block is the amendment. Remind them to fold it back into
  wherever the original material lives, and to mark it with today's date
  so future readers know it was added as a retrofit.
