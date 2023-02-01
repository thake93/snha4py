#! /usr/bin/env python3

from snha4py.Snha import Snha
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string

if __name__ == "__main__":
    graph = np.genfromtxt("werner.csv", delimiter=",")  # loading your graph

    s = Snha(graph=graph)  # initialize the Snha object with your graph

    """
    Instead of loading a graph stored in a csv file you could use the new_graph method to create a graph:
    
    s = Snha()
    s.new_graph() # see the API for further details
    
    or you could type your own graph
    graph = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 0]])

    s = Snha(graph=graph)
    s.plot_graph(pred=False)
    plt.show()
    """
    s.create_corr_data(  # create correlation data
        n=200,
        steps=25,
    )

    data = s.get_data()
    data.columns = list(string.ascii_uppercase[: graph.shape[0]])  # rename the columns
    data.to_csv("data.csv", index=False)  # save the data

    # plot the figure
    s.comp_corr()  # compute the correlation for the plot

    fig, ax = plt.subplots(1, 2, figsize=(14, 7))
    s.plot_graph(ax=ax[0], labels=data.columns, pred=False)
    s.plot_corr(ax=ax[1], labels=data.columns)
    plt.tight_layout()
    # plt.savefig("../examples/pics/g2d.png", dpi=120)
    plt.show()
