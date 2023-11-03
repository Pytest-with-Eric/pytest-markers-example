import pytest


# A test that's expected to fail.
@pytest.mark.xfail(reason="Expected to fail until we fix the bug.")
def test_example_xfail():
    assert 2 * 3 == 7


# A normal test that's expected to pass.
def test_example_xpass():
    assert 3 * 2 == 6
