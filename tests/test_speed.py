import pytest
import time


@pytest.mark.fast
def test_fast_one():
    assert True


@pytest.mark.fast
def test_fast_two():
    assert True


@pytest.mark.slow
def test_slow_one():
    time.sleep(5)
    assert True
