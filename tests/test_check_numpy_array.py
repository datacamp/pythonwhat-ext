from pythonwhat_ext import check_numpy_array
from pythonwhat.check_syntax import Ex
from pythonwhat.Test import TestFail as TF

import numpy as np

import pytest
from helpers import create_x_state

def test_check_numpy_array():
    state = create_x_state(np.array([1,2,3]), np.array([1,2,3]))
    check_numpy_array("x", state = state)

def test_check_numpy_array_fail():
    state = create_x_state(np.array([1,2,3]), np.array([1,2]))
    with pytest.raises(TF):
        check_numpy_array("x", state = state)

def test_ex_check_numpy_array():
    state = create_x_state(np.array([1,2,3]), np.array([1,2, 3]))
    Ex(state).multi(check_numpy_array('x'))
