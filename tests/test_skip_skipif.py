import pytest
import sys


# A test that will always be skipped.
@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_example_skip():
    assert 2 + 2 == 4


# A test that will be skipped if it's run on a Python version earlier than 3.8.
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8 or later.")
def test_example_skipif():
    assert 3 * 3 == 9
