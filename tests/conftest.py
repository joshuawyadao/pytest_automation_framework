""" ConfTest.py

Configuration file for PyTest

"""

import pytest

### INTEGER INPUTS ###

# Two positive
@pytest.fixture
def pos_int_pos_int():
    return 5, 2

# Two negative
@pytest.fixture
def neg_int_neg_int():
    return -3, -6

# One positive, one negative
@pytest.fixture
def pos_int_neg_int():
    return 9, -2

# One negative, one positive
@pytest.fixture
def neg_int_pos_int():
    return -7, 1

# Two zeros
@pytest.fixture
def zero_zero():
    return 0, 0

# One positive, one zero
@pytest.fixture
def pos_int_zero():
    return 1, 0

# One zero, one positive
@pytest.fixture
def zero_pos_int():
    return 0, 8

# One negative, one zero
@pytest.fixture
def neg_int_zero():
    return -6, 0

# One zero, one negative
@pytest.fixture
def neg_int_zero():
    return 0, -2

### FLOAT INPUTS ###
#TODO: Add in permutations for FLOAT inputs

### STRING INPUTS ###
#TODO: Add in permutations for String inputs