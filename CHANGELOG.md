# Changelog

All notable changes to this skill are documented here. This project follows
[Semantic Versioning](https://semver.org/).

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
