#! /usr/bin/env python3

"""
The St. Nicolas House algorithm for python.

The main module of the snha4py package. It can be used either in code or as a command line application. For further information and examples see the  [readme file](https://github.com/thake93/snha4py/tree/main/snha4py/readme.md).

"""

import pandas as pd
import numpy as np
from snha4py.SnhaNewGraph import SnhaNewGraph
from snha4py.SnhaPlot import SnhaPlot
from snha4py.SnhaDataGen import SnhaDataGen


class Snha:
    def __init__(self, data=None, graph=None):
        """
        Create an St. Nicolas House Object.

        Args:
            data (pandas.DataFrame): input data
            graph (numpy.array): adjacency matrix of a graph
        """
        self.data = data
        self.graph = graph
        self.graph_pred = None
        self.corr = None
        self.chains = []
        self.col_map = {}

    def chains2admat(self):
        """
        Converts association chains into an adjacency matrix.
        """
        g = np.zeros((self.data.shape[1], self.data.shape[1]))
        for ch in self.chains:
            for i in range(len(ch) - 1):
                g[ch[i], ch[i + 1]] = 1
        self.graph_pred = g

    def check_labels(self):
        """
        Checks for attributes and sets labels for the nodes.

        Returns:
            labels (list): list of labels for the nodes
        """
        if not (self.data is None):
            labels = list(self.data.columns)
        elif not (self.graph_pred is None):
            labels = range(self.graph_pred.shape[0])
        elif not (self.graph is None):
            labels = range(self.graph.shape[0])
        else:
            labels = []
        return labels

    def clean_sub_chains(self, chains):
        """
        Removes sub chains of the association chains.

        Args:
            chains (list): list of chains

        Returns:
            chains_clean (list): list of chains wihtout sub chains
        """
        chains_clean = []
        max_len = len(chains[0])
        for i in range(len(chains) - 1, -1, -1):
            f = False
            l = len(chains[i])
            for j in range(len(chains)):
                cur_check = chains[j]
                if l == max_len:
                    f = False
                    break
                for k in range(len(cur_check) - l + 1):
                    if chains[i] == cur_check[k : k + l] and not (len(cur_check) == l):
                        f = True
                        break
                if f:
                    break
            if not (f):
                chains_clean.append(chains[i])
        return chains_clean

    def comp_corr(self, df=None, method="pearson", in_place=True):
        """
        Computes the correlation matrix for the Snha objects data.

        Args:
            df (pandas.DataFrame): compute the correlation based on the data
            method (str):
                "pearson" (default): standard correlation coefficient
                "kendall": Kendall Tau correlation coefficient
                "spearman": Spearman rank correlation
            in_place (boolean):
                True (default): assigns self.corr the computed correlation
                False: returns the computed correlation instead

        Returns:
            Only if in_place=False: the computed correlation

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        s.comp_corr()

        cor = s.get_corr()
        print(cor)
        ```
        """
        if df is None:
            df = self.data
        if in_place:
            self.corr = df.corr(method=method)
        else:
            return df.corr(method=method)

    def conf_mat(self):
        """
        Computes the confusion matrix of the predicted and true edges of the graph.

        Returns:
            cmat (numpy.ndarray; shape: (2,2)): confusion matrix

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        s.comp_corr()
        s.st_nich_alg()

        cm = s.conf_mat()
        print(cm)
        ```
        """
        true = self.graph + self.graph.T

        pred = self.graph_pred + self.graph_pred.T
        cmat = np.zeros((2, 2))
        for i in range(true.shape[0]):
            for j in range(true.shape[1]):
                if true[i, j] != 0 and pred[i, j] != 0:
                    # TP
                    cmat[0, 0] += 1
                elif true[i, j] == 0 and pred[i, j] != 0:
                    # FP
                    cmat[1, 0] += 1
                elif true[i, j] != 0 and pred[i, j] == 0:
                    # FN
                    cmat[1, 1] += 1
                else:
                    # TN
                    cmat[0, 1] += 1

        return cmat / 2

    def create_corr_data(self, n=100, steps=15, mean=100, sd=2, noise=1, prop=0.05):
        """
        Create correlation data for the Snha objects graph.

        Args:
            n (int): the number of measurements per node, default: 100
            steps (int): the number of iterations, default: 15
            mean (float): mean value for sampling from a Gaussian distribution, default: 100
            sd (float): standard deviation for sampling from a Gaussian distribution, default: 2
            noise (float): standard deviation for sampling noise from a Gaussian distribution with mean 0 after each iteration, default: 1
            prop (float): proportion of the target node value take the source node, default: 0.05

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        data = s.get_data()
        print(data)
        ```
        """
        sdg = SnhaDataGen(
            graph=self.graph, n=n, steps=steps, mean=mean, sd=sd, noise=noise, prop=prop
        )
        self.data = sdg.get_data()

    def get_chains(self, rename=True):
        """
        Get the association chains extrected by the St. Nicholas Algorithm.

        Args:
            rename (boolean): default: True
                True: Chains of column names of the input data
                False: Chains of column index numbers

        Returns:
            chains (list): Association chains for the correlation data
        """
        if rename:
            col_map_rev = {y: x for x, y in self.col_map.items()}
            new_names = [[col_map_rev[i] for i in l] for l in self.chains]
            return new_names
        else:
            return self.chains

    def get_corr(self):
        """
        Get the correlation data from the Snha object.

        Returns:
            corr (pandas.DataFrame): Correlation matrix of the Snha obejct
        """
        return self.corr

    def get_data(self):
        """
        Get the data from the Snha object.

        Returns:
            data (pandas.DataFrame): DataFrame with m observations for n variables
        """
        return self.data

    def get_graph(self):
        """
        Get the graph from the Snha object.

        Returns:
            graph (numpy.ndarray): adjacency matrix from the Snha object
        """
        return self.graph

    def get_graph_pred(self):
        """
        Get the graph predicten from the Snha object.

        Returns:
            graph_pred (numpy.ndarray): adjacency matrix from the predicted graph
        """
        return self.graph_pred

    def graph_stats(self):
        """
        Computes the accuracy, sensitivity, specificity, BCR (Balanced Classification Rate) and MCC (Matthews Correlation Coefficient).

        Returns:
            stats (dictionary): dictionary containing the statistics

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        s.comp_corr()
        s.st_nich_alg()

        stats = s.graph_stats()
        print(stats)
        ```
        """
        cmat = self.conf_mat()
        stats = {}
        TP, TN, FP, FN = cmat[0, 0], cmat[0, 1], cmat[1, 0], cmat[1, 1]

        stats["Accuracy"] = (TP + TN) / (TP + TN + FP + FN)
        stats["Sensitivity"] = TP / (TP + FN)
        stats["Specificity"] = TN / (TN + FP)
        stats["BCR"] = (stats["Sensitivity"] + stats["Specificity"]) / 2
        stats["MCC"] = (TP * TN - FP * FN) / (
            np.sqrt((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN))
        )
        return stats

    def middle_chains(self, nodes, df):
        """
        Extracts the middle chains of resulting from the correlation data.

        Args:
            nodes (list): list of nodes
            df (pandas.DataFrame): matrix of squared correlation coeficients

        Returns:
            fchain (list): middle chains of a list of nodes
        """
        nodes.reverse()
        for fi in range(1, len(nodes) - 1):
            fl = nodes[fi]
            for si in range(fi + 1, len(nodes)):
                sl = nodes[si]
                df_sort = (
                    df[[fl, sl]].iloc[nodes].sort_values(by=sl, key=lambda x: np.abs(x))
                )
                schain = df_sort.index.to_list()
                df_sort = (
                    df[[fl, sl]].iloc[nodes].sort_values(by=fl, key=lambda x: np.abs(x))
                )
                fchain = df_sort.index.to_list()
                fchain.reverse()
                if fchain == schain:
                    nodes.reverse()
                    return fchain
        nodes.reverse()

    def new_graph(self, graph_type="werner", nodes=5, edges=8, mode="directed", cont=2):
        """
        Creates a new graph for the Snha object.

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

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        graph = s.get_graph()
        print(graph)
        ```
        """
        g = SnhaNewGraph(
            graph_type=graph_type, nodes=nodes, edges=edges, mode=mode, cont=cont
        )
        self.graph = g.get_graph()

    def plot_corr(self, labels=None, ax=None):
        """
        Plots the correlation matrix of the Snha data.

        Args:
            labels (list): labels for the nodes of the graph
            ax (matplotlib.axes): axes to plot the graph on

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        s.comp_corr()

        s.plot_corr()
        ```
        """
        if labels is None:
            labels = self.check_labels()

        p = SnhaPlot(adj_mat=None, corr=self.corr, labels_n=labels, ax=ax)
        p.corr()

    def plot_graph(
        self,
        layout=None,
        mode="directed",
        col="tab:blue",
        labels=None,
        labels_e=None,
        pred=True,
        ax=None,
        vs=0.15,
    ):
        """
        Plots the graph of the Snha Object.

        Args:
            labels (list): labels for the nodes of the graph
            target (matplotlib.axes): axes to plot the graph on
            pred (boolean):
                True (default): Plot the determined association chains
                False: Plot the edges from the adjacency matrix
            vs (float): vertrex size; default: 25

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        s.comp_corr()
        s.st_nich_alg()

        stats = s.graph_stats()
        print(stats)
        ```
        """
        if labels is None:
            labels = self.check_labels()

        if pred:
            p = SnhaPlot(
                adj_mat=self.graph_pred, corr=self.corr, labels_n=labels, ax=ax
            )
            mode = "undir"
        else:
            p = SnhaPlot(
                adj_mat=self.graph_pred, corr=self.corr, labels_n=labels, ax=ax
            )

        p.graph(layout=layout, mode=mode, col=col, labels_e=labels_e, vs=vs)

    def set_corr(self, c_data):
        """
        Set the correlation data for the Snha object.

        Args:
            c_data (pandas.DataFrame): Correlation matrix
        """
        self.corr = c_data

    def set_data(self, data):
        """
        Set the data for the Snha object.

        Args:
            data (pandas.DataFrame): DataFrame with m observations for n variables
        """
        self.data = data

    def set_graph(self, graph):
        """
        Set the graph for the Snha object.

        Args:
            graph (numpy.ndarray): adjacency matrix
        """
        self.graph = graph

    def set_graph_pred(self, graph):
        """
        Set the graph prediction for the Snha object.

        Args:
            graph (numpy.ndarray): adjacency matrix
        """
        self.graph_pred = graph

    def snha(self, df, alpha):
        """
        Extracts the association chains resulting from the correlation data.

        Args:
            df (pandas.DataFrame): correlation matrix
            alpha (float, [0,1]): correlation coefficient cut off
        """
        chains = []

        # df = self.corr**2
        self.col_map = {col: i for i, col in enumerate(df.columns)}
        df = df.rename(index=self.col_map, columns=self.col_map)
        for idx, col in df.items():
            col_sort = col.sort_values(key=lambda x: np.abs(x), ascending=True)
            if len(df) > 10:
                pos_ends = col_sort.index.to_list()[-11:]
            else:
                pos_ends = col_sort.index.to_list()
            while len(pos_ends) >= 3:
                i = pos_ends[0]
                if i == idx:
                    break
                temp_df = df[[idx, i]].iloc[pos_ends]
                s = temp_df.sort_values(by=i, key=lambda x: np.abs(x))
                nodes_sorted = s.index.to_list()
                if s[i].iloc[0] < alpha:
                    pos_ends.pop(0)
                    continue
                if pos_ends == nodes_sorted[::-1]:
                    if not (nodes_sorted in chains) and not (
                        nodes_sorted[::-1] in chains
                    ):
                        chains.append(nodes_sorted)
                        break
                else:
                    mc = self.middle_chains(pos_ends, df)
                    if mc and (not (mc in chains) and not (mc[::-1] in chains)):
                        chains.append(mc)
                        break
                pos_ends.pop(0)
        if len(chains) > 0:
            self.chains = self.clean_sub_chains(chains)
        self.chains2admat()

    def snha_bt(self, df, alpha, n, lbd, method):
        """
        Applying the St Nicholas algorithm within a bootstrapp routine.

        Args:
            df (pandas.DataFrame): Input data
            alpha (float, [0,1]): correlation coefficient cut off
            n (int): number of bootstrap iterations
            lbd (float, [0,1]): fraction of all iterations to accept an edge as a prediction (e.g. 50/100 iterations an edge need to be found, to be considered as a predicted edge at lbd=0.5 and n=100)
            method (str):
                "pearson" (default): standard correlation coefficient
                "kendall": Kendall Tau correlation coefficient
                "spearman": Spearman rank correlation
        """
        predictions = []
        samples = [df.sample(len(df), replace=True) for i in range(n)]
        for i, smpl in enumerate(samples):
            c = self.comp_corr(df=smpl, in_place=False, method=method)
            self.snha(c**2, alpha)
            predictions.append(self.graph_pred)

        edges = []
        for p in predictions:
            a = np.where(p == 1)
            edges += list(zip(a[0], a[1]))

        edge_count = {}
        for e in edges:
            if e in edge_count or e[::-1] in edge_count:
                try:
                    edge_count[e] += 1
                except:
                    edge_count[e[::-1]] += 1
            else:
                edge_count[e] = 1

        self.comp_corr(method=method)
        self.snha(self.corr**2, alpha)
        for k, v in edge_count.items():
            if v >= 2 * n * lbd:
                x, y = k
                self.graph_pred[x, y] = 1
                self.graph_pred[y, x] = 1

    def st_nich_alg(
        self, data=None, alpha=0.1, bt=False, n=100, lbd=0.5, method="pearson"
    ):
        """
        Selection to use the St. Nicholaus algorithm with or without bootstrapping.

        Args:
            data (pandas.DataFrame):
                bt=True: Input data
                bt=False: Correlation matrix
            alpha (float, [0,1]): correlation coefficient cut off; default: 0.1
            bt (boolean): Bootstrap True/Flase; default: False
            n (int): number of bootstrap iterations; default: 100
            lbd (float, [0,1]): fraction of all iterations to accept an edge as a prediction; default: 0.5 (e.g. 50/100 iterations an edge need to be found, to be considered as a predicted edge at lbd=0.5 and n=100)
            method (string):
                "pearson" (default): standard correlation coefficient
                "kendall": Kendall Tau correlation coefficient
                "spearman": Spearman rank correlation

        Examples:

        ```{.py}
        from snha4py.Snha import Snha

        s = Snha()
        s.new_graph()
        s.create_corr_data(n=200, steps=25)
        s.comp_corr()
        s.st_nich_alg()

        chains = s.get_chains()
        graph_pred = s.get_graph_pred()

        print(chains)
        print(graph_pred)
        ```
        """
        if bt:
            if data is None:
                data = self.data
            self.snha_bt(data, alpha**2, n, lbd, method)
        else:
            if data is None:
                data = self.corr
            self.snha(data**2, alpha**2)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    s = Snha()
    s.new_graph()
    s.create_corr_data(
        n=200,
        steps=25,
        mean=100,
        sd=2,
        noise=1,
        prop=0.05,
    )
    s.comp_corr()
    s.st_nich_alg()
    s.data.columns = ["A", "B", "C", "D", "E", "F"]
    s.plot_graph(pred=False)
    s.plot_graph()
    s.plot_corr()
    plt.show()
