import pytest


# A fixture returning a sample database entry.
@pytest.fixture
def database_data():
    return {"username": "Alice", "password": "password123"}


# Test function using the database_data fixture.
def test_database_entry(database_data):
    assert database_data["username"] == "Alice"
    assert database_data["password"] == "password123"
