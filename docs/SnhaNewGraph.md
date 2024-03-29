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

<a href="../snha4py/SnhaNewGraph.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `SnhaNewGraph.py`
The St. Nicolas House Algorithm graph collection. 

[Back to github](https://github.com/thake93/snha4py/) 

**Examples:**
 

```{.py}
from snha4py.SnhaNewGraph import SnhaNewGraph

fct = dir(SnhaNewGraph)
ignore = ["set_graph", "get_graph", "undir2dir", "edge_dir_shuffle", "dir2undir"]
for f in fct:
     if f not in ignore and "__" not in f:
         print(f)
         g = SnhaNewGraph(graph_type=f, nodes=5, edges=8, mode="directed", cont=2)
         graph = g.get_graph()
         print(graph)
``` 



---

## <kbd>class</kbd> `SnhaNewGraph`




<a href="../snha4py/SnhaNewGraph.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(graph_type, nodes, edges, mode, cont)
```

Creates a new graph. 



**Args:**
 
 - <b>`graph_type`</b> (str):  type of the graph; choice of ["werner", "rnd_chain", "band", "circle", "hub", "random", "barabasi_m1", "barabasi_m2"] 
 - <b>`nodes`</b> (int):  number of nodes in the graph 
 - <b>`edges`</b> (int):  number of edges in the graph 
 - <b>`mode`</b> (str):  "directed": directed graph; "undirected": undirected graph 
 - <b>`cont`</b> (int):  number of signal seeds (only for graph type rndChain) 




---

<a href="../snha4py/SnhaNewGraph.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `band`

```python
band()
```

Implementation of a band graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `barabasi`

```python
barabasi(m=1)
```

Creates an Barabasi-M1/M2 graph. 



**Args:**
 
 - <b>`m`</b> (int):  1: barabasi-M1 graph; 2: brabasi-M2 graph 

---

<a href="../snha4py/SnhaNewGraph.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `barabasi_m1`

```python
barabasi_m1()
```

Implementation of a barabasi-M1 graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `barabasi_m2`

```python
barabasi_m2()
```

Implementation of a barabasi-M2 graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `circle`

```python
circle()
```

Implementation of a circle graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `dir2undir`

```python
dir2undir()
```

Turns a directed graph into an undirected graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `edge_dir_shuffle`

```python
edge_dir_shuffle()
```

Shuffle the direction of the Snha objects graph edges. 

---

<a href="../snha4py/SnhaNewGraph.py#L128"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_graph`

```python
get_graph()
```



**Returns:**
 
 - <b>`self.graph (numpy.ndarray)`</b>:  the created graph 

---

<a href="../snha4py/SnhaNewGraph.py#L120"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `hub`

```python
hub()
```

Implementation of a hub graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `random`

```python
random()
```

Implementation of a random graph. 

---

<a href="../snha4py/SnhaNewGraph.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `rnd_chain`

```python
rnd_chain()
```

Implementation of a random graph. Select random start nodes and create directed paths through all nodes. 

---

<a href="../snha4py/SnhaNewGraph.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `set_graph`

```python
set_graph(fct)
```

Calls the graph-function and sets the graph. 



**Args:**
 
 - <b>`fct`</b> (string):  name of the graph to call the function 

---

<a href="../snha4py/SnhaNewGraph.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `undir2dir`

```python
undir2dir(start, visited, g_new, nodes)
```

Creates a directed graph from an undirected graph. 



**Args:**
 
 - <b>`start`</b> (numpy.ndarray):  list of start nodes 
 - <b>`visited`</b> (list):  list of nodes already visited 
 - <b>`g_new`</b> (np.array):  directed graph 
 - <b>`nodes`</b> (int):  number of nodes 

---

<a href="../snha4py/SnhaNewGraph.py#L205"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `werner`

```python
werner()
```

Implementation of a werner graph. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
