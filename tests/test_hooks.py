import pytest


# A test with a special marker
@pytest.mark.special_test
def test_example():
    assert 1 == 1


# A test without the special marker
def test_regular_example():
    assert 2 == 2


def pytest_runtest_setup(item):
    """This hook runs before a test starts"""
    if "special_test" in item.keywords:
        print("\nGetting ready for a special test!")


def pytest_runtest_teardown(item, nextitem):
    """This hook runs after a test ends"""
    if "special_test" in item.keywords:
        print("\nCleaning up after a special test!")
