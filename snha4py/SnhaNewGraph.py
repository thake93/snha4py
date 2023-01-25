#! /usr/bin/env python3

"""
The St. Nicolas House Algorithm graph collection.

Examples:

```{.py}
from snha4py.SnhaNewGraph import SnhaNewGraph

fct = dir(SnhaNewGraph)
ignore = ["set_graph", "get_graph", "undir2dir"]
for f in fct:
    if f not in ignore and "__" not in f:
        print(f)
        g = SnhaNewGraph(graph_type=f, nodes=5, edges=8, mode="directed", cont=2)
        graph = g.get_graph()
        print(graph)
```
"""
import numpy as np


class SnhaNewGraph:
    def __init__(self, graph_type, nodes, edges, mode, cont):
        """
        Creates a new graph.

        Args:
            graph_type (str): type of the graph
                "werner" (default)
                "rnd_chain"
                "band"
                "circle"
                "hub"
                "random"
                "barabasi_m1"
                "barabasi_m2"
            nodes (int): number of nodes in the graph (default: 5)
            edges (int): number of edges in the graph (default: 6)
            mode (str):
                "directed": directed graph (default)
                "undirected": undirected graph
            cont (int): number of signal seeds; default: 2 (only for graph type rndChain)
        """
        self.nodes = nodes
        self.edges = edges
        self.graph = np.zeros((nodes, nodes))
        self.mode = mode
        self.cont = cont
        self.set_graph(graph_type)

    def band(self):
        """
        Implementation of a band graph.
        """
        for i in range(self.nodes - 1):
            self.graph[i, i + 1] = 1

    def barabasi(self, m=1):
        """
        Creates an Barabasi-M1/M2 graph.

        Args:
            m (int):
                1 (default): barabasi-M1 graph
                2: brabasi-M2 graph
        """
        self.graph[1, 0] = 1
        for n in range(2, self.nodes):
            if m == n:
                sel = n - 1
            else:
                sel = m
            deg = (self.graph + self.graph.T).sum(axis=1)
            prob = deg[:n] / (deg[:n].sum())
            idx = np.random.choice(range(n), size=sel, p=prob)
            self.graph[idx, n] = 1

    def barabasi_m1(self):
        """
        Implementation of a barabasi-M1 graph.
        """
        self.barabasi()

    def barabasi_m2(self):
        """
        Implementation of a barabasi-M2 graph.
        """
        self.barabasi(m=2)

    def circle(self):
        """
        Implementation of a circle graph.
        """
        self.band()
        self.graph[self.nodes - 1, 0] = 1

    def edge_dir_shuffle(self):
        """
        Shuffle the direction of the Snha objects graph edges.
        """
        for i in range(self.graph.shape[0]):
            for j in range(self.graph.shape[0]):
                w = self.graph[i, j] + self.graph[j, i]
                if w > 0:
                    if int(np.random.uniform(0, 2)):
                        self.graph[i, j] = w
                        self.graph[j, i] = 0
                    else:
                        self.graph[i, j] = 0
                        self.graph[j, i] = w

    def hub(self):
        """
        Implementation of a hub graph.
        """
        ix = np.random.choice(range(self.nodes))
        self.graph[ix, :] = 1
        self.graph[ix, ix] = 0

    def get_graph(self):
        """
        Returns:
            self.graph (numpy.ndarray): the created graph
        """
        if self.mode == "undirected":
            return self.graph + self.graph.T
        else:
            return self.graph

    def random(self):
        """
        Implementation of a random graph.
        """
        g = np.zeros(self.nodes**2)
        ix = np.random.choice(range(self.nodes**2), self.edges, replace=False)
        g[ix] = 1
        self.graph = g.reshape((self.nodes, self.nodes))

    def rnd_chain(self):
        """
        Implementation of a random graph. Select random start nodes and create directed paths through all nodes.
        """
        x, y = np.triu_indices(self.nodes, k=1)
        up_tri = np.array(list(zip(x, y)))
        v = np.random.choice(range(len(up_tri)), size=self.edges, replace=False)
        idx = up_tri[v]
        for i in idx:
            x, y = i
            self.graph[x, y] = 1
        self.graph = self.graph + self.graph.T

        start = np.random.choice(range(self.nodes), size=self.cont, replace=False)
        g_new = np.zeros((self.nodes, self.nodes))
        self.undir2dir(start, [], g_new, self.nodes)
        self.graph = g_new

    def set_graph(self, fct):
        """
        Calls the graph-function and sets the graph.

        Args:
            fct (string): name of the graph to call the function
        """
        f = getattr(self, fct)
        f()

    def undir2dir(self, start, visited, g_new, nodes):
        """
        Creates a directed graph from an undirected graph.

        Args:
            start (numpy.ndarray): list of start nodes
            visited (list): list of nodes already visited
            g_new (np.array): directed graph
            nodes (int): number of nodes
        """
        all_n = []
        np.random.shuffle(start)
        for s in start:
            if s in visited:
                continue
            visited.append(s)
            (neigh,) = np.where(self.graph[s] == 1)
            all_n.append(neigh)
            np.random.shuffle(neigh)

            for n in neigh:
                if g_new[s, n] == 1 or g_new[n, s] == 1:
                    continue
                else:
                    g_new[s, n] = 1
            if len(visited) == nodes:
                return
        for n in all_n:
            self.undir2dir(n, visited, g_new, nodes)

    def werner(self):
        """
        Implementation of a werner graph.
        """
        self.graph = np.array(
            [
                [0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0],
            ]
        )


if __name__ == "__main__":
    fct = dir(SnhaNewGraph)
    ignore = ["set_graph", "get_graph", "undir2dir"]
    for f in fct:
        if f not in ignore and "__" not in f:
            print(f)
            g = SnhaNewGraph(graph_type=f, nodes=5, edges=8, mode="directed", cont=2)
            graph = g.get_graph()
            print(graph)
