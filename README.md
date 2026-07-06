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
- **State.** **GREENFIELD** (nothing built or written yet), **EXISTS** (work
  already exists that should be read first), or **REVISE** (a filled North
  Star already exists and needs a targeted amendment)? State drives whether
  the agent interviews from blank (Phase 1A), reads the evidence first and
  amends (Phase 1B), or runs the short revision pass (Phase 1C).

When in doubt between GREENFIELD and EXISTS, treat as EXISTS — reading first
is cheap; writing-from-blank into a non-blank project causes real damage.
REVISE is deliberately narrow: it changes only the fields with a nameable
failure behind them, and escalates to the full retrofit if the star needs a
rethink rather than an amendment.

## Where the result goes

Phase 4 detects the destination — it's not a mode the human picks at the start.
The four artifacts are universal; only the write step branches:

- **Code project →** written into `PROJECT.md` under `## North Star`. In a repo
  that uses an `AGENTS.md` relevance gate, that block is what every non-trivial
  task is expected to trace back to.
- **Document project →** written into the project's primary strategy document,
  under a clearly named "North Star" section. If no such document exists, the
  agent asks where it should live rather than assuming a path.

Once the star lands, the ritual marks the moment with a **finalisation
reveal** — the finished star shown once as a full ASCII scene (a five-pointed
star, the Metric boxed at centre, Saturn alongside). Every other display —
the working draft you watch evolve through the interview, a project's
session-start reminder — uses a plain bordered box. Spectacle is reserved for
the moment the star is set, so it stays a landmark rather than wallpaper.

## Install / use matrix

| Surface | How to run it |
|---|---|
| Claude Code (recommended) | install as a plugin via the [gorillabiscuit marketplace](https://github.com/gorillabiscuit/claude-plugins) (below) — auto-updates, no manual `git pull` |
| Claude Code (manual) | clone into `~/.claude/skills/north-star` (below) — you own the update step |
| Cowork | planned — a Cowork plugin wrapper |

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

### Cowork

Cowork plugin support is **planned but not yet built**. For now, use one of
the Claude Code routes above.

## License

MIT — see [LICENSE](./LICENSE).
