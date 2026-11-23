# Antigravity Tiny Chess Engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/BLD933/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/BLD933/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A tournament-tested 4KB Python chess engine built for the [make.fun tiny-chess-01](https://make.fun/c/tiny-chess-01) challenge.

## Features & Architecture

- **Board Representation**: 0x88 board with incremental 64-bit Zobrist hashing for positions, castling rights, and en passant squares.
- **Search Algorithm**: Iterative deepening alpha-beta with Transposition Table (TT), 2 killer moves per ply, and adaptive Null-Move Pruning (R=3).
- **Quiescence**: Selective capture and in-check escape resolution with MVV-LVA move ordering.
- **Evaluation**: Piece-Square Tables with endgame king tables, bishop pair bonus (+30 cp), and material balance.
- **Budget**: 55,000 node search cap ensuring deterministic execution, 0 timeouts, and ~2.0s average thinking time.
- **Integration**: Full make.fun `/game` and `/move` HTTP client protocol.

## Compliance

- `main.py`: 4,088 bytes (cap: 4,096 bytes)
- Snapshot: ~5.9 KB (cap: 8,192 bytes)
- Deterministic search (zero wall-clock dependence in move selection).

