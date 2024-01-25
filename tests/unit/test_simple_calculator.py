""" test_simple_calculator.py

Unit test suite to test the Simple Calculator

"""

import sys
from contextlib import nullcontext as does_not_raise
import pytest
sys.path.insert(0, '././calculator')
from simple_calculator import SimpleCalculator

#####################
### 1. TEST CASES ###
#####################

# 1.1. Addition w/ INT inputs
ADD_INT_TEST_CASES = ("add_int, expected_add_int, test_case_name", [
    ("pos_int_pos_int", 7,      "1.1. Add two positive ints"),
    ("neg_int_neg_int", -9,     "1.2. Add two negative ints"),
    ("pos_int_neg_int", 7,      "1.3. Add one positive, one negative ints"),
    ("neg_int_pos_int", -6,     "1.4. Add one negative, one positive ints"),
    ("zero_int_zero_int", 0,    "1.5. Add two zeros ints"),
    ("pos_int_zero_int", 1,     "1.6. Add one positive, one zero ints"),
    ("zero_int_pos_int", 8,     "1.7. Add one zero, one positive ints"),
    ("neg_int_zero_int", -6,    "1.8. Add one negative, one zero ints"),
    ("zero_int_neg_int", -2,    "1.9. Add one zero, one negative ints"),
])

# 1.2. Subtraction w/ INT inputs
SUB_INT_TEST_CASES = ("sub_int, expected_sub_int, test_case_name", [
    ("pos_int_pos_int", 3,      "1.1. Sub two positive ints"),
    ("neg_int_neg_int", 3,      "1.2. Sub two negative ints"),
    ("pos_int_neg_int", 11,     "1.3. Sub one positive, one negative ints"),
    ("neg_int_pos_int", -8,     "1.4. Sub one negative, one positive ints"),
    ("zero_int_zero_int", 0,    "1.5. Sub two zeros ints"),
    ("pos_int_zero_int", 1,     "1.6. Sub one positive, one zero ints"),
    ("zero_int_pos_int", -8,    "1.7. Sub one zero, one positive ints"),
    ("neg_int_zero_int", -6,    "1.8. Sub one negative, one zero ints"),
    ("zero_int_neg_int", 2,     "1.9. Sub one zero, one negative ints"),
])

# 1.3. Multiplication w/ INT inputs
MULT_INT_TEST_CASES = ("mult_int, expected_mult_int, test_case_name", [
    ("pos_int_pos_int", 10,     "1.1. Multi two positive ints"),
    ("neg_int_neg_int", 18,     "1.2. Multi two negative ints"),
    ("pos_int_neg_int", -18,    "1.3. Multi one positive, one negative ints"),
    ("neg_int_pos_int", -7,     "1.4. Multi one negative, one positive ints"),
    ("zero_int_zero_int", 0,    "1.5. Multi two zeros ints"),
    ("pos_int_zero_int", 0,     "1.6. Multi one positive, one zero ints"),
    ("zero_int_pos_int", 0,     "1.7. Multi one zero, one positive ints"),
    ("neg_int_zero_int", 0,     "1.8. Multi one negative, one zero ints"),
    ("zero_int_neg_int", 0,     "1.9. Multi one zero, one negative ints"),
])

# 1.4. Division w/ INT inputs
DIV_INT_TEST_CASES = ("div_int, expected_div_int, error_int, test_case_name", [
    ("pos_int_pos_int", 2.5, does_not_raise(),                  "1.1. Div two positive ints"),
    ("neg_int_neg_int", 0.5, does_not_raise(),                  "1.2. Div two negative ints"),
    ("pos_int_neg_int", -4.5, does_not_raise(),                 "1.3. Div one positive, one negative ints"),
    ("neg_int_pos_int", -7, does_not_raise(),                   "1.4. Div one negative, one positive ints"),
    ("zero_int_zero_int", 0, pytest.raises(ZeroDivisionError),  "1.5. Div two zeros ints"),
    ("pos_int_zero_int", 0, pytest.raises(ZeroDivisionError),   "1.6. Div one positive, one zero ints"),
    ("zero_int_pos_int", 0, does_not_raise(),                   "1.7. Div one zero, one positive ints"),
    ("neg_int_zero_int", 0, pytest.raises(ZeroDivisionError),   "1.8. Div one negative, one zero ints"),
    ("zero_int_neg_int", 0, does_not_raise(),                   "1.9. Div one zero, one negative ints"),
])

