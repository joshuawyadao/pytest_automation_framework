""" test_simple_calculator.py

Unit test suite for the simple_calculator.py file

"""

import pytest,sys
sys.path.insert(0, './calculator')
from simple_calculator import SimpleCalculator

@pytest.fixture
def calculator():
    return SimpleCalculator()

def test_add_positive_ints(calculator, pos_int_pos_int):
    x, y = pos_int_pos_int
    assert calculator.add(x, y) == 7
    
# TODO: Add in other test cases