"""Deck variant tests."""

from ptcg_battle.decks.lucario_variants import (
    CRUSTLE_RETUNED_DECK,
    DECK_VARIANTS,
    validate_deck,
)


def test_crustle_retuned_deck_is_legal() -> None:
    validate_deck(CRUSTLE_RETUNED_DECK)


def test_all_variants_are_60_cards() -> None:
    for name, deck in DECK_VARIANTS.items():
        validate_deck(deck)
        assert len(deck) == 60, name
