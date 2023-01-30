#! /usr/bin/env python3

from snha4py.Snha import Snha
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":
    data = pd.read_csv("decathlon.tab", sep="\t")
    print(data.head())
    print(data.columns)

    """
    Change the time into speed for the running distances 100, 400, 1500 and 110m 
    hurdling, to be comparable with the other events. Here, highest is best, 
    while for running events the lowest would be best.
    """
    data = pd.read_csv("decathlon.tab", sep="\t")
    dist = [100, 110, 400, 1500]

    for d in dist:
        data[str(d)] = d / data[str(d)] * 3.6

    data = data.rename(columns={"poid": "shot", "haut": "high", "perc": "pole"})

    cols_re = [str(d) for d in dist]
    for c in data.columns:
        if not c in cols_re:
            cols_re.append(c)
    data = data[cols_re]

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
