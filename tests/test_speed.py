import pytest
import time
from calculator import Calculator

# Importing a hypothetical Calculator class from
# calculator module.


# Marked as a 'fast' test, this function tests the addition method of the Calculator.
@pytest.mark.fast
def test_fast_add():
    calc = Calculator()  # Creating an instance of the Calculator class.
    result = calc.add(2, 2)  # Using the add method to add two numbers.
    assert result == 4  # Asserting that the result is correct.


# Marked as a 'slow' test due to the intentional delay, this function tests the
# subtraction method of the Calculator.
@pytest.mark.slow
def test_slow_subtraction():
    time.sleep(5)  # Introducing a delay of 5 seconds to simulate a slow test.
    calc = Calculator()  # Creating an instance of the Calculator class.
    result = calc.subtract(10, 5)  # Using the subtract method to subtract two numbers.
    assert result == 5  # Asserting that the result is correct.
