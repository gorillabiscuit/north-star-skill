# north-star

A standalone [Claude Code](https://claude.com/claude-code) skill that runs the
**North Star kickoff** ritual: a structured interview that converges on ONE
product North Star metric, a companion sentence ("what this means for what we
build"), and a scope boundary ("what does NOT serve this") — written into your
project's `PROJECT.md`.

A North Star is a proxy for delivered value, not a vanity count. The ritual is
opinionated by design: it interviews you one question at a time, rejects vanity
metrics (signups, MAU, page views), generates at least two candidates, and
pressure-tests them before recommending one. You decide.

The ritual lives in [`SKILL.md`](./SKILL.md).

## Two modes

The ritual asks once, at Phase 0, which mode applies:

- **Greenfield** — nothing built yet. The agent interviews you from a blank
  slate (Phase 1A): what the product is, the single most important user, the
  one job they hire it to do.
- **Retrofit** — code shipped, decisions made, real or pilot users exist. The
  agent reads the evidence first (README, PROJECT.md, recent commits, ROADMAP,
  LEARNED), reads back what it found, then interviews you informed by it
  (Phase 1B). The result lands in `PROJECT.md` as a **dated amendment**, never a
  blind replacement.

When in doubt, the ritual picks retrofit — reading first is cheap; writing from
blank into a non-blank repo causes real damage.

## Install

### Claude Code (user-level skill)

Clone this repo into your user skills directory so it's available in every
project:

```bash
git clone git@github.com:gorillabiscuit/north-star-skill.git ~/.claude/skills/north-star
```

Then in any project, invoke it with:

```
/north-star
```

To update later: `git -C ~/.claude/skills/north-star pull`.

### claude.ai

Zip the skill folder and upload it via the skills UI:

```bash
cd ~/Code/north-star-skill
zip -r north-star.zip SKILL.md
```

Then upload `north-star.zip` in claude.ai's skill settings.

### Cowork

Cowork plugin support is **planned but not yet built**. For now, use the Claude
Code or claude.ai install paths above.

## Where the result goes

The ritual writes a `## North Star` block into your project's `PROJECT.md`
containing the metric, the companion sentence, and the boundary. In a repo that
uses an `AGENTS.md` relevance gate, that block is what every non-trivial task is
expected to trace back to.

## License

MIT — see [LICENSE](./LICENSE).
