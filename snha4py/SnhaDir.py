#! /usr/bin/env python3

"""
Direction analysis of the St. Nicolas House Algorithm.

Soon be updated.
"""


class SnhaDir:
    def comp_xi(self):
        """
        Computes Xi correlation matrix for the Snha objects data.
        """
        self.xi = np.zeros((self.data.shape[1], self.data.shape[1]))
        for i, r1 in enumerate(self.data):
            for j, r2 in enumerate(self.data):
                self.xi[i, j] = self.xiCorr(self.data[r1], self.data[r2])
        self.xi = pd.DataFrame(self.xi)

    def get_xi(self):
        """
        Get the Xi correlation matrix from the Snha object.

        Returns:
            xi: Xi correlation matrix
        """
        return self.xi

    def xi_corr(self, x, y):
        """
        Computes the Xi correlation between two arrays.

        Args:
            x (pandas.Series): Data vector
            y (pandas.Series): Data vector

        Returns:
            xi: Xi correlation from x to y
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
