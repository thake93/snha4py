#! /usr/bin/env python3
import numpy as np
import pandas as pd

"""
Direction analysis of the St. Nicolas House Algorithm.

Soon be updated. 
[Back to github](https://github.com/thake93/snha4py/)
"""


class SnhaDir:
    def __init__(self, data):
        self.data = data
        self.xi = None

    def comp_xi(self):
        """
        Computes Xi correlation matrix for the Snha objects data.
        """
        xi = np.zeros((self.data.shape[1], self.data.shape[1]))
        for i, r1 in enumerate(self.data):
            for j, r2 in enumerate(self.data):
                xi[i, j] = self.xi_corr(self.data[r1], self.data[r2])
        self.xi = pd.DataFrame(xi)

    def deg_mat(mat):
        """
        Computes the degree matrix.

        Args:
            mat (numpy.ndarray): Input matrix

        Returns:
            deg (numpy.ndarray): degree matrix of input matrix
        """
        m_undir = mat + mat.T
        m_undir[m_undir != 0] = 1
        tri = np.triu(m_undir)
        c = tri.sum(axis=0)
        r = tri.sum(axis=1)
        deg = (c + r) * np.eye(mat.shape[0])
        return deg

    def get_xi(self):
        """
        Get the Xi correlation matrix from the Snha object.

        Returns:
            xi (pandas.DataFrame): Xi correlation matrix
        """
        return self.xi

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

    def xi_corr(self, x, y):
        """
        Computes the Xi correlation between two arrays.

        Args:
            x (pandas.Series): Data vector
            y (pandas.Series): Data vector

        Returns:
            xi (float): Xi correlation from x to y
        """
        # x, y = pd.Series(x), pd.Series(y)
        n = len(x)
        rk_x = x.rank()
        f = y.rank(method="max") / n
        g = (-y).rank(method="max") / n
        order = rk_x.sort_values().index
        f = f[order].to_numpy()
        A = np.mean(abs(f[0 : (n - 1)] - f[1:n])) * (n - 1) / (2 * n)
        C = np.mean(g * (1 - g))
        xi = 1 - (A / C)
        return xi
