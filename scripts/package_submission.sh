#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$ROOT/submission"
VARIANT="${DECK_VARIANT:-crustle_retuned}"

rm -rf "$OUT"
mkdir -p "$OUT/cg"

cp "$ROOT/main.py" "$OUT/main.py"
cp -r "$ROOT/cg/"* "$OUT/cg/"

# Write deck from variant module when Python is available
if command -v python3 >/dev/null 2>&1; then
  PYTHONPATH="$ROOT/src" python3 - <<PY
from ptcg_battle.decks.lucario_variants import write_deck_csv
write_deck_csv("$OUT/deck.csv", "$VARIANT")
print("deck variant: $VARIANT")
PY
else
  cp "$ROOT/deck.csv" "$OUT/deck.csv"
fi

cd "$OUT"
tar -czf "$ROOT/submission.tar.gz" main.py deck.csv cg/
echo "Packaged $ROOT/submission.tar.gz"
echo "Upload via Kaggle -> Submit Agent"
