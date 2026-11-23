# Antigravity Tiny Chess Engine

[![make.fun tiny-chess-01](https://img.shields.io/badge/make.fun-tiny--chess--01-blue)](https://make.fun/c/tiny-chess-01)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

A high-performance chess engine in under 4 KB of Python for the [make.fun tiny-chess-01](https://make.fun/c/tiny-chess-01) competition.

## Architecture

- **Representation**: 0x88 board representation with incremental 64-bit Zobrist hashing.
- **Search**: Iterative deepening alpha-beta with Transposition Table (TT), Killer move heuristics (2 per ply), and Null-Move Pruning (adaptive R=3).
- **Quiescence**: Selective search extending captures and check evasions.
- **Evaluation**: Piece-Square Tables with endgame king transitions, bishop pair bonus, and piece activity terms.
- **Budget**: Fixed node search cap (55,000 nodes/move) ensuring 100% deterministic replay and ~2s average move latency.
- **Protocol**: Native HTTP client implementing the make.fun `/game` and `/move` API.

## Size & Compliance

- `main.py`: 3,746 bytes (cap: 4,096 bytes)
- Total snapshot: ~5.8 KB (cap: 8,192 bytes)
- Standard MIT License & paired owner wallet configuration.
