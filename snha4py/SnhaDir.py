#! /usr/bin/env python3
import numpy as np
import pandas as pd
from snha4py.utils import np_in, chains2admat

"""
Direction analysis of the St. Nicolas House Algorithm.

Soon be updated. 
[Back to github](https://github.com/thake93/snha4py/)
"""


class SnhaDir:
    def __init__(self, snha):
        self.snha = snha
        self.xi = None
        self.pred_xi = None
        self.pred_logic = None

    def comp_xi(self):
        """
        Computes Xi correlation matrix for the Snha objects data.
        """
        data = self.snha.get_data()
        xi = np.zeros((data.shape[1], data.shape[1]))
        for i, r1 in enumerate(data):
            for j, r2 in enumerate(data):
                xi[i, j] = self.xi_corr(data[r1], data[r2])
        self.xi = pd.DataFrame(xi)

    def conn_nodes(self, chs, deg_mat):
        # nodes mit unterschiedlichen nachbarn
        """
        Finds nodes with different neighbors.

        Args:
            chs (list): list with chains from a SNHA object
            deg_mat (numpy.ndarray): degree matrix of a graph prediciton

        Returns:
            nodes (dictionary): nodes with different neighbors and its corresponing chain
        """
        nodes = {}
        for i in range(len(chs)):
            ch1 = chs[i]
            for n in ch1[1:-1]:
                for j in range(len(chs)):
                    if i == j:
                        continue
                    if n in chs[j][1:-1] and deg_mat[n, n] > 2:
                        if n in nodes.keys() and not chs[j] in nodes[n]:
                            nodes[n].append(chs[j])
                        else:
                            nodes[n] = [ch1, chs[j]]
        return nodes

    def deg_mat(self, mat):
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

    def dir_ind(self, nodes, corr):
        """
        Computes indication of direction based on chains intersecting in one node

        Args:
            nodes (dictionary): nodes with different neighbors and its corresponing chain
            corr (pandas.DataFrame): correlation matrix

        Returns:
            di_indic (list): list of tuple, which indicated the direction (e.g (a,b) a -> b)
        """
        idx = [(0, 0), (0, 1), (1, 0), (1, 1)]
        red = {}
        for k, v in nodes.items():
            red_chains = []
            for chain in v:
                (ik,) = np.where(chain == k)
                red_chains.append([chain[ik - 1], chain[ik + 1]])
            red[k] = red_chains

        dir_indic = []
        cent_2 = False
        for node, ch in red.items():
            max_c = 0
            for i in range(len(ch)):
                cur = ch[i]
                for j in range(i + 1, len(ch)):
                    comp = ch[j]
                    for k in range(4):
                        l, m = idx[k]
                        (ix,) = cur[l]
                        (iy,) = comp[m]
                        if ix != iy:
                            c = corr.iloc[ix, iy]
                            if abs(c) < 0.05:
                                cent_2 = True
                                if not ((ix, node) in dir_indic):
                                    dir_indic.append((ix, node))
                                if not ((iy, node) in dir_indic):
                                    dir_indic.append((iy, node))
                                break
                        elif abs(c) > max_c:
                            max_c = abs(c)
                            cont = (ix, iy)
            if not cent_2:
                dir_indic.append((node, cont[0]))
                dir_indic.append((node, cont[1]))
        return dir_indic

    def get_xi(self):
        """
        Get the Xi correlation matrix from the Snha object.

        Returns:
            xi (pandas.DataFrame): Xi correlation matrix
        """
        return self.xi

    def inf_dir(self, chains, dir_indic):
        """
        Rearange the chains based on direction indications and derive direction indication from changed chains

        Args.:
            chains (list): list of undirected chains of the Snha Object
            di_indic (list): list of tuple, which indicated the direction (e.g (a,b) a -> b)

        Returns:
            directed+temp (list): list of chains, each chain is now directed (e.g [a,b,c] a->b->c)
        """
        checked = []
        changed = []
        directed = []
        for di in dir_indic:
            for c in chains:
                (idx,) = np.where(c == di[0])
                if not (idx.size == 0):
                    (idx2,) = np.where(c == di[1])
                    if idx2.size == 0 or not (abs(idx2 - idx) == 1):
                        break
                    checked.append(c)
                    if not (idx2 > idx):
                        if np_in(c, changed):
                            print(f"{c} already changed")
                        changed.append(c)
                        c = c[::-1]
                    if not np_in(c, directed):
                        directed.append(c)

        temp = []

        for c in chains:
            found = False
            if np_in(c, checked):
                continue
            checked.append(c)
            for dc in directed:
                for i in range(0, dc.size - 1):
                    st = dc[i]
                    en = dc[i + 1]
                    (idx,) = np.where(c == st)
                    if not (idx.size == 0):
                        (idx2,) = np.where(c == en)
                        if idx2.size == 0 or not (abs(idx2 - idx) == 1):
                            continue
                        found = True
                        if not (idx2 > idx):
                            if np_in(c, changed):
                                print(f"{c} already changed")
                            changed.append(c)
                            c = c[::-1]
                        if not np_in(c, temp):
                            temp.append(c)
                        break
            if not found:
                if not np_in(c, temp):
                    temp.append(c)
                if not np_in(c[::-1], temp):
                    temp.append(c[::-1])

        return directed + temp

    def predict_dir(method="logic"):
        graph_pred = self.snha.get_graph_pred()
        if method == "logic":
            chains = self.snha.get_chains()
            corr = self.snha.get_corr()
            deg_mat = self.deg_mat(graph_pred)
            nodes = self.conn_nodes(chains, deg_mat)
            directions = self.dir_ind(nodes, corr)
            directed_chains = self.inf_dir(chains, directions)
            self.pred_logic = chains2admat(directed_chains)
        elif method == "xi":
            return
        return

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


if __name__ == "__main__":
    from snha4py.Snha import Snha

    d = pd.read_csv(
        f"/media/sf_Documents/Uni/data/MA/notebooks/eval_data/d_0284",
        header=None,
        skiprows=1,
        index_col=False,
    )
    s2 = Snha(d)
    s2.new_graph()
    s2.comp_corr()
    s2.st_nich_alg()
    ch = s2.get_chains()
    da = SnhaDir(d)
    dm = da.deg_mat(s2.get_graph_pred())
    print(dm)
    nodes = da.conn_nodes(ch, dm)
    print(nodes)
    di = da.dir_ind(nodes, s2.get_corr())
    print(di)
    dir_chains = da.inf_dir(ch, di)
    print(dir_chains)
