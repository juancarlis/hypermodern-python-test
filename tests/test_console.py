# tests/test_console.property

import click.testing
import pytest

from hypermodern_python_test import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_main_succeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0

