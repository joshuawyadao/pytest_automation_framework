""" test_simple_calculator.py

Unit test suite to test the Simple Calculator

"""

import pytest, sys
sys.path.insert(0, '././calculator')
from simple_calculator import SimpleCalculator

# Create a calculator object to run the Simple Calculator Test Suite
@pytest.fixture(scope="module")
def calculator():
    return SimpleCalculator()
   
# Parametrize integer inputs for ADDITION
@pytest.mark.parametrize("add_int, expected_add_int", [
    ("pos_int_pos_int", 7),     # Add two positive ints
    ("neg_int_neg_int", -9),    # Add two negative ints
    ("pos_int_neg_int", 7),     # Add one positive, one negative ints
    ("neg_int_pos_int", -6),    # Add one negative, one positive ints
    ("zero_int_zero_int", 0),   # Add two zeros ints
    ("pos_int_zero_int", 1),    # Add one positive, one zero ints
    ("zero_int_pos_int", 8),    # Add one zero, one positive ints
    ("neg_int_zero_int", -6),   # Add one negative, one zero ints
    ("zero_int_neg_int", -2),    # Add one zero, one negative ints
])

# Test addition function
@pytest.mark.int_input
@pytest.mark.addition
def test_addition_int(calculator, add_int, expected_add_int, request):
    x, y = request.getfixturevalue(add_int)
    assert calculator.add(x, y) == expected_add_int
