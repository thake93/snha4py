#! /usr/bin/env python3
import numpy as np


def chains2admat(chains, shape):
    """
    Converts association chains into an adjacency matrix.

    Args:
        chains (list): list of association chains
        shape (tuple): size of graph

    Returns:
        graph (numpy.ndarray): predicted graph created by association chains
    """
    graph = np.zeros(shape)
    for ch in chains:
        for i in range(len(ch) - 1):
            graph[ch[i], ch[i + 1]] = 1
    return graph


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