# 1.5. All arithmetic w/ STR inputs (always result in TypeError)
STRING_TEST_CASES = ("arith_str, expected_str, error_str, test_case_name", [
    ("char_char", 0, pytest.raises(TypeError),          "2.1. Two chars"),
    ("str_str", 0, pytest.raises(TypeError),            "2.2. Two strings"),
    ("char_str", 0, pytest.raises(TypeError),           "2.3. One char, one string"),
    ("str_char", 0, pytest.raises(TypeError),           "2.4. One string, one char"),
    ("pos_str_pos_str", 0, pytest.raises(TypeError),    "2.5. Two strings of positive ints"),
    ("neg_str_neg_str", 0, pytest.raises(TypeError),    "2.6. Two strings of negative ints"),
    ("pos_str_neg_str", 0, pytest.raises(TypeError),    "2.7. Two strings of one positive, one negative"),
    ("neg_str_pos_str", 0, pytest.raises(TypeError),    "2.8. Two strings of one negative, one positive"),
])

# 1.6. All arithmetic w/ COMBO inputs (always result in TypeError)
COMBO_TEST_CASES = ("arith_combo, expected_combo, error_combo, test_case_name",[
    ("pos_int_str", 0, pytest.raises(TypeError),    "3.1. One positive int, one positive string"),
    ("str_pos_int", 0, pytest.raises(TypeError),    "3.2. One positive string, one positive int"),
    ("neg_int_str", 0, pytest.raises(TypeError),    "3.3. One neg int, one positive string"),
    ("str_neg_int", 0, pytest.raises(TypeError),    "3.4. One string, one neg int"),
    ("zero_int_str", 0, pytest.raises(TypeError),   "3.5. One zero int, one string"),
    ("str_zero_int", 0, pytest.raises(TypeError),   "3.6. One string, one zero int"),
])

############################
### 2. CALCULATOR OBJECT ###
############################

# Create a calculator object to run the Simple Calculator Test Suite
@pytest.fixture(scope="module")
def calculator():
    return SimpleCalculator()

################
### 3. TESTS ###
################

### 3.1. INTEGER INPUTS ###

