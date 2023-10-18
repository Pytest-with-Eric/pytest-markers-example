import pytest


# First test for login functionality
@pytest.mark.login
def test_login_valid_user():
    username = "valid_user"
    password = "valid_pass"
    assert username == "valid_user" and password == "valid_pass"


# Second test for login functionality
@pytest.mark.login
def test_login_invalid_user():
    username = "invalid_user"
    password = "valid_pass"
    # Let's check if the invalid username doesn't match a known valid username
    # and if the password does match a known valid password
    assert username != "valid_user" and password == "valid_pass"


# First test for signup functionality
@pytest.mark.signup
def test_signup_new_user():
    new_username = "new_user"
    new_password = "new_pass"
    assert new_username == "new_user" and new_password == "new_pass"


# Second test for signup functionality
@pytest.mark.signup
def test_signup_existing_user():
    existing_username = "existing_user"
    assert existing_username == "existing_user"
