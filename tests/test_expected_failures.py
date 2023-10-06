import pytest


@pytest.mark.xfail(reason="Known bug with version 2.0")
def test_known_failure():
    assert False


@pytest.mark.xfail(reason="Expected to fail intermittently")
def test_intermittent_failure():
    result = 1 + 1
    assert result == 3


def test_regular():
    assert True