# 3.1.1. Addition w/ INT inputs
@pytest.mark.order(1)
@pytest.mark.parametrize(*ADD_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.addition
def test_addition_int(calculator, add_int, expected_add_int, test_case_name, request):
    # Set the docstring
    test_addition_int.__doc__ = f"Addition with INTEGERS: {test_case_name}"
    # Run the test
    x, y = request.getfixturevalue(add_int)
    assert calculator.add(x, y) == expected_add_int
    
# 3.1.2. Subtraction w/ INT inputs
@pytest.mark.order(2)
@pytest.mark.parametrize(*SUB_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.subtraction
def test_subtraction_int(calculator, sub_int, expected_sub_int, test_case_name, request):
    # Set the docstring
    test_subtraction_int.__doc__ = f"Subtraction with INTEGERS: {test_case_name}"
    # Run the test
    x, y = request.getfixturevalue(sub_int)
    assert calculator.subtract(x, y) == expected_sub_int
    
# 3.1.3. Multiplication w/ INT inputs
@pytest.mark.order(3)
@pytest.mark.parametrize(*MULT_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.multiplication
def test_multiplication_int(calculator, mult_int, expected_mult_int, test_case_name, request):
    # Set the docstring
    test_multiplication_int.__doc__ = f"Multiplication with INTEGERS: {test_case_name}"
    # Run the test
    x, y = request.getfixturevalue(mult_int)
    assert calculator.multiply(x, y) == expected_mult_int
    
# 3.1.4. Division w/ INT inputs
@pytest.mark.order(4)
@pytest.mark.parametrize(*DIV_INT_TEST_CASES, scope="module")
@pytest.mark.int_input
@pytest.mark.division
def test_division_int(calculator, div_int, expected_div_int, error_int, test_case_name, request):
    # Set the docstring
    test_division_int.__doc__ = f"Division with INTEGERS: {test_case_name}"
    # Run the test
    with error_int:
        x, y = request.getfixturevalue(div_int)
        assert calculator.divide(x, y) == expected_div_int

### 3.2. STRING INPUTS ###

# 3.2.1. Addition w/ STR inputs
@pytest.mark.order(5)
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module")
@pytest.mark.str_input
@pytest.mark.addition
def test_addition_str(calculator, arith_str, expected_str, error_str, test_case_name, request):
    # Set the docstring
    test_addition_str.__doc__ = f"Addition with STRINGS: {test_case_name}"
    # Run the test
    with error_str:
        x, y = request.getfixturevalue(arith_str)
        assert calculator.add(x, y) == expected_str
    
# 3.2.2. Subtraction w/ STR inputs
@pytest.mark.order(6)
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module") 
@pytest.mark.str_input
@pytest.mark.subtraction
def test_subtraction_str(calculator, arith_str, expected_str, error_str, test_case_name, request):
    # Set the docstring
    test_subtraction_str.__doc__ = f"Subtraction with STRINGS: {test_case_name}"
    # Run the test
    with error_str:
        x, y = request.getfixturevalue(arith_str)
        assert calculator.subtract(x, y) == expected_str
    
# 3.2.3. Multiplication w/ STR inputs
@pytest.mark.order(7) 
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module")
@pytest.mark.str_input
@pytest.mark.multiplication
def test_multiplication_str(calculator, arith_str, expected_str, error_str, test_case_name, request):
    # Set the docstring
    test_multiplication_str.__doc__ = f"Multiplication with STRINGS: {test_case_name}"
    # Run the test
    with error_str:
        x, y = request.getfixturevalue(arith_str)
        assert calculator.multiply(x, y) == expected_str
    
# 3.2.4. Division w/ STR inputs 
@pytest.mark.order(8)
@pytest.mark.parametrize(*STRING_TEST_CASES, scope="module")
@pytest.mark.str_input
@pytest.mark.division
def test_division_str(calculator, arith_str, expected_str, error_str, test_case_name, request):
    # Set the docstring
    test_division_str.__doc__ = f"Division with STRINGS: {test_case_name}"
    # Run the test
    with error_str:
        x, y = request.getfixturevalue(arith_str)
        assert calculator.divide(x, y) == expected_str

### 3.3. COMBINATION INPUTS ###

# 3.3.1. Addition w/ COMBO inputs 
@pytest.mark.order(9)
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module")
@pytest.mark.combo_input
@pytest.mark.addition
def test_addition_combo(calculator, arith_combo, expected_combo, error_combo, test_case_name, request):
    # Set the docstring
    test_addition_combo.__doc__ = f"Addition with COMBO: {test_case_name}"
    # Run the test
    with error_combo:
        x, y = request.getfixturevalue(arith_combo)
        assert calculator.add(x, y) == expected_combo
    
# 3.3.2. Subtraction w/ COMBO inputs 
@pytest.mark.order(10)
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module") 
@pytest.mark.combo_input
@pytest.mark.subtraction
def test_subtraction_combo(calculator, arith_combo, expected_combo, error_combo, test_case_name, request):
    # Set the docstring
    test_subtraction_combo.__doc__ = f"Subtraction with COMBO: {test_case_name}"
    # Run the test
    with error_combo:
        x, y = request.getfixturevalue(arith_combo)
        assert calculator.subtract(x, y) == expected_combo
    
# 3.3.3. Multiplication w/ COMBO inputs
@pytest.mark.order(11) 
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module")
@pytest.mark.combo_input
@pytest.mark.multiplication
def test_multiplication_combo(calculator, arith_combo, expected_combo, error_combo, test_case_name, request):
    # Set the docstring
    test_multiplication_combo.__doc__ = f"Multiplication with COMBO: {test_case_name}"
    # Run the test
    with error_combo:
        x, y = request.getfixturevalue(arith_combo)
        assert calculator.multiply(x, y) == expected_combo
    
# 3.3.4. Division w/ COMBO inputs 
@pytest.mark.order(12)
@pytest.mark.parametrize(*COMBO_TEST_CASES, scope="module")
@pytest.mark.combo_input
@pytest.mark.division
def test_division_combo(calculator, arith_combo, expected_combo, error_combo, test_case_name, request):
    # Set the docstring
    test_division_combo.__doc__ = f"Division with COMBO: {test_case_name}"
    # Run the test
    with error_combo:
        x, y = request.getfixturevalue(arith_combo)
        assert calculator.divide(x, y) == expected_combo