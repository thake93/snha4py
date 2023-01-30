#! /usr/bin/env python3

"""
The St. Nicolas House Algorithm plotting routine.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.colors import LinearSegmentedColormap
import random
import numpy as np
import igraph as ig


class SnhaPlot:
    def __init__(self, adj_mat, corr, labels_n, ax=None):
        """
        Create a support object to plot a graph or a correlation matrix.

        Args:
            adj_mat (numpy.ndarray): adjacency matrix to plot a graph with SnhaPlot.graph()
            corr (pd.DataFrame): correlation matrix to plot with SnhaPlot.corr()
            ax (matplotlib.axes): target axes to place the plot
            labels_n (list): variable names
        """
        self.adj_mat = adj_mat
        self.corr_mat = corr
        self.labels_n = labels_n

        if ax is None:
            plt.figure(figsize=(10, 10))
            self.ax = plt.gca()
        else:
            self.ax = ax

        self.ax.tick_params(left=False, bottom=False)
        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)
        self.ax.spines["bottom"].set_visible(False)
        self.ax.spines["left"].set_visible(False)

    def corr(self):
        """
        Plot the correlation matrix.
        """
        cvals = [-1, 0, 1]
        colors = ["tab:orange", "white", "tab:blue"]
        norm = plt.Normalize(min(cvals), max(cvals))
        tuples = list(zip(map(norm, cvals), colors))
        cmap = LinearSegmentedColormap.from_list("", tuples)
        mask = np.zeros_like(self.corr_mat)
        mask[np.triu_indices_from(mask, k=1)] = True
        mask = self.corr_mat * mask
        im = self.ax.imshow(mask, cmap=cmap, vmin=-1, vmax=1)
        for i in range(self.corr_mat.shape[0]):
            for j in range(self.corr_mat.shape[1]):
                if mask[j][i] != 0:
                    self.ax.annotate(
                        np.round(mask[j][i], 3),
                        xy=(i, j),
                        ha="center",
                        va="center",
                    )
        self.ax.set_title("Correlations")
        self.ax.set_xticks([i for i in range(mask.shape[0])])
        self.ax.set_yticks([i for i in range(mask.shape[1])])
        self.ax.set_xticklabels(self.labels_n)
        self.ax.set_yticklabels(self.labels_n)

    def get_orth_vec(self, vec, scale=1):
        """
        Computes an orthogonal vector of an input vector.
        Args:
            vec (numpy.ndarry): input vector
            scale (float): scales the orthogonal vector

        Returns:
            orth_vec (numpy.ndarray): scaled orthogonal vector
        """
        orth_vec = np.array([-vec[:, 1], vec[:, 0]]).T
        orth_vec = self.unit_length_vec(orth_vec)
        return orth_vec * scale

    def graph(self, layout, mode, col, labels_e, vs):
        """
        Plots a graph.
        Args:
            layout (list): list of coordinates of the nodes
            mode (string): 'directed' or 'undirected'
            col (matplotlib.colors): color of the nodes or a list of colors, which holds a color for each node
            labels_e (list): list of edge labels
            vs (float): size for the nodes
        """
        circle_radius = vs
        scale_a = -2
        scale_b = 2

        if layout is None:
            random.seed(123)
            G = ig.Graph.Adjacency(self.adj_mat)
            layout = np.array(G.layout("fr"))
        self.scale(layout, scale_a, scale_b)

        if mode == "directed":
            style = "Simple, tail_width=0.5, head_width=4, head_length=8"
        else:
            style = "Simple, tail_width=0.5, head_width=0"
            self.adj_mat = np.triu(self.adj_mat + self.adj_mat.T)

        kw = dict(arrowstyle=style, color="k")

        start, end = np.where(self.adj_mat != 0)
        # start = layout[start]
        # end = layout[end]

        edges = []
        for i in range(len(start)):
            s = start[i]
            e = end[i]
            if self.corr_mat.iloc[s, e] >= 0:
                c = "k"
            else:
                c = "red"
            edges.append(
                patches.FancyArrowPatch(
                    posA=(layout[s][0], layout[s][1]),
                    posB=(layout[e][0], layout[e][1]),
                    shrinkA=circle_radius * 200,  # 20,
                    shrinkB=circle_radius * 200,  # 20,
                    arrowstyle=style,
                    color=c,
                    # **kw
                )
            )
        for e in edges:
            self.ax.add_patch(e)

        for i, l in enumerate(layout):
            if type(col) == list:
                c = col[i]
            else:
                c = col

            n = patches.Circle(
                (l[0], l[1]),
                radius=circle_radius,
                color=c,
            )
            self.ax.add_patch(n)

        # nodes = [
        #     patches.Circle(
        #         (l[0], l[1]),
        #         radius=circle_radius,
        #         color=col,
        #     )
        #     for l in layout
        # ]
        # for n in nodes:
        #     self.ax.add_patch(n)

        for i in range(len(layout)):
            x, y = layout[i]
            self.ax.annotate(
                self.labels_n[i],
                xy=(x, y),
                ha="center",
                va="center",
                fontsize=15,
                fontweight="bold",
                color="lightgray",
            )

        if not (labels_e is None):
            true_edge = end - start
            perp_edge = self.get_orth_vec(true_edge, 0.1)
            edge_center_coords = start + true_edge * 0.5 + perp_edge
            for i in range(len(edge_center_coords)):
                x, y = edge_center_coords[i]
                self.ax.annotate(
                    labels_e[i],
                    xy=(x, y),
                    ha="center",
                    va="center",
                )

        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.set_xlim(scale_a - circle_radius - 0.05, scale_b + circle_radius + 0.05)
        self.ax.set_ylim(scale_a - circle_radius - 0.05, scale_b + circle_radius + 0.05)
        self.ax.set_aspect("equal")
        plt.tight_layout()

    def scale(self, layout, a, b):
        """
        Centers and rescale the layout coordinates for the nodes.

        Args:
            layout (numpy.ndarray): layout of the nodes
            a (float): lower bound for rescaling
            b (float): upper bound for rescaling
        """
        mean = layout.mean(axis=0)
        std = layout.std()
        for i in range(len(layout)):
            layout[i] = (layout[i] - mean) / std
        mi = layout.min()
        ma = layout.max()
        for i in range(len(layout)):
            for j in range(2):
                layout[i, j] = a + ((layout[i, j] - mi) * (b - a)) / (ma - mi)

    def unit_length_vec(self, vec):
        """
        Rescales a vector to unit length.
        Args:
            vec (numpy.ndarry): Input vector

        Returns:
            new_vec (numpy.ndarry): Unit length version of the input vector
        """
        new_vec = []
        for v in vec:
            mag = np.sqrt((v**2).sum())
            new_vec.append((v[0] / mag, v[1] / mag))
        return np.array(new_vec)


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt

    data = pd.read_csv("examples/decathlon.tab", sep="\t")
    dist = [100, 110, 400, 1500]

    for d in dist:
        data[str(d)] = d / data[str(d)] * 3.6
        data = data.rename(columns={"poid": "shot", "haut": "high", "perc": "pole"})

    graph = np.array(
        [
            [0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0],
            [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        ]
    )
    labels = data.columns
    c = data.corr("spearman")
    print(c)
    p = SnhaPlot(adj_mat=graph, corr=c, labels_n=labels)

    # c = ["blue", "red", "green", "orange", "gray", "tab:blue"]

    p.graph(None, "undirected", "tab:blue", None, 0.15)
    plt.show()
