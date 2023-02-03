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

<!-- markdownlint-disable -->

<a href="../snha4py/Snha.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Snha.py`
The St. Nicolas House algorithm for python. 

The main module of the snha4py package. It can be used either in code or as a command line application. For further information and examples see the  [readme file](https://github.com/thake93/snha4py/tree/main/snha4py/README.md).  [Back to github](https://github.com/thake93/snha4py/) 



---

## <kbd>class</kbd> `Snha`




<a href="../snha4py/Snha.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(data=None, graph=None)
```

Create an St. Nicolas House Object. 



**Args:**
 
 - <b>`data`</b> (pandas.DataFrame):  input data 
 - <b>`graph`</b> (numpy.array):  adjacency matrix of a graph 




---

<a href="../snha4py/Snha.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `chains2admat`

```python
chains2admat()
```

Converts association chains into an adjacency matrix. 

---

<a href="../snha4py/Snha.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `check_labels`

```python
check_labels()
```

Checks for attributes and sets labels for the nodes. 



**Returns:**
 
 - <b>`labels`</b> (list):  list of labels for the nodes 

---

<a href="../snha4py/Snha.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `clean_sub_chains`

```python
clean_sub_chains(chains)
```

Removes sub chains of the association chains. 



**Args:**
 
 - <b>`chains`</b> (list):  list of chains 



**Returns:**
 
 - <b>`chains_clean`</b> (list):  list of chains wihtout sub chains 

---

<a href="../snha4py/Snha.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `comp_corr`

```python
comp_corr(df=None, method='pearson', in_place=True)
```

Computes the correlation matrix for the Snha objects data. 



**Args:**
 
 - <b>`df`</b> (pandas.DataFrame):  compute the correlation based on the data 
 - <b>`method`</b> (str):  choice of ["pearson" : standard correlation coefficient, "kendall": Kendall Tau correlation coefficient, "spearman": Spearman rank correlation] 
 - <b>`in_place`</b> (boolean):  True : assigns self.corr the computed correlation; False: returns the computed correlation instead 



**Returns:**
 
 - <b>`Only if in_place=False`</b>:  the computed correlation 



**Examples:**
 

```{.py}
from snha4py.Snha import Snha

s = Snha()
s.new_graph()
s.create_corr_data(n=200, steps=25)
s.comp_corr()

cor = s.get_corr()
print(cor)
``` 

---

<a href="../snha4py/Snha.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `conf_mat`

```python
conf_mat()
```

Computes the confusion matrix of the predicted and true edges of the graph. 



**Returns:**
 
 - <b>`cmat`</b> (numpy.ndarray; shape: (2,2)):  confusion matrix 



**Examples:**
 

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

---

<a href="../snha4py/Snha.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create_corr_data`

```python
create_corr_data(n=100, steps=15, mean=100, sd=2, noise=1, prop=0.05)
```

Create correlation data for the Snha objects graph. 



**Args:**
 
 - <b>`n`</b> (int):  the number of measurements per node 
 - <b>`steps`</b> (int):  the number of iterations 
 - <b>`mean`</b> (float):  mean value for sampling from a Gaussian distribution 
 - <b>`sd`</b> (float):  standard deviation for sampling from a Gaussian distribution 
 - <b>`noise`</b> (float):  standard deviation for sampling noise from a Gaussian distribution with mean 0 after each iteration 
 - <b>`prop`</b> (float):  proportion of the target node value take the source node 



**Examples:**
 

```{.py}
from snha4py.Snha import Snha

s = Snha()
s.new_graph()
s.create_corr_data(n=200, steps=25)
data = s.get_data()
print(data)
``` 

---

<a href="../snha4py/Snha.py#L196"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_chains`

```python
get_chains(rename=True)
```

Get the association chains extrected by the St. Nicholas Algorithm. 



**Args:**
 
 - <b>`rename`</b> (boolean):  True: Chains of column names of the input data; False: Chains of column index numbers 



**Returns:**
 
 - <b>`chains`</b> (list):  Association chains for the correlation data 

---

<a href="../snha4py/Snha.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_corr`

```python
get_corr()
```

Get the correlation data from the Snha object. 



**Returns:**
 
 - <b>`corr`</b> (pandas.DataFrame):  Correlation matrix of the Snha obejct 

---

<a href="../snha4py/Snha.py#L222"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_data`

```python
get_data()
```

Get the data from the Snha object. 



**Returns:**
 
 - <b>`data`</b> (pandas.DataFrame):  DataFrame with m observations for n variables 

---

<a href="../snha4py/Snha.py#L231"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_graph`

```python
get_graph()
```

Get the graph from the Snha object. 



**Returns:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacency matrix from the Snha object 

---

<a href="../snha4py/Snha.py#L240"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_graph_pred`

```python
get_graph_pred()
```

Get the graph predicten from the Snha object. 



**Returns:**
 
 - <b>`graph_pred`</b> (numpy.ndarray):  adjacency matrix from the predicted graph 

---

<a href="../snha4py/Snha.py#L249"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_p_values`

```python
get_p_values()
```

Get the p-value matrix with p-values of all edges before the p-value filtering was applied. 



**Returns:**
 
 - <b>`p_val`</b> (numpy.ndarray):  matrix of p-values 

---

<a href="../snha4py/Snha.py#L258"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `graph_stats`

```python
graph_stats()
```

Computes the accuracy, sensitivity, specificity, BCR (Balanced Classification Rate) and MCC (Matthews Correlation Coefficient). 



**Returns:**
 
 - <b>`stats`</b> (dictionary):  dictionary containing the statistics 



**Examples:**
 

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

---

<a href="../snha4py/Snha.py#L293"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `middle_chains`

```python
middle_chains(nodes, df)
```

Extracts the middle chains of resulting from the correlation data. 



**Args:**
 
 - <b>`nodes`</b> (list):  list of nodes 
 - <b>`df`</b> (pandas.DataFrame):  matrix of squared correlation coeficients 



**Returns:**
 
 - <b>`fchain`</b> (list):  middle chains of a list of nodes 

---

<a href="../snha4py/Snha.py#L323"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `new_graph`

```python
new_graph(graph_type='werner', nodes=5, edges=8, mode='directed', cont=2)
```

Creates a new graph for the Snha object. 



**Args:**
 
 - <b>`graph_type`</b> (str):  type of the graph; choice of ["werner", "rnd_chain", "band", "circle", "hub", "random", "barabasi_m1", "barabasi_m2"] 
 - <b>`nodes`</b> (int):  number of nodes in the graph 
 - <b>`edges`</b> (int):  number of edges in the graph 
 - <b>`mode`</b> (str):  "directed": directed graph; "undirected": undirected graph 
 - <b>`cont`</b> (int):  number of signal seeds (only for graph type rndChain) 



**Examples:**
 

```{.py}
from snha4py.Snha import Snha

s = Snha()
s.new_graph()
graph = s.get_graph()
print(graph)
``` 

---

<a href="../snha4py/Snha.py#L425"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `p_value_filter`

```python
p_value_filter(thrsh)
```

Eliminates edges which are not significant based on a p-value estimate and a threshold. 



**Args:**
 
 - <b>`thrsh`</b> (float):  threshold for the p-value 

---

<a href="../snha4py/Snha.py#L350"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `plot_corr`

```python
plot_corr(labels=None, ax=None)
```

Plots the correlation matrix of the Snha data. 



**Args:**
 
 - <b>`labels`</b> (list):  labels for the nodes of the graph 
 - <b>`ax`</b> (matplotlib.axes):  axes to plot the graph on 



**Examples:**
 

```{.py}
from snha4py.Snha import Snha

s = Snha()
s.new_graph()
s.create_corr_data(n=200, steps=25)
s.comp_corr()

s.plot_corr()
``` 

---

<a href="../snha4py/Snha.py#L377"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `plot_graph`

```python
plot_graph(
    layout=None,
    mode='directed',
    col='tab:blue',
    labels=None,
    labels_e=None,
    pred=True,
    ax=None,
    vs=0.15
)
```

Plots the graph of the Snha Object. 



**Args:**
 
 - <b>`labels`</b> (list):  labels for the nodes of the graph 
 - <b>`target`</b> (matplotlib.axes):  axes to plot the graph on 
 - <b>`pred`</b> (boolean):  True: Plot the determined association chains; False: Plot the edges from the adjacency matrix 
 - <b>`vs`</b> (float):  vertrex size 



**Examples:**
 

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

---

<a href="../snha4py/Snha.py#L451"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_corr`

```python
set_corr(c_data)
```

Set the correlation data for the Snha object. 



**Args:**
 
 - <b>`c_data`</b> (pandas.DataFrame):  Correlation matrix 

---

<a href="../snha4py/Snha.py#L460"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_data`

```python
set_data(data)
```

Set the data for the Snha object. 



**Args:**
 
 - <b>`data`</b> (pandas.DataFrame):  DataFrame with m observations for n variables 

---

<a href="../snha4py/Snha.py#L469"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_graph`

```python
set_graph(graph)
```

Set the graph for the Snha object. 



**Args:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacency matrix 

---

<a href="../snha4py/Snha.py#L478"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_graph_pred`

```python
set_graph_pred(graph)
```

Set the graph prediction for the Snha object. 



**Args:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacency matrix 

---

<a href="../snha4py/Snha.py#L487"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `snha`

```python
snha(df, alpha)
```

Extracts the association chains resulting from the correlation data. 



**Args:**
 
 - <b>`df`</b> (pandas.DataFrame):  correlation matrix 
 - <b>`alpha`</b> (float, [0,1]):  correlation coefficient cut off 

---

<a href="../snha4py/Snha.py#L532"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `snha_bt`

```python
snha_bt(df, alpha, n, lbd, method)
```

Applying the St Nicholas algorithm within a bootstrapp routine. 



**Args:**
 
 - <b>`df`</b> (pandas.DataFrame):  Input data 
 - <b>`alpha`</b> (float, [0,1]):  correlation coefficient cut off 
 - <b>`n`</b> (int):  number of bootstrap iterations 
 - <b>`lbd`</b> (float, [0,1]):  fraction of all iterations to accept an edge as a prediction (e.g. 50/100 iterations an edge need to be found, to be considered as a predicted edge at lbd=0.5 and n=100) 
 - <b>`method`</b> (str):  choice of ["pearson": standard correlation coefficient, "kendall": Kendall Tau correlation coefficient, "spearman": Spearman rank correlation] 

---

<a href="../snha4py/Snha.py#L573"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `st_nich_alg`

```python
st_nich_alg(
    data=None,
    alpha=0.1,
    bt=False,
    n=20,
    lbd=0.5,
    method='pearson',
    p_cut=0.05
)
```

Selection to use the St. Nicholaus algorithm with or without bootstrapping. 



**Args:**
 
 - <b>`data`</b> (pandas.DataFrame):  bt=True: Input data; bt=False: Correlation matrix 
 - <b>`alpha`</b> (float, [0,1]):  correlation coefficient cut off 
 - <b>`bt`</b> (boolean):  Bootstrap True/Flase 
 - <b>`n`</b> (int):  number of bootstrap iterations 
 - <b>`lbd`</b> (float, [0,1]):  fraction of all iterations to accept an edge as a prediction (e.g. 50/100 iterations an edge need to be found, to be considered as a predicted edge at lbd=0.5 and n=100) 
 - <b>`method`</b> (string):  choice of ["pearson" : standard correlation coefficient, "kendall": Kendall Tau correlation coefficient, "spearman": Spearman rank correlation] 
 - <b>`p_cut`</b> (float):  p-value threshold to identify significant edges 



**Examples:**
 

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




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
