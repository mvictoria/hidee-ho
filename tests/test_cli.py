import filecmp
from pathlib import Path

import pytest
from click.testing import CliRunner
from hidee_ho import main


@pytest.fixture
def call_cli_with_va():
    state = "va"
    outfile = "file.html"
    runner = CliRunner()
    result = runner.invoke(main.cli, [state, "-o", outfile])
    yield result, outfile
    Path(outfile).unlink()


def test_cli_with_state(call_cli_with_va):
    assert call_cli_with_va[0].exit_code == 0
    assert filecmp.cmp(call_cli_with_va[1], "./tests/va_map.html") == 0
