from unittest.mock import patch, MagicMock
import pytest

from poker import FormatPoker, Variante, TypeJeuPoker


# Fixture pour fournir des instances de FormatPoker et leurs clés
@pytest.fixture
def format_poker_fixture():
    format_poker_instances = [
        FormatPoker(Variante.TEXAS_HOLDEM_NO_LIMIT, TypeJeuPoker.MTT, 9),
        FormatPoker(Variante.TEXAS_HOLDEM_NO_LIMIT, TypeJeuPoker.MTT_KO, 6),
        FormatPoker(Variante.TEXAS_HOLDEM_NO_LIMIT, TypeJeuPoker.CASH_GAME, 2),
    ]
    format_poker_keys = [fp.to_key() for fp in format_poker_instances]
    return format_poker_instances, format_poker_keys


def test_from_key(format_poker_fixture):
    format_poker_instances, format_poker_keys = format_poker_fixture

    for instance, key in zip(format_poker_instances, format_poker_keys):
        recreated_instance = FormatPoker.from_key(key)
        assert recreated_instance.variante == instance.variante
        assert recreated_instance.type_jeu == instance.type_jeu
        assert recreated_instance.n_joueurs == instance.n_joueurs