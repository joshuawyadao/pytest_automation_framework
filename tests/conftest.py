""" ConfTest.py

Configuration file for PyTest

"""

import pytest

### INTEGER INPUTS ###

# Positive INT value
@pytest.fixture
def positive_int():
    return 5

# Negative INT value
@pytest.fixture
def negative_int():
    return -3

# Zero INT value
@pytest.fixture
def zero_int():
    return 0

### FLOAT INPUTS ###

# Positive FLOAT value
@pytest.fixture
def postive_float():
    return 7.21

# Negative FLOAT value
@pytest.fixture
def negative_float():
    return -2.38

# Zero FLOAT value
@pytest.fixture
def zero_float():
    return 0.00

### STRING INPUTS ###

# Single CHAR value
@pytest.fixture
def single_char():
    return "a"

# STRING value
@pytest.fixture
def string_val():
    return "test"

# STRING of an positive INT value
@pytest.fixture
def string_positive_int():
    return "9"

# STRING of an negative INT value
@pytest.fixture
def string_negative_int():
    return "-8"

# STRING of an positive FLOAT value
@pytest.fixture
def string_positive_float():
    return "6.45"

# STRING of an negative FLOAT value
@pytest.fixture
def string_negative_float():
    return "-4.73"