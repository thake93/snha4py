<center>

[Introduction](__init__.md) -
[Snha](Snha.md) -
[SnhaDataGen](SnhaDataGen.md) -
[SnhaDir](SnhaDir.md) -
[SnhaNewGraph](SnhaNewGraph.md) -
[SnhaPlot](SnhaPlot.md) -
[CLI](__main__.md) -
[Usage](README.md) 

</center>

<!-- markdownlint-disable -->

<a href="../snha4py/Snha.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `Snha.py`
The St. Nicolas House algorithm for python. 

The main module of the snha4py package. It can be used either in code or as a command line application. For further information and examples see the  [readme file](https://github.com/thake93/snha4py/tree/main/snha4py/README.md). 



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

<a href="../snha4py/Snha.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `chains2admat`

```python
chains2admat()
```

Converts association chains into an adjacency matrix. 

---

<a href="../snha4py/Snha.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `check_labels`

```python
check_labels()
```

Checks for attributes and sets labels for the nodes. 



**Returns:**
 
 - <b>`labels`</b> (list):  list of labels for the nodes 

---

<a href="../snha4py/Snha.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../snha4py/Snha.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `comp_corr`

```python
comp_corr(df=None, method='pearson', in_place=True)
```

Computes the correlation matrix for the Snha objects data. 



**Args:**
 
 - <b>`df`</b> (pandas.DataFrame):  compute the correlation based on the data method (str): 
 - <b>`"pearson" (default)`</b>:  standard correlation coefficient 
 - <b>`"kendall"`</b>:  Kendall Tau correlation coefficient 
 - <b>`"spearman"`</b>:  Spearman rank correlation in_place (boolean): 
 - <b>`True`</b> (default):  assigns self.corr the computed correlation 
 - <b>`False`</b>:  returns the computed correlation instead 



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

<a href="../snha4py/Snha.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../snha4py/Snha.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create_corr_data`

```python
create_corr_data(n=100, steps=15, mean=100, sd=2, noise=1, prop=0.05)
```

Create correlation data for the Snha objects graph. 



**Args:**
 
 - <b>`n`</b> (int):  the number of measurements per node, default: 100 
 - <b>`steps`</b> (int):  the number of iterations, default: 15 
 - <b>`mean`</b> (float):  mean value for sampling from a Gaussian distribution, default: 100 
 - <b>`sd`</b> (float):  standard deviation for sampling from a Gaussian distribution, default: 2 
 - <b>`noise`</b> (float):  standard deviation for sampling noise from a Gaussian distribution with mean 0 after each iteration, default: 1 
 - <b>`prop`</b> (float):  proportion of the target node value take the source node, default: 0.05 



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

<a href="../snha4py/Snha.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_chains`

```python
get_chains(rename=True)
```

Get the association chains extrected by the St. Nicholas Algorithm. 



**Args:**
 
 - <b>`rename`</b> (boolean):  default: True 
 - <b>`True`</b>:  Chains of column names of the input data 
 - <b>`False`</b>:  Chains of column index numbers 



**Returns:**
 
 - <b>`chains`</b> (list):  Association chains for the correlation data 

---

<a href="../snha4py/Snha.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_corr`

```python
get_corr()
```

Get the correlation data from the Snha object. 



**Returns:**
 
 - <b>`corr`</b> (pandas.DataFrame):  Correlation matrix of the Snha obejct 

---

<a href="../snha4py/Snha.py#L228"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_data`

```python
get_data()
```

Get the data from the Snha object. 



**Returns:**
 
 - <b>`data`</b> (pandas.DataFrame):  DataFrame with m observations for n variables 

---

<a href="../snha4py/Snha.py#L237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_graph`

```python
get_graph()
```

Get the graph from the Snha object. 



**Returns:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacency matrix from the Snha object 

---

<a href="../snha4py/Snha.py#L246"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_graph_pred`

```python
get_graph_pred()
```

Get the graph predicten from the Snha object. 



**Returns:**
 
 - <b>`graph_pred`</b> (numpy.ndarray):  adjacency matrix from the predicted graph 

---

<a href="../snha4py/Snha.py#L255"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../snha4py/Snha.py#L290"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../snha4py/Snha.py#L320"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `new_graph`

```python
new_graph(graph_type='werner', nodes=5, edges=8, mode='directed', cont=2)
```

Creates a new graph for the Snha object. 



**Args:**
 
 - <b>`graph_type`</b> (str):  type of the graph  "werner" (default)  "rnd_chain"  "band"  "circle"  "hub"  "random"  "barabasi_m1"  "barabasi_m2" 
 - <b>`nodes`</b> (int):  number of nodes in the graph (default: 5) 
 - <b>`edges`</b> (int):  number of edges in the graph (default: 6) mode (str): 
 - <b>`"directed"`</b>:  directed graph (default) 
 - <b>`"undirected"`</b>:  undirected graph 
 - <b>`cont`</b> (int):  number of signal seeds; default: 2 (only for graph type rndChain) 



**Examples:**
 

```{.py}
from snha4py.Snha import Snha

s = Snha()
s.new_graph()
graph = s.get_graph()
print(graph)
``` 

---

<a href="../snha4py/Snha.py#L357"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="../snha4py/Snha.py#L384"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
 - <b>`target`</b> (matplotlib.axes):  axes to plot the graph on pred (boolean): 
 - <b>`True`</b> (default):  Plot the determined association chains 
 - <b>`False`</b>:  Plot the edges from the adjacency matrix 
 - <b>`vs`</b> (float):  vertrex size; default: 25 



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

<a href="../snha4py/Snha.py#L436"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_corr`

```python
set_corr(c_data)
```

Set the correlation data for the Snha object. 



**Args:**
 
 - <b>`c_data`</b> (pandas.DataFrame):  Correlation matrix 

---

<a href="../snha4py/Snha.py#L445"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_data`

```python
set_data(data)
```

Set the data for the Snha object. 



**Args:**
 
 - <b>`data`</b> (pandas.DataFrame):  DataFrame with m observations for n variables 

---

<a href="../snha4py/Snha.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_graph`

```python
set_graph(graph)
```

Set the graph for the Snha object. 



**Args:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacency matrix 

---

<a href="../snha4py/Snha.py#L463"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_graph_pred`

```python
set_graph_pred(graph)
```

Set the graph prediction for the Snha object. 



**Args:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacency matrix 

---

<a href="../snha4py/Snha.py#L472"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `snha`

```python
snha(df, alpha)
```

Extracts the association chains resulting from the correlation data. 



**Args:**
 
 - <b>`df`</b> (pandas.DataFrame):  correlation matrix 
 - <b>`alpha`</b> (float, [0,1]):  correlation coefficient cut off 

---

<a href="../snha4py/Snha.py#L517"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `snha_bt`

```python
snha_bt(df, alpha, n, lbd, method)
```

Applying the St Nicholas algorithm within a bootstrapp routine. 



**Args:**
 
 - <b>`df`</b> (pandas.DataFrame):  Input data 
 - <b>`alpha`</b> (float, [0,1]):  correlation coefficient cut off 
 - <b>`n`</b> (int):  number of bootstrap iterations 
 - <b>`lbd`</b> (float, [0,1]):  fraction of all iterations to accept an edge as a prediction (e.g. 50/100 iterations an edge need to be found, to be considered as a predicted edge at lbd=0.5 and n=100) method (str): 
 - <b>`"pearson" (default)`</b>:  standard correlation coefficient 
 - <b>`"kendall"`</b>:  Kendall Tau correlation coefficient 
 - <b>`"spearman"`</b>:  Spearman rank correlation 

---

<a href="../snha4py/Snha.py#L561"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `st_nich_alg`

```python
st_nich_alg(data=None, alpha=0.1, bt=False, n=100, lbd=0.5, method='pearson')
```

Selection to use the St. Nicholaus algorithm with or without bootstrapping. 



**Args:**
  data (pandas.DataFrame): 
 - <b>`bt=True`</b>:  Input data 
 - <b>`bt=False`</b>:  Correlation matrix 
 - <b>`alpha`</b> (float, [0,1]):  correlation coefficient cut off; default: 0.1 
 - <b>`bt`</b> (boolean):  Bootstrap True/Flase; default: False 
 - <b>`n`</b> (int):  number of bootstrap iterations; default: 100 
 - <b>`lbd`</b> (float, [0,1]):  fraction of all iterations to accept an edge as a prediction; default: 0.5 (e.g. 50/100 iterations an edge need to be found, to be considered as a predicted edge at lbd=0.5 and n=100) method (string): 
 - <b>`"pearson" (default)`</b>:  standard correlation coefficient 
 - <b>`"kendall"`</b>:  Kendall Tau correlation coefficient 
 - <b>`"spearman"`</b>:  Spearman rank correlation 



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
