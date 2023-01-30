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

<a href="../snha4py/SnhaPlot.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `SnhaPlot.py`
The St. Nicolas House Algorithm plotting routine. 



---

## <kbd>class</kbd> `SnhaPlot`




<a href="../snha4py/SnhaPlot.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(adj_mat, corr, labels_n, ax=None)
```

Create a support object to plot a graph or a correlation matrix. 



**Args:**
 
 - <b>`adj_mat`</b> (numpy.ndarray):  adjacency matrix to plot a graph with SnhaPlot.graph() 
 - <b>`corr`</b> (pd.DataFrame):  correlation matrix to plot with SnhaPlot.corr() 
 - <b>`ax`</b> (matplotlib.axes):  target axes to place the plot 
 - <b>`labels_n`</b> (list):  variable names 




---

<a href="../snha4py/SnhaPlot.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `corr`

```python
corr()
```

Plot the correlation matrix. 

---

<a href="../snha4py/SnhaPlot.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_orth_vec`

```python
get_orth_vec(vec, scale=1)
```

Computes an orthogonal vector of an input vector. 

**Args:**
 
 - <b>`vec`</b> (numpy.ndarry):  input vector 
 - <b>`scale`</b> (float):  scales the orthogonal vector 



**Returns:**
 
 - <b>`orth_vec`</b> (numpy.ndarray):  scaled orthogonal vector 

---

<a href="../snha4py/SnhaPlot.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `graph`

```python
graph(layout, mode, col, labels_e, vs)
```

Plots a graph. 

**Args:**
 
 - <b>`layout`</b> (list):  list of coordinates of the nodes 
 - <b>`mode`</b> (string):  'directed' or 'undirected' 
 - <b>`col`</b> (matplotlib.colors):  color of the nodes or a list of colors, which holds a color for each node 
 - <b>`labels_e`</b> (list):  list of edge labels 
 - <b>`vs`</b> (float):  size for the nodes 

---

<a href="../snha4py/SnhaPlot.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `scale`

```python
scale(layout, a, b)
```

Centers and rescale the layout coordinates for the nodes. 



**Args:**
 
 - <b>`layout`</b> (numpy.ndarray):  layout of the nodes 
 - <b>`a`</b> (float):  lower bound for rescaling 
 - <b>`b`</b> (float):  upper bound for rescaling 

---

<a href="../snha4py/SnhaPlot.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `unit_length_vec`

```python
unit_length_vec(vec)
```

Rescales a vector to unit length. 

**Args:**
 
 - <b>`vec`</b> (numpy.ndarry):  Input vector 



**Returns:**
 
 - <b>`new_vec`</b> (numpy.ndarry):  Unit length version of the input vector 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
