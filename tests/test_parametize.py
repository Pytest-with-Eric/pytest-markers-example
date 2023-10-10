import pytest


# Test function demonstrating the parametrize feature.
# It will run 3 times with different inputs.
@pytest.mark.parametrize("test_input,expected", [(1, 3), (3, 5), (5, 7)])
def test_addition(test_input, expected):
    assert test_input + 2 == expected
