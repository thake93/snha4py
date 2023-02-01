<center>

[Introduction](../docs/__init__.md) -
[Snha](../docs/Snha.md) -
[SnhaDataGen](../docs/SnhaDataGen.md) -
[SnhaDir](../docs/SnhaDir.md) -
[SnhaNewGraph](../docs/SnhaNewGraph.md) -
[SnhaPlot](../docs/SnhaPlot.md) -
[CLI](../docs/__main__.md) -
[Usage](../snha4py/README.md) 

</center>

# Usage
Here, I present an in-depth explenation of 

1. [Analysing your data by graph prediction](#analysing-your-data-by-graph-prediction)
2. [Creating correlated data from a directed graph](#creating-correlated-data-from-a-directed-graph)

via the command-line interface (CLI) or within your python scirpt.

## Analysing your data by graph prediction
I demonstrate the useage of the tool on exemplary data from the 
[olympic decathlon of 1988](https://github.com/thake93/snha4py/blob/main/examples/data/decathlon.tab)
[(further information)](https://rdrr.io/cran/ade4/man/olympic.html).
The data set comprises the results of 33 Athletes competing in 1988 in the events:

- **running**: 100m, 400m, 1500m and 110m hurdles (seconds)
- **jumping**: long jump, high jump and pole vault (meter)
- **throwing**: javelin, discus, shot put (meter)

For demonstration reasons I add a random variable.

### Command-line interface
### In python script 
Using the tool within your script grants you the most flexibility. So, I recommend you to use it that way.


## Creating correlated data from a directed graph

Assume you want to create correlated data for a graph, which looks like this:
<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/werner.png" width="300" height="300">
</div>

**Note:** The adjacency martix for this graph is stored in [werner.csv](https://github.com/thake93/snha4py/blob/main/examples/data/werner.csv)  
We create correlated data along the edges of the graph, e.g. the data in column A would be correlated with data in column C.

### Command-line interface

The CLI of snha4py has the option --create-data, which creates correlated data based on a graph and stores it into a *.csv* file.
The terminal command is: 

```shell
python3 -m snha4py --create-data -g werner.csv -o data.csv -s 25 -i 200 -p
```
Lets have a closer look on the arguments.

- **-g | --graph**      - holds the path to the file containing the adjacency matrix
- **-o | --output**     - holds the path to the file containing the resulting data
- **-s | --steps**      - number of steps within the data generation process for further information see ([Novine et al. 2022](https://doi.org/10.52905/hbph2021.3.26))
- **-i | --iterations** - number of steps within the data generation process for further information see ([Novine et al. 2022](https://doi.org/10.52905/hbph2021.3.26://doi.org/10.52905/hbph2021.3.26)
- **-p | --plot**     - plots the resulting matrix of correlation coefficients, as well as the input graph.

### In python script

We start with initializing the Snha object with our desired graph.
```python
graph = np.genfromtxt("werner.csv", delimiter=",")  # loading your graph

s = Snha(graph=graph)  # initialize the Snha object with your graph
```

Instead of loading a graph stored in a csv file you could use the new_graph method to create a graph:

```python
s = Snha()
s.new_graph() # see the API for further details
```

or you could type your own graph
```python
graph = np.array([[0, 0, 1], [1, 0, 1], [0, 1, 0]])

s = Snha(graph=graph)
```
Now, we can create data, which correlates along the edges of the input graph:
```python
s.create_corr_data(  # create correlation data
    n=200,
    steps=25,
)

data = s.get_data()
data.columns = list(string.ascii_uppercase[: graph.shape[0]])  # rename the columns
data.to_csv("data.csv", index=False)  # save the data
```
Finally, we create a plot of the input graph and the resulting correlation matrix:
```python
s.comp_corr()  # compute the correlation for the plot

fig, ax = plt.subplots(1, 2, figsize=(14, 7))
s.plot_graph(ax=ax[0], labels=data.columns, pred=False)
s.plot_corr(ax=ax[1], labels=data.columns)
plt.tight_layout()
plt.show()
```

The code is also stored in a 
[python script](https://github.com/thake93/snha4py/blob/main/examples/graph2data.py)
, as well as in a 
[jupyter notebook](https://github.com/thake93/snha4py/blob/main/examples/graph2data.ipynb).

* * *
Both the python script and the terminal command leads to the file *data.csv* containing the data and showing the following figure:

<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/g2d.png">
</div>
