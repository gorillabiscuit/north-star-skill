# north-star-skill — project brief

## North Star

_(added retrofit, 2026-07-05)_

- **Mission.** north-star-skill makes a builder sit down and converge
  what their project is actually for into four durable artifacts — and
  exists so that the AI agents working on that project carry that
  bigger picture into every decision, however deep the subtask and
  however many context windows later, instead of optimising locally
  while the goal drifts out of frame. It lives where enforcement can
  live: Claude Code, for code and document projects alike.

- **Metric.** Per week, the number of work units across the
  maintainer's projects whose one-sentence North Star trace survives
  independent review. (Defaults, open to challenge: "per week" is the
  measurement frame, not the definition of success; a "work unit" is a
  commit or PR on a code project, a substantive edit or decision on a
  document project; "independent review" is a cold-context reviewer or
  audit, not the authoring session grading itself. Baseline measured
  2026-07-05 on helpme2c: 0 of 30 commits.)

- **Companion.** What this means for what we build: enforcement
  machinery before interview polish — hooks that block feature work
  while the star is unfilled, session-start injection so the star is
  always in frame, trace review folded into pre-PR — built code-first,
  document projects after; plus the end-of-ritual feedback issue form
  so real runs improve the next version.

- **Boundary.** What does NOT serve this: surfaces outside Claude Code
  (chat paste blocks, claude.ai zips, Pi) — they can define a star but
  never enforce one; telemetry pipelines for other users' runs;
  monetisation or copyability concerns; further interview refinement
  not demanded by a real documented failure; and anything that helps a
  human define a goal they then keep in their head instead of putting
  it where the AI works.

---

## What this is

The rest of this brief is intentionally thin: the product is the ritual
in [SKILL.md](./SKILL.md), its rationale lives in [docs/](./docs/), and
its history in [CHANGELOG.md](./CHANGELOG.md). This file exists to hold
the North Star above — the block every non-trivial change to this repo
should trace to.
