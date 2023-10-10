import time


# A test function simulating some processing time.
def test_addition():
    time.sleep(2)  # Simulating some delay
    assert 3 + 4 == 7


# Another test function with processing delay.
def test_subtraction():
    time.sleep(2)
    assert 10 - 3 == 7
