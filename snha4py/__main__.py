#! /usr/bin/env python3

"""
The St. Nicolas House Algorithm comando line application.

Currently available functions are:

- the general algorithm with/ without bootstrap to predict a graph from data
- create correlated data based on a directed graph
- crete a directed graph

For further information and examples see [readme file](https://github.com/thake93/snha4py/tree/main/snha4py/readme.md).
"""

from snha4py.Snha import Snha
import argparse
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def create_data(args):
    """
    A wrapper to create data based on the arguments given by the parser.

    Argumenst:
        args (argparse.Namespace): Namespace object result from the comando line arguments
    """
    f = read_file(args.graph, True)
    if f is None:
        print(
            "Use a *.tab or *.csv file containing a adjacency matrix of a directed graph."
        )
        return
    f = f.to_numpy()
    s = Snha(graph=f)
    s.create_corr_data(
        n=args.iterations,
        steps=args.steps,
        mean=args.mean,
        sd=args.std,
        noise=args.noise,
        prop=args.prop,
    )
    data = s.get_data()
    if args.output is None:
        data.to_csv("temp.csv", sep=",", index=False)
        print(f"Correlated data saved in temp.csv")
    else:
        data.to_csv(args.output, sep=",", index=False)
        print(f"Correlated data saved in {args.output}")

    if args.plot:
        s.comp_corr()

        fig, ax = plt.subplots(1, 2, figsize=(10, 5))
        s.plot_graph(pred=False, ax=ax[0])
        s.plot_corr(ax=ax[1])
        plt.show()


def create_graph(args):
    """
    A wrapper to create a graph based on the arguments given by the parser.

    Argumenst:
        args (argparse.Namespace): Namespace object result from the comando line arguments
    """
    print("graph")
    s = Snha()
    s.new_graph(
        graph_type=args.graph_type,
        nodes=args.nodes,
        edges=args.edges,
        mode=args.mode,
        cont=args.cont,
    )
    g = s.get_graph()
    if args.output is None:
        np.savetxt("temp.csv", g, delimiter=",")
        print(f"Graph was saved in temp.csv")
    else:
        np.savetxt(f"{args.output}", g, delimiter=",", fmt="%.3f")
        print(f"Graph was saved to {args.output}.")

    if args.plot:
        s.plot_graph(pred=False)
        plt.show()


def read_file(f, graph):
    """
    Reads a file.

    Arguments:
        f (str): path to the file
        graph (boolean): True: reads the file without a header; False: reads the file with a header
    Returns:
        in_file (pandas.DataFrame): data or adjacency matrix
    """
    name, ext = os.path.splitext(f)
    if ext == ".csv":
        delimiter = ","
    elif ext == ".tab":
        delimiter = "\t"
    else:
        return
    if graph:
        in_file = pd.read_csv(f, delimiter=delimiter, header=None)
    else:
        in_file = pd.read_csv(f, delimiter=delimiter)
    return in_file


def snha(args):
    """
    A wrapper to run the St. Nicolas House algorithm based on the arguments given by the parser.

    Argumenst:
        args (argparse.Namespace): Namespace object result from the comando line arguments
    """
    f = read_file(args.data, False)
    if f is None:
        print("Use a *.tab or *.csv file containing a data to analyse.")
        return

    s = Snha(data=f)
    s.comp_corr(method=args.method)
    s.st_nich_alg(
        alpha=args.alpha,
        bt=args.bootstrap,
        n=args.iterations,
        lbd=args.lbd,
        method=args.method,
    )

    g = s.get_graph_pred()
    np.savetxt(f"{args.output}", g, delimiter=",", fmt="%.3f")
    print(f"Graph prediction was saved to {args.output}.")

    if args.plot:
        s.plot_graph()
        plt.show()


def main(parser):
    """
    Calls the desired function.

    Arguments:
        parser (argparse.ArgumentParser): holding information of the CLI input
    """
    args = parser.parse_args()
    if args.create_data:
        create_data(args)
    elif args.create_graph:
        create_graph(args)
    elif args.snha:
        snha(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="St. Nicolas House Alogrithm CLI",
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("--snha", action="store_true")
    parser.add_argument("-d", "--data", type=str)
    parser.add_argument("--alpha", type=float, default=0.1)
    parser.add_argument("--bootstrap", action="store_true")
    parser.add_argument("--lbd", type=float, default=0.5)
    parser.add_argument(
        "--method",
        type=str,
        choices=["pearson", "kendall", "spearman"],
        default="pearson",
    )

    parser.add_argument("--create-data", action="store_true")
    parser.add_argument("-g", "--graph")
    parser.add_argument("-s", "--steps", default=25, type=int)
    parser.add_argument("-i", "--iterations", default=200, type=int)
    parser.add_argument("--mean", default=100, type=float)
    parser.add_argument("--std", default=2, type=float)
    parser.add_argument("--noise", default=1, type=float)
    parser.add_argument("--prop", default=0.05, type=float)

    parser.add_argument("--create-graph", action="store_true")
    parser.add_argument(
        "-t",
        "--graph-type",
        type=str,
        choices=[
            "werner",
            "rnd_chain",
            "band",
            "circle",
            "hub",
            "random",
            "barabasi_m1",
            "barabasi_m2",
        ],
        default="werner",
    )
    parser.add_argument("-n", "--nodes", type=int, default=5)
    parser.add_argument(
        "-m", "--mode", type=str, choices=["directed", "undirected"], default="directed"
    )
    parser.add_argument("-e", "--edges", type=int, default=10)
    parser.add_argument("--cont", type=int, default=2)

    parser.add_argument("-p", "--plot", action="store_true")
    parser.add_argument("-o", "--output", type=str)

    main(parser)
