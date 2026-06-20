"""Lucario deck variants from top public notebooks (Roman Rozen, Pilkwang Kim)."""

from __future__ import annotations

from collections import Counter
from typing import Final

CARD_LABELS: Final[dict[int, tuple[str, str, str]]] = {
    673: ("Makuhita", "Pokemon", "Basic"),
    674: ("Hariyama", "Pokemon", "Stage 1"),
    675: ("Lunatone", "Pokemon", "Basic"),
    676: ("Solrock", "Pokemon", "Basic"),
    677: ("Riolu", "Pokemon", "Basic"),
    678: ("Mega Lucario ex", "Pokemon", "Mega ex"),
    1102: ("Dusk Ball", "Trainer", "Item"),
    1123: ("Switch", "Trainer", "Item"),
    1141: ("Premium Power Pro", "Trainer", "Tool"),
    1142: ("Fighting Gong", "Trainer", "Item"),
    1152: ("Poke Pad", "Trainer", "Item"),
    1159: ("Hero Cape", "Trainer", "Tool"),
    1182: ("Boss's Orders", "Trainer", "Supporter"),
    1192: ("Carmine", "Trainer", "Supporter"),
    1227: ("Lillie's Determination", "Trainer", "Supporter"),
    1252: ("Gravity Mountain", "Trainer", "Stadium"),
    6: ("Basic Fighting Energy", "Energy", "Basic Energy"),
}

BASELINE_DECK: Final[list[int]] = [
    673, 673, 674, 674, 675, 675, 676, 676,
    676, 677, 677, 677, 678, 678, 678, 678,
    1102, 1102, 1102, 1102, 1123, 1123, 1141, 1141,
    1141, 1141, 1142, 1142, 1142, 1142, 1152, 1152,
    1152, 1152, 1159, 1182, 1182, 1192, 1192, 1192,
    1192, 1227, 1227, 1227, 1227, 1252, 1252, 6,
    6, 6, 6, 6, 6, 6, 6, 6,
    6, 6, 6, 6,
]

# Roman V9 retuned list: 70% vs Crustle (from 10%), mulligan 25.9% -> 19.1%
CRUSTLE_RETUNED_DECK: Final[list[int]] = (
    [678] * 4 + [677] * 4 + [673] * 3 + [674] * 3 + [676] * 3 + [675] * 2
    + [1102] * 4 + [1152] * 4 + [1192] * 4 + [1142] * 3 + [1123] * 3 + [1141] * 2
    + [1227] * 3 + [1252] * 2 + [1182] * 2 + [1159] * 1 + [6] * 13
)

DEFAULT_DECK: Final[list[int]] = CRUSTLE_RETUNED_DECK


def _apply(deck: list[int], card_id: int, delta: int) -> list[int]:
    result = list(deck)
    if delta < 0:
        for _ in range(-delta):
            result.remove(card_id)
    else:
        result.extend([card_id] * delta)
    return result


PUBLIC1084_ENERGY_HERO_DECK: Final[list[int]] = _apply(
    _apply(
        _apply(_apply(_apply(list(BASELINE_DECK), 677, +1), 1182, +1), 6, +1),
        1252,
        -1,
    ),
    1152,
    -2,
)

DECK_VARIANTS: Final[dict[str, list[int]]] = {
    "baseline": BASELINE_DECK,
    "crustle_retuned": CRUSTLE_RETUNED_DECK,
    "public1084_energy_hero": PUBLIC1084_ENERGY_HERO_DECK,
}


def validate_deck(deck: list[int]) -> None:
    if len(deck) != 60:
        raise ValueError(f"deck must have 60 cards, got {len(deck)}")
    counts = Counter(deck)
    if any(n > 4 for cid, n in counts.items() if cid != 6):
        raise ValueError("max 4 copies per non-energy card")
    if counts.get(1159, 0) > 1:
        raise ValueError("Hero Cape is ACE SPEC: max 1")


def write_deck_csv(path: str, variant: str = "crustle_retuned") -> list[int]:
    deck = DECK_VARIANTS.get(variant, DEFAULT_DECK)
    validate_deck(deck)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(map(str, deck)) + "\n")
    return deck
