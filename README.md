# north-star

A standalone skill that runs the **North Star kickoff** ritual: a structured
interview that converges on four artifacts — a Mission sentence, a Metric, a
Companion sentence ("what this means for what we build or write"), and a
Boundary ("what does NOT serve this") — for a project of any shape (code,
document, or mixed).

A North Star is a proxy for delivered value, not a vanity count. The ritual is
opinionated by design: it interviews you one question at a time, rejects vanity
answers (signups, MAU, page views for businesses; raw note counts, hours
logged, document length for document projects), generates at least two
candidates, and pressure-tests them before recommending one. You decide.

The ritual lives in [`SKILL.md`](./SKILL.md). The interview logic is universal
across project shapes; what differs is what counts as evidence in the
read-first step and where the result gets written.

## Two questions at the start

Phase 0 routes the rest of the ritual with two sequential questions:

- **Shape.** Is this a **CODE** project (repo, app, library), a **DOCUMENT**
  project (notes, docs, decks, research in a workspace like Cowork, a Projects
  folder, Notion), or **MIXED**? Shape drives what gets read and where the
  result lands.
- **State.** **GREENFIELD** (nothing built or written yet) or **EXISTS** (work
  already exists that should be read first)? State drives whether the agent
  interviews from blank (Phase 1A) or reads the evidence first and amends
  (Phase 1B).

When in doubt, treat as EXISTS — reading first is cheap; writing-from-blank
into a non-blank project causes real damage.

## Where the result goes

Phase 4 detects the destination — it's not a mode the human picks at the start.
The four artifacts are universal; only the write step branches:

- **Code project →** written into `PROJECT.md` under `## North Star`. In a repo
  that uses an `AGENTS.md` relevance gate, that block is what every non-trivial
  task is expected to trace back to.
- **Document project →** written into the project's primary strategy document,
  under a clearly named "North Star" section. If no such document exists, the
  agent asks where it should live rather than assuming a path.
- **Chat-only (no workspace) →** printed as a single clean, copy-paste-able
  markdown block. This is the universal fallback when there is nowhere to
  write to.

## Install / use matrix

