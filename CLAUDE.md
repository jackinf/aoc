# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an Advent of Code (AoC) solutions repository. Solutions exist in two languages:

- **Python** — covers 2021–2024 under `python/<year>/day<NN>/`
- **Rust** — covers 2024–2025 under `rust/bin/<year>/day<NN>/`

Each day directory contains `part1` and `part2` solution files, one or more sample input files, and `input.txt` (personal puzzle input).

## Python

### Running solutions

Scripts read input relative to the working directory, so run from the solution directory:

```bash
cd python/2024/day01
python part1.py
```

To run against sample data, change `input.txt` to `sample.txt` (or `sample1.txt`, etc.) inside the script, or temporarily swap the file.

### Debugging

Set `DEBUG=1` to enable verbose output (used via the `pr()` helper in `python/2024/utils.py`):

```bash
DEBUG=1 python part1.py
```

### Dependencies

Python solutions use `poetry` (see `pyproject.toml`):

```bash
poetry install
```

Direct install via pip also works (`requirements.txt` lists: matplotlib, sympy, networkx, scipy, numpy).

### Conventions (Python)

- Input is always read from a local file with `open('input.txt')` — no stdin.
- `part1.py` / `part2.py` split when the two parts diverge significantly; `main.py` is used when they share most logic.
- `brainstorm.py`, `sol.py`, and `*_not_mine.py` files are scratch/reference files, not the primary solution.
- `__checks__/` directories contain lightweight assertion-based correctness checks (not pytest) that are run directly: `python __checks__/checks_foo.py`.
- `python/2024/dayxx/` serves as a template for new days.

## Rust

All Rust solutions live in a single Cargo workspace at `rust/`. Each day's `part1.rs` and `part2.rs` are registered as separate `[[bin]]` entries in `rust/Cargo.toml` with names following the pattern `<year>_day<NN>_part<N>`.

### Building and running

```bash
cd rust

# Build everything
cargo build

# Build a specific binary
cargo build --bin 2025_day07_part1

# Run a specific binary
cargo run --bin 2025_day07_part1

# Run with logging enabled
RUST_LOG=debug cargo run --bin 2025_day07_part1
```

### Testing (inline Rust tests)

```bash
cd rust
cargo test                          # all tests
cargo test --bin 2025_day07_part1   # tests within a specific binary
```

The `test-case` crate is available for parameterised test cases.

### Conventions (Rust)

- Input is embedded at compile time with `include_str!("input.txt")` — no file I/O at runtime.
- 2025 solutions use `env_logger` with `env_logger::init()` and log via `log::{debug, info}`. Enable with `RUST_LOG=debug`.
- 2024 solutions (earlier style) use a `const DEBUG: bool` flag or `log::debug!` directly.
- When days share parsing logic, a `common.rs` file lives alongside `part1.rs` and `part2.rs`.
- `rust/bin/2024/dayxx/` is the Rust template for new days; it includes `error.rs`, `prelude.rs`, and a `utils/` module with a `W<T>` newtype wrapper for implementing `TryFrom` on foreign types.
- New `[[bin]]` entries must be added to `rust/Cargo.toml` before the binary can be built.

### Adding a new Rust day

1. Copy `rust/bin/2024/dayxx/` to `rust/bin/<year>/day<NN>/`.
2. Add `[[bin]]` entries for `part1` and `part2` in `rust/Cargo.toml`.
3. Place `input.txt` and sample files (`sample0.txt`, `sample1.txt`, …) in the new directory.
