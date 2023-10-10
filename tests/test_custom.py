import pytest


# A test function with a custom marker.
@pytest.mark.custom
def test_custom_behavior():
    data = {"name": "John", "age": 30}
    assert data["age"] == 30