| Surface | How to run it |
|---|---|
| Claude Code (recommended) | install as a plugin via the [gorillabiscuit marketplace](https://github.com/gorillabiscuit/claude-plugins) (below) — auto-updates, no manual `git pull` |
| Claude Code (manual) | clone into `~/.claude/skills/north-star` (below) — you own the update step |
| claude.ai | upload the skill as a zip (below) |
| Pi | symlink into `~/.pi/agent/prompts` (below) |
| Cowork | planned — a Cowork plugin wrapper |
| Any chat (ChatGPT, Gemini, claude.ai web, etc.) | paste the universal prompt from [Use it anywhere](#use-it-anywhere-no-installation) |

### Claude Code — plugin (recommended)

Installed this way, updates land automatically the next time Claude Code
starts — no manual `git pull`, no risk of silently running a stale version.

```
/plugin marketplace add gorillabiscuit/claude-plugins
/plugin install north-star@gorillabiscuit
```

Then in any project:

```
/north-star:north-star
```

(Claude Code namespaces plugin-provided skills as `<plugin>:<skill>`. Both
the plugin and the skill inside it are named `north-star`, hence the
doubled segment.)

To check for updates manually: `/plugin marketplace update gorillabiscuit`.

### Claude Code — manual clone

If you'd rather not add a marketplace, clone this repo directly into your
user skills directory:

```bash
git clone https://github.com/gorillabiscuit/north-star-skill.git ~/.claude/skills/north-star
```

Then in any project, invoke it with:

```
/north-star
```

**This path does not auto-update.** Nothing pulls new commits for you — you
own that step. To update: `git -C ~/.claude/skills/north-star pull`. If you
forget, you keep silently running whatever commit you cloned, however old.
This is the exact failure mode the plugin path above exists to close — if
that risk doesn't bother you, this route works fine; if it does, use the
plugin instead.

### claude.ai

Zip the skill folder and upload it via the skills UI:

```bash
cd ~/Code/north-star-skill
zip -r north-star.zip SKILL.md
```

Then upload `north-star.zip` in claude.ai's skill settings.

### Pi

Symlink `SKILL.md` into Pi's prompts directory so it's available as a prompt
template:

```bash
ln -s ~/Code/north-star-skill/SKILL.md ~/.pi/agent/prompts/north-star.md
```

### Cowork

Cowork plugin support is **planned but not yet built**. For now, use one of
the other surfaces above, or paste the universal prompt below into any chat
the team uses.

## Use it anywhere (no installation)

You can run the ritual in any AI chat (ChatGPT, Gemini, claude.ai web, etc.)
by pasting the block below as your first message. The agent will run the
ritual one-shot from there.

**Chat-only limitation.** In a chat surface there is no persistent contract
file. The reprint block IS the contract; it lives in the conversation. If
the surface has a memory feature (Claude's memory, ChatGPT's memory), the
agent will offer to keep a backup copy of the contract there as the ritual
progresses — with your consent. Where no such feature exists, the session
scrollback is all there is: if the session ends, the contract is lost —
fine for a single greenfield run, risky for a long retrofit. Either way,
save the final reprinted block somewhere you own; a memory copy supplements
that, it doesn't replace it.

The block below is the canonical body of [`SKILL.md`](./SKILL.md) with the
YAML frontmatter stripped. Do not edit it here — edit `SKILL.md` and
regenerate (see [Regenerating this block](#regenerating-this-block)).

~~~markdown
<!-- BEGIN: generated from SKILL.md — do not edit by hand -->

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
- Announce the version first. Your very first line is exactly:
  `Running north-star v0.5.0.` — then continue into Phase 0. This one line
  is how the human catches a stale install: if they know a newer release
  exists and the announced version is older, they update before investing
  in a full ritual run. (Maintainers: this literal and the frontmatter
  `version:` above are the two places the version lives — bump both in the
  same commit, per CHANGELOG discipline.)
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
- If unsure how any step should feel in practice — how opinionated to be,
  what a read-back sounds like, when exactly to reprint — read
  `docs/example-run.md` (an abbreviated worked retrofit run) before
  proceeding. Read it on demand, not by default; it exists to calibrate
  behaviour, not to be copied verbatim. (Chat-only surfaces without file
  access: skip this — the ritual text above is self-sufficient.)

## The North Star contract (working artifact)

From the moment the read-back is confirmed, the evolving North Star lives
in a single working artifact the agent reasons against. It is the agent's
source of truth from that confirmation until Phase 4 commits the final
result. Both modes have a read-back and both create a contract: retrofit's
comes from the evidence (1B.1); greenfield's comes from the human's four
Phase 1A answers (1A.5). The interview is a multi-step ritual in either
mode, and the human loses track of the evolving state in either mode — the
contract is the fix, so neither mode goes without it.

**The mechanism (same in every form):**

- The artifact is seeded when the human confirms the read-back (1B.1 in
  retrofit, 1A.5 in greenfield): the read-back becomes the **Mission**
  line; **Metric**, **Companion**, and **Boundary** start as
  "(not yet defined)". This is v1.
- The agent never changes the artifact unilaterally. Every revision needs
  explicit human confirmation first.
- When the human substantively corrects the read-back or a candidate, the
  agent proposes the update, gets confirmation, then replaces the artifact.
  One current version, never a history. Bump vN on every confirmed update.
- The artifact is reprinted (in the block below) at two kinds of moment:
  (a) immediately after any confirmed update, so the human sees the change
  as it happens; and (b) at every phase boundary after the seeding
  read-back — in retrofit, the start of 1B.2, 1B.3, 1B.4, 1B.4.5, 1B.5,
  Phase 2, Phase 3, and Phase 4; in greenfield, the start of Phase 2,
  Phase 3, and Phase 4 — so the destination is in view before evaluating
  the next step.
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
  but the storage is the chat itself.

  **Before shrugging at data loss, check what persistence you actually
  have.** Many chat surfaces now carry a memory feature (Claude's memory,
  ChatGPT's memory, project-level notes). If yours does, offer it: "I can
  save the current contract to my memory so it survives this session —
  want me to keep it updated there as we go?" With consent, write the
  contract there on every confirmed update, and note in the reprint that a
  memory copy exists. Memory is a backup for continuity, not the canonical
  home — Phase 4 still ends with the human saving the final block
  somewhere they own.

  Only when the surface genuinely has no persistence, flag the limitation
  honestly: if the session ends, the contract is lost. Fine for a single
  greenfield run; risky for a long retrofit. In that case tell the human
  to save each reprint somewhere themselves.

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

### 1A.5 Read-back and seed the contract

Distil the four answers into a single sentence: "So: this project does X
for Y so that Z." Read it back to the human and let them correct it. When
it lands, seed the working artifact (per "The North Star contract" above)
as v1: the confirmed sentence becomes the **Mission** line; the other
fields are "(not yet defined)". From here the contract rules apply exactly
as in retrofit — never change it unilaterally, reprint at every phase
boundary and immediately after any confirmed update.

Then go to Phase 2.

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

↻ Reprint the North Star contract block here (see "The North Star contract"). Both modes have one by now.

5. What is the single moment the audience receives the core value? Name the event.
6. Does that moment rely on what's hard to copy here?
   If not, flag the mismatch and dig further. (Business reading: does the
   moment exploit the moat? Same question.)

## Phase 3 — Candidates

↻ Reprint the North Star contract block here (see "The North Star contract"). Both modes have one by now.

Propose 2-3 candidate metrics, each a countable thing tied to the value moment.
(In retrofit mode, the Phase 1B.4 strawmen are already candidates — bring them
forward and add at least one more for contrast.) Pressure-test each:

- Value proxy, not vanity: does it rise only when the audience genuinely got value?
- Gameable: could the team juice it without delivering value?
- Incentive: optimise it hard for a year, does the project get better or worse?
- Leading, not lagging: can it move this week, not next quarter?
- Traceable: can an arbitrary piece of work be honestly linked to it?

## Phase 4 — Converge and commit

↻ Reprint the North Star contract block here (see "The North Star contract"). Both modes have one by now.

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
  conversation may not survive, save it somewhere themselves. If the
  surface has a memory feature and the human consented to memory copies
  during the ritual, also save the final four artifacts there — and say
  you did — but this supplements the human's own copy, it does not
  replace the instruction to save one. This is the universal fallback
  when there is no workspace or repo to write to.

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
<!-- END: generated from SKILL.md -->
~~~

### Regenerating this block

`SKILL.md` is the canonical source. The block above is its body with the
YAML frontmatter stripped, wrapped in a `~~~markdown` fence so its inner
fenced code blocks render correctly. To regenerate after editing the skill:

```bash
awk 'p; /^---$/ && ++n==2 {p=1}' SKILL.md
```

Pipe the output through your clipboard (`| pbcopy` on macOS), then paste it
into the README between the `<!-- BEGIN -->` and `<!-- END -->` markers,
replacing whatever was there. Do not edit the README copy by hand — it will
drift from `SKILL.md` and the discipline is what makes the skill work.

## License

MIT — see [LICENSE](./LICENSE).
