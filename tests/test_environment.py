import pytest


@pytest.mark.development
def test_dev_environment():
    assert True


@pytest.mark.production
def test_prod_environment():
    assert True
