#!/usr/bin/env python3
"""Generate an alternative RGB888 test image — checkerboard + circle + gradients."""

from __future__ import annotations

import argparse
from pathlib import Path


def pixel(width: int, height: int, x: int, y: int) -> tuple[int, int, int]:
    """A visually distinct pattern with:
    - Checkerboard background (cyan / orange)
    - Central white circle
    - Diagonal gradient stripes
    - Red border
    """
    # Red border (3px)
    if (x < 3 or x >= width - 3 or y < 3 or y >= height - 3):
        return 255, 20, 20

    # Central white circle (radius ~20)
    cx, cy = width // 2, height // 2
    dx = x - cx
    dy = y - cy
    if dx * dx + dy * dy < 18 * 18:
        return 240, 240, 240

    # Diagonal stripes (left-top to right-bottom)
    if (x + y) % 20 < 10:
        return 40, 40, 40

    # Checkerboard background
    if (x // 8 + y // 8) % 2 == 0:
        r, g, b = 0, 160, 200   # cyan
    else:
        r, g, b = 220, 120, 40  # orange

    return r, g, b


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", type=int, default=128)
    parser.add_argument("--height", type=int, default=72)
    parser.add_argument("--output", type=Path, default=Path("build1/input_alt.hex"))
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="ascii") as f:
        for y in range(args.height):
            for x in range(args.width):
                for channel in pixel(args.width, args.height, x, y):
                    f.write(f"{channel:02x}\n")


if __name__ == "__main__":
    main()
