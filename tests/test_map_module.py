import filecmp
from pathlib import Path

import pytest
from hidee_ho import maps


@pytest.fixture
def va_map() -> Path:
    filename = Path("compare_map.html")
    maps.mapper("va").write_html(filename)
    yield filename
    filename.unlink()


def test_valid_state():
    assert maps.valid_state("VA")
    assert not maps.valid_state("Not A State")


def test_state():
    assert maps.state_abbreviation("ViRgInIa") == "VA"


def test_state_with_whitespace():
    assert maps.state_abbreviation(" washington ") == "WA"


def test_state_with_two_words():
    assert maps.state_abbreviation("new york ") == "NY"


def test_state_abbreviation():
    assert maps.state_abbreviation("va") == "VA"


def test_muliple_states():
    assert maps.list_abbreviations(["Virginia", "PA"]) == ["VA", "PA"]


def test_list_with_one_state():
    assert maps.list_abbreviations("Virginia") == ["VA"]


def test_state_does_not_exist():
    with pytest.raises(KeyError):
        maps.state_abbreviation("Not A State")


def test_map_output(va_map: Path):
    assert filecmp.cmp(va_map, "./tests/va_map.html") == 0
