import pytest
from hidee_ho import maps


def test_state():
    assert maps.state_abbreviation("ViRgInIa") == "VA"


def test_state_abbrev():
    assert maps.state_abbreviation("va") == "VA"


def test_states():
    assert maps.list_abbreviations(["Virginia", "PA"]) == ["VA", "PA"]


def test_state_does_not_exist():
    with pytest.raises(Exception):
        maps.state_name_to_abbreviation("Not A State")
