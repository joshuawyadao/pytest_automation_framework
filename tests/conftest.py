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
def zero_int_zero_int():
    return 0, 0

# One positive, one zero
@pytest.fixture
def pos_int_zero_int():
    return 1, 0

# One zero, one positive
@pytest.fixture
def zero_int_pos_int():
    return 0, 8

# One negative, one zero
@pytest.fixture
def neg_int_zero_int():
    return -6, 0

# One zero, one negative
@pytest.fixture
def neg_int_zero_int():
    return 0, -2

### STRING INPUTS ###

# Two chars
@pytest.fixture
def char_char():
    return "a", "c"

# Two strings
@pytest.fixture
def str_str():
    return "test", "help"

# One char, one string
@pytest.fixture
def char_str():
    return "x", "math"

# One string, one char
@pytest.fixture
def str_char():
    return "happy", "v"

## Combination of String and INT inputs ##

# One positive int, one positive string
@pytest.fixture
def pos_int_str():
    return 9, "1"

# One positive string, one positive int
@pytest.fixture
def str_pos_int():
    return "3", 5

# One neg int, one positive string
@pytest.fixture
def neg_int_str():
    return -9, "1"

# One string, one neg int
@pytest.fixture
def str_neg_int():
    return "3", -5

# One zero int, one string
@pytest.fixture
def zero_int_str():
    return 0, "-4"

# One string, one zero int
@pytest.fixture
def str_zero_int():
    return "-6", 0