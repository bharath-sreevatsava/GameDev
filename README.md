# Fractured Light Prototype

This repository now includes the first playable **systems prototype** for the open-world concept.

## What is implemented

- Identity/system state models (fronting identity, stress, regulation, trust).
- World state models (district pressure/support and continuity logs).
- Core mechanics:
  - switch requests constrained by trust/stress/regulation,
  - grounding actions,
  - mission approach resolution based on active identity strengths.
- A runnable vertical slice CLI that simulates two missions.

## Run

```bash
PYTHONPATH=src python -m fractured_light.main
```

## Test

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Run on Windows

Use the included launcher scripts from the repository root:

```bat
run_game.bat
```

To run tests on Windows:

```bat
run_tests.bat
```
