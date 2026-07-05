#!/usr/bin/env python3
"""Render the North Star finalisation banner.

The ritual runs this ONCE, at Phase 4, when a star is finalised — a
fresh kickoff or a revise-mode amendment. It prints a 100-column ASCII
scene: a five-pointed star on the left, the Metric in a box overlaying
the star's right side, and Saturn on the right. This is the reveal —
the one moment the full scene appears. Every other display (the
working-draft reprints during the interview, a project's session-start
reminder) uses the plain bordered box, not this.

Usage: pass the final Metric sentence as argv (or on stdin):
    python3 scripts/render-north-star-banner.py "<metric sentence>"

Exits non-zero when the text will not fit the scene (the caller falls
back to the plain box) or on any error — the banner is celebration, it
must never be the reason the ritual fails to land the star.

The Saturn is the classic piece by Horroroso (signature -hrr- kept),
via https://asciiart.website/art/2526. The star and sky are generated
(fixed seed, so the banner is identical run to run).
"""

import math
import random
import sys
import textwrap

W, H = 100, 21
RAMP = " .,:;coCO8@"
MAX_TEXT_LINES = 9

SATURN = r'''                                             ___
                                          ,o88888
                                       ,o8888888'
                 ,:o:o:oooo.        ,8O88Pd8888"
             ,.::.::o:ooooOoOoO. ,oO8O8Pd888'"
           ,.:.::o:ooOoOoOO8O8OOo.8OOPd8O8O"
          , ..:.::o:ooOoOOOO8OOOOo.FdO8O8"
         , ..:.::o:ooOoOO8O888O8O,COCOO"
        , . ..:.::o:ooOoOOOO8OOOOCOCO"
         . ..:.::o:ooOoOoOO8O8OCCCC"o
            . ..:.::o:ooooOoCoCCC"o:o
            . ..:.::o:o:,cooooCo"oo:o:
         `   . . ..:.:cocoooo"'o:o:::'
         .`   . ..::ccccoc"'o:o:o:::'
        :.:.    ,c:cccc"':.:.:.:.:.'
      ..:.:"'`::::c:"'..:.:.:.:.:.'
    ...:.'.:.::::"'    . . . . .'
   .. . ....:."' `   .  . . ''
 . . . ...."'
 .. . ."'     -hrr-
.'''.split('\n')


def build_sky():
    random.seed(5)
    grid = [[' '] * W for _ in range(H)]
    cx, cy, raylen = 19.0, 10.0, 12.0
    rays = [math.radians(-90 + k * 72) for k in range(5)]
    for y in range(H):
        for x in range(52):
            dx, dy = (x - cx) / 2.0, y - cy
            r = math.hypot(dx, dy)
            b = 2.6 * math.exp(-(r * r) / 3.0)
            th = math.atan2(dy, dx)
            for a in rays:
                d = abs(math.atan2(math.sin(th - a), math.cos(th - a)))
                perp = r * math.sin(min(d, math.pi / 2))
                w = max(0.35, 2.6 * (1 - r / raylen))
                if d < math.pi / 2:
                    b += 2.1 * math.exp(-(perp / w) ** 2) * math.exp(-r / (raylen * 0.85))
            b += random.uniform(-0.05, 0.05)
            i = min(len(RAMP) - 1, int(max(b, 0) * (len(RAMP) - 1) / 2.6))
            ch = RAMP[i]
            if ch == ' ' and random.random() < 0.02:
                ch = random.choice("..''`,")
            grid[y][x] = ch
    for y, line in enumerate(SATURN):
        for x, ch in enumerate(line[:W - 51]):
            if ch != ' ':
                grid[y][51 + x] = ch
    return grid


def make_box(text, inner=32):
    lines = textwrap.wrap(text, inner)
    if not lines or len(lines) > MAX_TEXT_LINES:
        return None
    w = inner + 6
    box = ["+" + "-" * (w - 2) + "+"]
    box.append("|" + " N O R T H   S T A R ".center(w - 2, ".") + "|")
    box.append("|" + " " * (w - 2) + "|")
    for l in lines:
        box.append("|  " + l.ljust(inner) + "  |")
    box.append("|" + " " * (w - 2) + "|")
    box.append("+" + "-" * (w - 2) + "+")
    return box


def main():
    text = " ".join(sys.argv[1:]).strip() or sys.stdin.read().strip()
    text = " ".join(text.split())
    if not text:
        return 1
    box = make_box(text)
    if box is None or len(box) > H:
        return 1
    grid = build_sky()
    bx, by = 30, (H - len(box)) // 2
    for y, line in enumerate(box):
        for x, ch in enumerate(line):
            grid[by + y][bx + x] = ch
    print('\n'.join(''.join(r).rstrip() for r in grid))
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception:
        sys.exit(1)
