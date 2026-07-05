# Changelog

All notable changes to this skill are documented here. This project follows
[Semantic Versioning](https://semver.org/).

## v0.8.0 — 2026-07-05

Adds a finalisation reveal: the moment a star is set — a fresh kickoff
or a revise-mode amendment — the ritual shows it once as a full ASCII
star scene (a five-pointed star, the Metric boxed at centre, Saturn
alongside). Establishes the display rule the skill had left implicit:
the plain bordered box is the star's normal display (the working draft
through the interview, a project's session-start reminder); the full
scene is reserved for finalisation so it stays a landmark, not
wallpaper.

- Phase 4.5: run the bundled renderer with the final Metric and show
  the scene; fall back to the plain box on any failure (no python3,
  metric too long, no renderer present) — the reveal is celebration,
  never a blocker.
- scripts/render-north-star-banner.py: the deterministic renderer
  (fixed seed). Saturn is the classic Horroroso piece, signature kept.
- The reprint-format section now states the plain-box-vs-reveal rule
  explicitly.

## v0.7.0 — 2026-07-05

Adds revise mode, demanded by a real documented failure (per the
Boundary's own rule for interview changes): on 2026-07-05 the maintainer
needed a small amendment to an existing star, the skill offered only the
full kickoff interview, and the run was abandoned mid-ritual as
burdensome.

- Phase 0 Q2 gains a third state, REVISE: a filled star exists and the
  goal is to change it, not create it. Routes to the new Phase 1C.
- Phase 1C — the short path: read the current star and what changed;
  print it and ask which fields are wrong and what happened in the world
  to make them wrong (a revision needs a nameable failure — wordsmithing
  without one is refused); propose new text for only the named fields;
  land as a dated amendment (`; revised YYYY-MM-DD`).
- Scaled discipline, not skipped discipline: a changed Metric still runs
  the Phase 3 pressure tests; a changed Mission still gets a read-back;
  Companion/Boundary changes must state their evidence.
- Escape hatch: three or more fields wrong, or a Mission that no longer
  describes the project, is a rethink — the agent must switch to the
  full retrofit rather than let the discount path bypass the ritual.
- Contract seeding for revise: all four fields start filled from the
  current star, instead of "(not yet defined)".

## v0.6.0 — 2026-07-05

Scope-cut release, executing the Boundary line of this repo's own North
Star (PROJECT.md, added 2026-07-05): surfaces outside Claude Code can
define a star but never enforce one, so the skill stops carrying them.
Removal only — no interview content changed.

- Removed the chat-paste distribution: the README's "Use it anywhere"
  universal prompt block (the generated SKILL.md mirror) and its
  regeneration instructions are gone. SKILL.md is once again the only
  copy of the ritual.
- Removed chat-only mode from the ritual itself: the chat-only working-
  artifact form (in-conversation reprint + memory backup), the 1B.0
  paste-the-evidence branch, and the Phase 4 / retrofit CHAT-ONLY
  destinations. The contract now has two forms (repo dotfile, visible
  working document) and Phase 4 two destinations (PROJECT.md, primary
  strategy document).
- Removed claude.ai zip upload and Pi symlink install paths from the
  README's install matrix.
- Supported surfaces are now Claude Code (plugin or manual clone) and,
  when built, Cowork.

## v0.5.0 — 2026-07-05

Hardens the ritual against the failure mode that motivated the release: a
user ran the skill from an install silently frozen at v0.1.0 — three
releases stale, missing the contract mechanism entirely — with nothing in
the ritual to reveal it. Also closes the greenfield/retrofit scaffolding
gap and teaches chat-only mode to use memory where the surface has one.

- Version self-announcement: the agent's literal first line is now
  `Running north-star vX.Y.Z.`, so a stale install is visible in the
  first second of a run instead of never. The version literal lives in
  two places (frontmatter + announcement line); bump both per release.
- Greenfield parity: Phase 1A gains a 1A.5 read-back that seeds the
  North Star contract, exactly as retrofit's 1B.1 does. The contract and
  its phase-boundary reprints were retrofit-only; the reasons they exist
  (multi-step interview, human loses track of evolving state) apply to
  greenfield too. Phase 2/3/4 reprint markers are now unconditional.
- Chat-only memory integration: when the chat surface has a persistent
  memory feature, the agent offers to keep a consented backup copy of the
  contract there — updated on every confirmed revision, final artifacts
  saved at Phase 4 — instead of only warning that scrollback is lossy.
  Memory supplements the human's own saved copy; it never replaces it.
- Worked example: docs/example-run.md, an abbreviated CODE-retrofit
  transcript showing correct behaviour at each step (read-back
  correction, contract seeding, evidence-anchored questions, the 1B.4.5
  re-grounding catch, Phase 4 amendment). Referenced from SKILL.md as
  read-on-demand calibration, not loaded by default.

## v0.4.0 — 2026-05-29

Generalises the ritual from code-only to any project shape. The interview
logic is unchanged; only the inputs (what counts as evidence) and outputs
(where the result lands) are now shape-aware. One skill, not two.
See docs/v0.4-rationale.md.

- Phase 0 split into two sequential questions: shape (code / document /
  mixed) and state (greenfield / exists). Shape drives evidence and
  destination; state drives 1A vs 1B.
- 1B.0 evidence list branches by shape, with the universal principle
  stated up front. Adds an explicit chat-only branch: the agent has no
  file access and asks the human to paste the material.
- 1B.2 examples branched into parallel CODE and DOCUMENT lists.
- Neutral vocabulary pass: 1B.3 reframed as "what's hard to copy, in
  practice", with the moat / defensibility framing kept as a marked
  business reading. Default tone aimed at a non-developer, non-founder.
- Phase 4 destination detection: code → PROJECT.md; document → primary
  strategy doc (ask if absent); chat-only → printed markdown block.
  Retrofit amendment discipline now described for all three shapes.
- North Star contract section rewritten: the mechanism described once,
  abstractly, then three concrete forms (repo dotfile, visible working
  doc, in-conversation reprint).
- Added docs/v0.4-rationale.md.

## v0.3.0 — 2026-05-29

Hardens the retrofit ritual against the helpme2c failure mode (a North Star
accepted, then found to have missed the product's most important dimension).
See docs/POSTMORTEM-helpme2c-2026-05-29.md.

- Re-grounding check (new 1B.4.5): reprint the read-back, verify the chosen
  candidate still covers every load-bearing noun; read-back wins on divergence.
- 1B.4 defence reframed: human defends the candidate against the read-back,
  not against the other candidate.
- Coverage check on candidate generation: candidates must collectively cover
  every load-bearing noun in the read-back.
- Phase 4 now produces four explicit artifacts — Mission, Metric (time-bounds
  named as measurement frames), Companion, Boundary — revisable independently.
- Default-naming discipline: unstated operationalisation defaults are named
  and opened to challenge.
- North Star contract file (docs/.north-star-contract.md): the agent's source
  of truth from 1B.1, updated only on confirmation, deleted at Phase 4 commit.
- Visual reprint of the contract after every confirmed update and at every
  phase boundary, with unfilled fields shown as "(not yet defined)".
- Added docs/POSTMORTEM-helpme2c-2026-05-29.md.

## v0.1.0 — 2026-05-29
