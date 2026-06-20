#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DATA="$ROOT/data"
COMPETITION="pokemon-tcg-ai-battle"

mkdir -p "$DATA"
kaggle competitions download -c "$COMPETITION" -p "$DATA"
unzip -qo "$DATA/${COMPETITION}.zip" -d "$DATA/sdk"
echo "Competition SDK extracted to $DATA/sdk"

# Refresh cg/ engine from official sample if missing
if [[ ! -f "$ROOT/cg/api.py" ]]; then
  cp -r "$DATA/sdk/sample_submission/cg" "$ROOT/cg"
  echo "Copied cg/ from sample submission"
fi
