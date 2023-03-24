#! /usr/bin/env python3
import numpy as np


def np_in(arr, lst):
    """
    Checks if an array is contained in a list of arrays.

    Args:
        arr (numpy.ndarray): array which may contain in lst
        lst (itterable): list containing arrays

    Returns:
        boolean
    """
    for l in lst:
        if np.array_equal(arr, l):
            return True
    return False
