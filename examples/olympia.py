#! /usr/bin/env python3

from snha4py.Snha import Snha
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == "__main__":
    data = pd.read_csv("decathlon.tab", sep="\t")
    print(data.head())
    print(data.columns)

    # change the time into speed for the running distances 100, 400, 1500 and 110m hurdling
    dist = [100, 110, 400, 1500]
    for d in dist:
        data[str(d)] = d / data[str(d)]
    print(data.head())

    s = Snha(data=data)
    s.comp_corr(method="spearman")

    s.st_nich_alg()

    s.plot_graph()
    plt.show()
