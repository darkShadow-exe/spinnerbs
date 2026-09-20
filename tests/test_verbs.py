import pytest

from spinnerbs import random_verb, random_verbs
from spinnerbs.verbs import VERBS


def test_random_verb_returns_a_known_verb():
    verb = random_verb()
    assert verb in VERBS


def test_random_verbs_returns_unique_items():
    verbs = random_verbs(6)
    assert len(verbs) == 6
    assert len(set(verbs)) == 6
    assert all(item in VERBS for item in verbs)


def test_random_verbs_raises_for_large_n():
    with pytest.raises(ValueError, match="larger than"):
        random_verbs(len(VERBS) + 1)
