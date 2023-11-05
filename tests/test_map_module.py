import pytest
from hidee_ho import maps


def test_state():
    assert maps.state_abbreviation("ViRgInIa") == "VA"


def test_state_abbreviation():
    assert maps.state_abbreviation("va") == "VA"


def test_muliple_states():
    assert maps.list_abbreviations(["Virginia", "PA"]) == ["VA", "PA"]


def test_list_with_one_state():
    assert maps.list_abbreviations("Virginia") == ["VA"]


def test_state_does_not_exist():
    with pytest.raises(KeyError):
        maps.state_abbreviation("Not A State")
