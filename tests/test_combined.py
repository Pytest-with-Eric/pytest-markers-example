import pytest


@pytest.mark.marker1
@pytest.mark.marker2
def test_combined_markers():
    assert 1 + 1 == 2


def test_no_markers():
    assert 1 + 1 == 2
