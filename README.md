# Pokémon TCG AI Battle — Simulation Track

Build an AI agent for the [PTCG AI Battle Challenge Simulation](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle).

**GitHub:** [dogahwisdom/pokemon-tcg-ai-battle](https://github.com/dogahwisdom/pokemon-tcg-ai-battle)

Locally grouped under `~/Documents/kaggle-competitions/` (workspace folder only — this repo is standalone).

**Current agent:** Roman Rozen's **Crustle-aware Mega Lucario V9** (public LB 950+ tier), hardened with crash-safe decision wrapper and retuned deck list.

## Leaderboard context (2026-06-20)

| Rank | Team | Score |
|------|------|-------|
| 1 | hiroingk | 1309.0 |
| 2 | The Debauchery Tea Party | 1285.6 |
| 3 | カドラバ Kadoraba | 1256.8 |

Top public code: [romanrozen/strong-start-crustle-lucario-agent-v9-lb-950](https://www.kaggle.com/code/romanrozen/strong-start-crustle-lucario-agent-v9-lb-950) (94 votes).

## Senior-scientist strategy

1. **Meta-first:** Day-1 #1 was a Crustle wall immune to ex attackers — route through non-ex Hariyama.
2. **Deck-policy coupling:** Policy hardcodes card IDs; deck variants must stay inside the Lucario shell.
3. **Never crash:** Validation plays you vs yourself; any exception = lost submission.
4. **Measure before search:** Enable `USE_SEARCH` only after local `search_begin` smoke tests pass.
5. **Next upgrades:** MCTS (Kiyota sample), deck A/B via self-play harness, forward search with time budget.

## Layout

```
main.py          # Kaggle entry (agent function)
deck.csv         # 60-card list (crustle_retuned default)
cg/              # Official game engine (from competition SDK)
src/ptcg_battle/ # Modular deck variants for experiments
scripts/         # Download + package submission.tar.gz
```

## Quick start

```bash
./scripts/download_competition.sh   # one-time
./scripts/package_submission.sh     # builds submission.tar.gz
# Kaggle UI -> Submit Agent -> upload submission.tar.gz
```

## Configuration

| Env var | Default | Description |
|---------|---------|-------------|
| `DECK_VARIANT` | `crustle_retuned` | Deck list (`baseline`, `public1084_energy_hero`) |

Edit `main.py` flags: `CRUSTLE_AWARE`, `USE_SEARCH`, `SEARCH_TIME_BUDGET`.

## Submission format

`submission.tar.gz` containing:

- `main.py` — must expose `agent(obs_dict) -> list[int]`
- `deck.csv` — 60 card IDs
- `cg/` — engine bindings from competition sample
