""" ConfTest.py

Configuration file for PyTest

"""

import pytest

### PY-TEST HTML CONFIGURATION ###

#########################
### 1. INTEGER INPUTS ###
#########################

# 1.1. Two positive
@pytest.fixture(scope="session")
def pos_int_pos_int():
    return 5, 2

# 1.2. Two negative
@pytest.fixture(scope="session")
def neg_int_neg_int():
    return -3, -6

# 1.3. One positive, one negative
@pytest.fixture(scope="session")
def pos_int_neg_int():
    return 9, -2

# 1.4. One negative, one positive
@pytest.fixture(scope="session")
def neg_int_pos_int():
    return -7, 1

# 1.5. Two zeros
@pytest.fixture(scope="session")
def zero_int_zero_int():
    return 0, 0

# 1.6. One positive, one zero
@pytest.fixture(scope="session")
def pos_int_zero_int():
    return 1, 0

# 1.7. One zero, one positive
@pytest.fixture(scope="session")
def zero_int_pos_int():
    return 0, 8

# 1.8. One negative, one zero
@pytest.fixture(scope="session")
def neg_int_zero_int():
    return -6, 0

# 1.9. One zero, one negative
@pytest.fixture(scope="session")
def zero_int_neg_int():
    return 0, -2

########################
### 2. STRING INPUTS ###
########################

# 2.1. Two chars
@pytest.fixture(scope="session")
def char_char():
    return "a", "c"

# 2.2. Two strings
@pytest.fixture(scope="session")
def str_str():
    return "test", "help"

# 2.3. One char, one string
@pytest.fixture(scope="session")
def char_str():
    return "x", "math"

# 2.4. One string, one char
@pytest.fixture(scope="session")
def str_char():
    return "happy", "v"

# 2.5. Two strings of positive ints
@pytest.fixture(scope="session")
def pos_str_pos_str():
    return "3", "5"

# 2.6. Two strings of negative ints
@pytest.fixture(scope="session")
def neg_str_neg_str():
    return "-7", "-4"

# 2.7. Two strings of one positive, one negative
@pytest.fixture(scope="session")
def pos_str_neg_str():
    return "6", "-8"

# 2.8. Two strings of one negative, one positive
@pytest.fixture(scope="session")
def neg_str_pos_str():
    return "-2", "5"

#############################
### 3. COMBINATION INPUTS ###
#############################

# 3.1. One positive int, one positive string
@pytest.fixture(scope="session")
def pos_int_str():
    return 9, "1"

# 3.2. One positive string, one positive int
@pytest.fixture(scope="session")
def str_pos_int():
    return "3", 5

# 3.3. One neg int, one positive string
@pytest.fixture(scope="session")
def neg_int_str():
    return -9, "1"

# 3.4. One string, one neg int
@pytest.fixture(scope="session")
def str_neg_int():
    return "3", -5

# 3.5. One zero int, one string
@pytest.fixture(scope="session")
def zero_int_str():
    return 0, "-4"

# 3.6. One string, one zero int
@pytest.fixture(scope="session")
def str_zero_int():
    return "-6", 0