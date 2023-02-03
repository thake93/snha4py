#! /usr/bin/env python3

from snha4py.Snha import Snha
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":
    data = pd.read_csv("data/decathlon.tab", sep="\t")
    data = data.reset_index(drop=True)
    print(data.head())

    """
    Change the time into speed for the running distances 100, 400, 1500 and 110m 
    hurdling, to be comparable with the other events. Here, highest is best, 
    while for running events the lowest would be best.
    """
    dist = [100, 110, 400, 1500]
    for d in dist:
        data[str(d)] = d / data[str(d)]

    data = data.rename(columns={"poid": "shot", "haut": "high", "perc": "pole"})

    cols_re = [str(d) for d in dist]
    for c in data.columns:
        if not c in cols_re:
            cols_re.append(c)
    data = data[cols_re]
    print(data.head())

    s = Snha(data=data)
    s.comp_corr(method="spearman")
    s.st_nich_alg()
    s.plot_graph()
    plt.show()

    cols = 4 * ["tab:orange"] + 6 * ["tab:blue"]

    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    s.plot_graph(ax=ax[0], col=cols)
    s.plot_corr(ax=ax[1])
    plt.show()

    """
    Insert a random variable
    Now a column is shuffeld and appended again to the data set. 
    This variable is not correlated to the other variables due to shuffeling. 
    It appears in the graph as a node, which is not connected to the other nodes.
    """
    cols += ["red"]
    data["rnd"] = data["100"].sample(n=data.shape[0], ignore_index=True)
    s = Snha(data=data)
    s.comp_corr(method="spearman")
    s.st_nich_alg()
    s.plot_graph(col=cols)
    plt.show()
