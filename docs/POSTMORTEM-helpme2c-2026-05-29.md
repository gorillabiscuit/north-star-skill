# Postmortem — helpme2c North Star retrofit (2026-05-29)

One page on why the v0.3 ritual looks the way it does.

## What happened

We ran the retrofit ritual against the helpme2c repo. The interview produced
a North Star the human read, found plausible, and accepted. About an hour
later the human realised the accepted North Star missed the single most
important dimension of the product — **partner-mode-as-destination**
(pair-discovery) — and had quietly promoted cross-era to the headline when it
was really a tactic.

The North Star was recovered by re-grounding it against what the human had
originally said the product was. Recovery worked, but the failure was real
and avoidable.

## Why it happened

- The candidate the human picked was defended in real time, against the
  *other candidate* — not against the human's own earlier deliberate
  articulation of what the product is (the 1B.1 read-back).
- Every candidate sat on the same tactical axis (content breadth / cross-era).
  Pair-discovery was never offered as a candidate, so it could not win — it
  silently dropped out.
- The North Star was a single conflated statement. When the metric framing
  drifted, it took the mission with it; there was no separable "soul" to check
  the metric against.
- An operationalisation default ("per week") was presented as a decision, not
  a question. The human skimmed past it.
- There was no persistent, visible artifact of the destination during the
  interview, so neither agent nor human noticed the drift until much later.

## The fix (v0.3 — nine changes)

1. **Re-grounding check (new 1B.4.5).** After the human picks a candidate,
   reprint the confirmed read-back and check the candidate still covers every
   load-bearing noun. On divergence the read-back wins — it was deliberate;
   the candidate-defence was real-time.
2. **Defend against the read-back, not the other candidate (1B.4).** The human
   must name which read-back noun the candidate captures and which it loses;
   otherwise the agent redirects.
3. **Coverage check on candidate generation (1B.4).** List the read-back's
   load-bearing nouns first; candidates must collectively cover all of them.
   This is what would have forced pair-discovery onto the table.
4. **Mission / metric split (Phase 4).** Four explicit artifacts — Mission
   (soul), Metric (operationalisation, time-bounds named as measurement
   frames), Companion, Boundary — revisable independently, so a drifting
   metric can no longer drag the mission.
5. **Default-naming discipline (cross-cutting).** Any unstated default is named
   as a default and opened to challenge: "I picked X because …. Push back if
   this is wrong." The generalised "per week" lesson.
6. **This postmortem.** So future-me knows why the ritual looks like this.
7. **Version + changelog.** Bumped to v0.3.0.
8. **North Star contract file.** `docs/.north-star-contract.md` — the agent's
   source of truth from 1B.1 onward, updated only on human confirmation,
   always one version (replaced, never appended), deleted when Phase 4 commits
   to PROJECT.md.
9. **Visual reprint of the contract.** The human's view of the same source of
   truth, reprinted after every confirmed update and at every phase boundary,
   with unfilled fields shown as "(not yet defined)" so the destination stays
   visible the whole way.
