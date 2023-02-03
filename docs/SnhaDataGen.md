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

<a href="../snha4py/SnhaDataGen.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `SnhaDataGen.py`
St. Nicolas House Algorithm data generation. 

The module generates data correlated data along a directed graph based on the Monte Carlo approach. For further inforation see [Novine et al. (2022)](https://doi.org/10.52905/hbph2021.3.26).  [Back to github](https://github.com/thake93/snha4py/) 



---

## <kbd>class</kbd> `SnhaDataGen`




<a href="../snha4py/SnhaDataGen.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `__init__`

```python
__init__(graph, n, steps, mean, sd, noise, prop)
```

Create a data generator for correlated data based on a graph. 



**Args:**
 
 - <b>`graph`</b> (numpy.ndarray):  adjacents matrix of a directed graph 
 - <b>`n`</b> (int):  the number of measurements per node 
 - <b>`steps`</b> (int):  the number of iterations 
 - <b>`mean`</b> (float):  mean value for sampling from a Gaussian distribution 
 - <b>`sd`</b> (float):  standard deviation for sampling from a Gaussian distribution 
 - <b>`noise`</b> (float):  standard deviation for sampling noise from a Gaussian distribution with mean 0 after each iteration 
 - <b>`prop`</b> (float):  proportion of the target node value take the source node 




---

<a href="../snha4py/SnhaDataGen.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `create_data`

```python
create_data()
```

Creates correlated data along edges of a directed graph based on a Monte Carlo approach. 



**Examples:**
 

```{.py}
from snha4py.SnhaDataGen import SnhaDataGen
import numpy as np

graph = np.array(
     [
         [0, 0, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0],
     ]
)
dg = SnhaDataGen(graph, n=100, steps=15, mean=100, sd=2, noise=1, prop=0.05)

data = dg.get_data()
print(data)
``` 

---

<a href="../snha4py/SnhaDataGen.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_data`

```python
get_data()
```



**Returns:**
 
 - <b>`self.data (pandas.DataFrame)`</b>:  correlated data of size (p, n), with p the number of nodes of the graph and n the number of measurements per node. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
