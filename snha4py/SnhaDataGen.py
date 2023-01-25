#! /usr/bin/env python3

"""
St. Nicolas House Algorithm data generation.

The module generates data correlated data along a directed graph based on the Monte Carlo approach. For further inforation see [Novine et al. (2022)](https://doi.org/10.52905/hbph2021.3.26).
"""
import numpy as np
import pandas as pd


class SnhaDataGen:
    def __init__(self, graph, n, steps, mean, sd, noise, prop):
        """
        Create a data generator for correlated data based on a graph.

        Args:
            graph (numpy.ndarray): adjacents matrix of a directed graph
            n (int): the number of measurements per node, default: 100
            steps (int): the number of iterations, default: 15
            mean (float): mean value for sampling from a Gaussian distribution, default: 100
            sd (float): standard deviation for sampling from a Gaussian distribution, default: 2
            noise (float): standard deviation for sampling noise from a Gaussian distribution with mean 0 after each iteration, default: 1
            prop (float): proportion of the target node value take the source node, default: 0.05
        """
        self.graph = graph
        self.n = n
        self.steps = steps
        self.mean = mean
        self.sd = sd
        self.noise = noise
        self.prop = prop

    def create_data(self):
        """
        Creates correlated data along edges of a directed graph based on a Monte Carlo approach.

        Examples:

        ```{.py}
        from snha4py.SnhaDataGen import SnhaDataGen
        import numpy as np

        graph = np.array(
            [
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
            ]
        )
        dg = SnhaDataGen(graph, n=100, steps=15, mean=100, sd=2, noise=1, prop=0.05)

        data = dg.get_data()
        print(data)
        ```
        """
        p = self.graph.shape[0]
        vtx = np.arange(p)
        data_mat = np.zeros((p, self.n))
        for i in range(self.n):
            x = np.random.normal(self.mean, self.sd, size=p)
            for j in range(self.steps):
                np.random.shuffle(vtx)
                for source in vtx:
                    neighbors = np.flatnonzero(self.graph[source])
                    if len(neighbors) == 0:
                        continue
                    np.random.shuffle(neighbors)
                    for target in neighbors:
                        weight = self.graph[source, target]
                        x_ = x[source] * self.prop * abs(weight) + x[target] * (
                            1 - self.prop
                        ) * abs(weight)
                        if weight < 0:
                            x[target] = 2 * x[target] - x_
                        else:
                            x[target] = x_
                x += np.random.normal(0, self.noise, size=p)
            data_mat[:, i] = x
        self.data = pd.DataFrame(data_mat.T)

    def get_data(self):
        """
        Returns:
            self.data (pandas.DataFrame): correlated data of size (p, n), with p the number of nodes of the graph and n the number of measurements per node.
        """
        self.create_data()
        return self.data


if __name__ == "__main__":
    graph = np.array(
        [
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    dg = SnhaDataGen(graph, n=100, steps=15, mean=100, sd=2, noise=1, prop=0.05)

    data = dg.get_data()
    print(data)
