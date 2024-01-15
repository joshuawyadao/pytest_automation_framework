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

### INT INPUTS ###

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
    ("zero_int_neg_int", -2),   # Add one zero, one negative ints
])

# Test addition function
@pytest.mark.int_input
@pytest.mark.addition
def test_addition_int(calculator, add_int, expected_add_int, request):
    x, y = request.getfixturevalue(add_int)
    assert calculator.add(x, y) == expected_add_int
    
# Parametrize integer inputs for SUBTRACTION
@pytest.mark.parametrize("sub_int, expected_sub_int", [
    ("pos_int_pos_int", 3),     # Sub two positive ints
    ("neg_int_neg_int", 3),     # Sub two negative ints
    ("pos_int_neg_int", 11),    # Sub one positive, one negative ints
    ("neg_int_pos_int", -8),    # Sub one negative, one positive ints
    ("zero_int_zero_int", 0),   # Sub two zeros ints
    ("pos_int_zero_int", 1),    # Sub one positive, one zero ints
    ("zero_int_pos_int", -8),   # Sub one zero, one positive ints
    ("neg_int_zero_int", -6),   # Sub one negative, one zero ints
    ("zero_int_neg_int", 2),    # Sub one zero, one negative ints
])

# Test subtraction function
@pytest.mark.int_input
@pytest.mark.subtraction
def test_subtraction_int(calculator, sub_int, expected_sub_int, request):
    x, y = request.getfixturevalue(sub_int)
    assert calculator.subtract(x, y) == expected_sub_int
    
# Parametrize integer inputs for MULTIPLICATION 
@pytest.mark.parametrize("mult_int, expected_mult_int", [
    ("pos_int_pos_int", 10),    # Multi two positive ints
    ("neg_int_neg_int", 18),    # Multi two negative ints
    ("pos_int_neg_int", -18),   # Multi one positive, one negative ints
    ("neg_int_pos_int", -7),    # Multi one negative, one positive ints
    ("zero_int_zero_int", 0),   # Multi two zeros ints
    ("pos_int_zero_int", 0),    # Multi one positive, one zero ints
    ("zero_int_pos_int", 0),    # Multi one zero, one positive ints
    ("neg_int_zero_int", 0),    # Multi one negative, one zero ints
    ("zero_int_neg_int", 0),    # Multi one zero, one negative ints
])

# Test multiplication function
@pytest.mark.int_input
@pytest.mark.multiplication
def test_multiplication_int(calculator, mult_int, expected_mult_int, request):
    x, y = request.getfixturevalue(mult_int)
    assert calculator.multiply(x, y) == expected_mult_int
    
# Parametrize integer inputs for DIVISION 
@pytest.mark.parametrize("div_int, expected_div_int", [
    ("pos_int_pos_int", 2.5),                   # Div two positive ints
    ("neg_int_neg_int", 0.5),                   # Div two negative ints
    ("pos_int_neg_int", -4.5),                  # Div one positive, one negative ints
    ("neg_int_pos_int", -7),                    # Div one negative, one positive ints
    ("zero_int_zero_int", ZeroDivisionError),   # Div two zeros ints
    ("pos_int_zero_int", ZeroDivisionError),    # Div one positive, one zero ints
    ("zero_int_pos_int", 0),                    # Div one zero, one positive ints
    ("neg_int_zero_int", ZeroDivisionError),    # Div one negative, one zero ints
    ("zero_int_neg_int", 0),                    # Div one zero, one negative ints
])

# Test division function
@pytest.mark.int_input
@pytest.mark.division
def test_division_int(calculator, div_int, expected_div_int, request):
    x, y = request.getfixturevalue(div_int)
    assert calculator.divide(x, y) == expected_div_int

# TODO: Add in test suite for String inputs

# TODO: Add in test suite for the cominbation inputs