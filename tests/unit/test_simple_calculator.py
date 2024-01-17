""" test_simple_calculator.py

Unit test suite to test the Simple Calculator

"""

import pytest, sys
sys.path.insert(0, '././calculator')
from simple_calculator import SimpleCalculator

### 1. TEST CASES ###

# 1.1 Addition w/ INT inputs
ADD_INT_TEST_CASES = ("add_int, expected_add_int", [
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

# 1.2 Subtraction w/ INT inputs
SUB_INT_TEST_CASES = ("sub_int, expected_sub_int", [
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

# 1.3 Multiplication w/ INT inputs
MULT_INT_TEST_CASES = ("mult_int, expected_mult_int", [
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

# 1.4 Division w/ INT inputs
DIV_INT_TEST_CASES = ("div_int, expected_div_int", [
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

# 1.5 All arithmetic w/ STR inputs (always result in TypeError)
STRING_TEST_CASES = ("arith_str, expected_str", [
    ("char_char", TypeError),       # Two chars
    ("str_str", TypeError),         # Two strings
    ("char_str", TypeError),        # One char, one string
    ("str_char", TypeError),        # One string, one char
    ("pos_str_pos_str", TypeError), # Two strings of positive ints
    ("neg_str_neg_str", TypeError), # Two strings of negative ints
    ("pos_str_neg_str", TypeError), # Two strings of one positive, one negative
    ("neg_str_pos_str", TypeError), # Two strings of one negative, one positive
])

# 1.6 All arithmetic w/ COMBO inputs (always result in TypeError)
COMBO_TEST_CASES = ("arith_combo, expected_combo", [
    ("pos_int_str", TypeError),     # One positive int, one positive string
    ("str_pos_int", TypeError),     # One positive string, one positive int
    ("neg_int_str", TypeError),     # One neg int, one positive string
    ("str_neg_int", TypeError),     # One string, one neg int
    ("zero_int_str", TypeError),    # One zero int, one string
    ("str_zero_int", TypeError),    # One string, one zero int
])

### 2. CALCULATOR OBJECT ###

# Create a calculator object to run the Simple Calculator Test Suite
@pytest.fixture(scope="module")
def calculator():
    return SimpleCalculator()

### 3. TESTS ###

### 3.1 INTEGER INPUTS ###

# 3.1.1. Addition w/ INT inputs
@pytest.mark.parametrize(*ADD_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.addition
def test_addition_int(calculator, add_int, expected_add_int, request):
    x, y = request.getfixturevalue(add_int)
    assert calculator.add(x, y) == expected_add_int
    
# 3.1.2. Subtraction w/ INT inputs
@pytest.mark.parametrize(*SUB_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.subtraction
def test_subtraction_int(calculator, sub_int, expected_sub_int, request):
    x, y = request.getfixturevalue(sub_int)
    assert calculator.subtract(x, y) == expected_sub_int
    
# 3.1.3. Multiplication w/ INT inputs
@pytest.mark.parametrize(*MULT_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.multiplication
def test_multiplication_int(calculator, mult_int, expected_mult_int, request):
    x, y = request.getfixturevalue(mult_int)
    assert calculator.multiply(x, y) == expected_mult_int
    
# 3.1.4. Division w/ INT inputs
@pytest.mark.parametrize(*DIV_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.division
def test_division_int(calculator, div_int, expected_div_int, request):
    x, y = request.getfixturevalue(div_int)
    assert calculator.divide(x, y) == expected_div_int

### 3.2 STRING INPUTS ###

# 3.2.1. Addition w/ STR inputs
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module")
@pytest.mark.str_input
@pytest.mark.addition
def test_addition_str(calculator, arith_str, expected_str, request):
    x, y = request.getfixturevalue(arith_str)
    assert calculator.add(x, y) == expected_str
    
# 3.2.2. Subtraction w/ STR inputs
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module") 
@pytest.mark.str_input
@pytest.mark.subtraction
def test_subtraction_str(calculator, arith_str, expected_str, request):
    x, y = request.getfixturevalue(arith_str)
    assert calculator.subtract(x, y) == expected_str
    
# 3.2.3. Multiplication w/ STR inputs 
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module")
@pytest.mark.str_input
@pytest.mark.multiplication
def test_multiplication_str(calculator, arith_str, expected_str, request):
    x, y = request.getfixturevalue(arith_str)
    assert calculator.multiply(x, y) == expected_str
    
# 3.2.4. Division w/ STR inputs 
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module")
@pytest.mark.str_input
@pytest.mark.division
def test_division_str(calculator, arith_str, expected_str, request):
    x, y = request.getfixturevalue(arith_str)
    assert calculator.divide(x, y) == expected_str

### 3.3 COMBINATION INPUTS ###

# 3.3.1. Addition w/ COMBO inputs 
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module")
@pytest.mark.combo_input
@pytest.mark.addition
def test_addition_combo(calculator, arith_combo, expected_combo, request):
    x, y = request.getfixturevalue(arith_combo)
    assert calculator.add(x, y) == expected_combo
    
# 3.3.2. Subtraction w/ COMBO inputs 
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module") 
@pytest.mark.combo_input
@pytest.mark.subtraction
def test_subtraction_combo(calculator, arith_combo, expected_combo, request):
    x, y = request.getfixturevalue(arith_combo)
    assert calculator.subtract(x, y) == expected_combo
    
# 3.3.3. Multiplication w/ COMBO inputs 
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module")
@pytest.mark.combo_input
@pytest.mark.multiplication
def test_multiplication_combo(calculator, arith_combo, expected_combo, request):
    x, y = request.getfixturevalue(arith_combo)
    assert calculator.multiply(x, y) == expected_combo
    
# 3.3.4. Division w/ COMBO inputs 
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module")
@pytest.mark.combo_input
@pytest.mark.division
def test_division_combo(calculator, arith_combo, expected_combo, request):
    x, y = request.getfixturevalue(arith_combo)
    assert calculator.divide(x, y) == expected_combo