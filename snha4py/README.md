# Usage
Here, I present an in-depth explenation of 

1. [Analysing your data by graph prediction](#analysing-your-data-by-graph-prediction)
2. [Creating correlated data from a directed graph](#creating-correlated-data-from-a-directed-graph)

via the command-line interface (CLI) or within your Python scirpt.

## Analysing your data by graph prediction
I demonstrate the useage of the tool on exemplary data from the 
[olympic decathlon of 1988](https://github.com/thake93/snha4py/blob/main/examples/data/decathlon.tab)
[(further information)](https://rdrr.io/cran/ade4/man/olympic.html).
The data set comprises the results of 33 Athletes competing in 1988 in the events:

- **running**: 100m, 400m, 1500m and 110m hurdles (seconds)
- **jumping**: long jump, high jump and pole vault (meter)
- **throwing**: javelin, discus, shot put (meter)

Note, that the running events are measured in seconds. 
For these events lowests is best, while for all other events highest is best. 
In order to follow the same reasoning, we turn the time into speed.

Also, I will add a random variable to the data set to highlight the edge prediction.

### Command-line interface
First, we change the time of the running events into speed and add a random variable.
The code below will do the task, or you can get the preprocessed data set
[here](https://github.com/thake93/snha4py/blob/main/examples/data/decathlon_pre.csv).
* * *

```shell
python3
```

```python
import pandas as pd

data = pd.read_csv("decathlon.tab", delimiter="\t")
data = data.reset_index(drop=True)
data = data.rename(columns={"poid":"shot", "haut":"high", "perc":"pole"})

dist = [100,110,400,1500]
for d in dist:
    data[str(d)] = d/data[str(d)]

data["rnd"] = data["100"].sample(n=data.shape[0], ignore_index=True)
data.to_csv("decathlon_pre.csv", index=False)
```
* * *

Now, we can analyse the preprocessed data with:
```shell
python3 -m snha4py --snha -d decathlon_pre.csv --method spearman -o decathlon_pred.csv -p
```
Lets have a closer look on the arguments.

- **--snha**      - calls the St. Nicolas House algorithm
- **-d | --data**     - holds the path to the file containing the input data
- **--method**      - choose the method to compute the correlation
- **-o | --output**     - holds the path to the file containing the resulting graph prediction
- **-p | --plot**     - plots the resulting matrix of correlation coefficients, as well as the input graph.

**Note:** We just used the default argumntes for the St. Nicolas House algorithm.
For your analysis you might want to play around with different sets of arguments.  
See the 
[argument details](#st-nicolas-house-arguments)
 here.
### In Python script 
Using the tool within your script grants you the most flexibility. 
So, I recommend you to use it that way.  
We start with importing required packages:
```python
from snha4py.Snha import Snha
import matplotlib.pyplot as plt
import pandas as pd
```
Next we load the data and we initialize the Snha object with the loaded data.
For space reasons I directly load the preprocessed data.
In the 
[Python file](https://github.com/thake93/snha4py/blob/main/examples/olympia.py)
and the
[jupyter notebook](https://github.com/thake93/snha4py/blob/main/examples/olympia.ipynb)
the preprocessing steps are included.

```python
data = pd.read_csv('decathlon_pre.csv')

s = Snha(data=data) 
```

Afterwards, we compute the correlation and run the algorithm:
```python
s.comp_corr(method='spearman')
s.st_nich_alg()
```
Finally, we plot the graph prediction: 
```python
s.plot_graph()
plt.show()
```
Till here the CLI and the script yield the same result, but we can also improve the plotting to reach figures similar to those on the right.

```python
cols = 4*['tab:orange']+6*['tab:blue']+['red']

fig, ax = plt.subplots(1,2,figsize=(20,10))
s.plot_graph(ax=ax[0],col=cols)
s.plot_corr(ax=ax[1])
plt.show()
```
<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/d2g.png">
</div>

You can get the code as a 
[Python script](https://github.com/thake93/snha4py/blob/main/examples/olympia.py)
or as a 
[jupyter notebook](https://github.com/thake93/snha4py/blob/main/examples/olympia.ipynb)

### St. Nicolas House arguments
```python
st_nich_alg(alpha=0.1, bt=False, n=20, lbd=0.5, method='pearson', p_cut=0.05)
```
- **alpha**      - Correlation coefficient cut of
- **bt**     - Use bootstrap
- **n**      - Number of bootstrap iterations
- **lbd**     - fraction of all iterations to accept an edge as a prediction
- **method**     - method to compute the correlation coefficient within the bootstrap iterations
- **p_cut**     - p-value threshold to identify significant edges 


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

### In Python script
We start with importing required packages:
```python
from snha4py.Snha import Snha
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
```
Next, we initialize the Snha object with our desired graph.
```python
graph = np.genfromtxt("werner.csv", delimiter=",")  # loading your graph

s = Snha(graph=graph)  # initialize the Snha object with your graph
```

Instead of loading a graph stored in a csv file you could use the new_graph method to create a graph:

```python
s = Snha()
s.new_graph() # see the API for further details
```
* * *
Here are four examples of different graph types.

<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/graphs.png">
</div>
You can call the method with the arguments:

```python
s.new_graph(graph_type='werner', nodes=5, edges=8, mode='directed', cont=2)
```
[Argument details](https://github.com/thake93/snha4py/blob/main/docs/Snha.md#function-new_graph)
* * *
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
[Python script](https://github.com/thake93/snha4py/blob/main/examples/graph2data.py)
, as well as in a 
[jupyter notebook](https://github.com/thake93/snha4py/blob/main/examples/graph2data.ipynb).

* * *
Both the Python script and the terminal command leads to the file *data.csv* containing the data and showing the following figure:

<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/g2d.png">
</div>
