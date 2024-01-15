""" test_simple_calculator.py

Unit test suite for the simple_calculator.py file

"""

import pytest,sys
sys.path.insert(0, './calculator')
from simple_calculator import SimpleCalculator

# Create a calculator object to run all of the tests in this suite
@pytest.fixture(scope="test")
def calculator():
    return SimpleCalculator()

# Class to test Integer inputs into the calculator
class Test_Integer_Inputs:
    pass

# Class to test String inputs into the calculator
class Test_String_Inputs:
    pass

# Class to test a combination of Integer and String inputs into the calculator
class Test_Combination_Type_Inputs:
    pass