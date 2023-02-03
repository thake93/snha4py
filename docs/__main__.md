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

<a href="../snha4py/__main__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `__main__.py`
The St. Nicolas House Algorithm comando line application. 

Currently available functions are: 


- the general algorithm with/ without bootstrap to predict a graph from data 
- create correlated data based on a directed graph 
- crete a directed graph 

For further information and examples see [readme file](https://github.com/thake93/snha4py/tree/main/snha4py/README.md).  [Back to github](https://github.com/thake93/snha4py/) 


---

<a href="../snha4py/__main__.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_data`

```python
create_data(args)
```

A wrapper to create data based on the arguments given by the parser. 

Argumenst:  args (argparse.Namespace): Namespace object result from the comando line arguments 


---

<a href="../snha4py/__main__.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_graph`

```python
create_graph(args)
```

A wrapper to create a graph based on the arguments given by the parser. 

Argumenst:  args (argparse.Namespace): Namespace object result from the comando line arguments 


---

<a href="../snha4py/__main__.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_file`

```python
read_file(f, graph)
```

Reads a file. 



**Arguments:**
 
 - <b>`f`</b> (str):  path to the file 
 - <b>`graph`</b> (boolean):  True: reads the file without a header; False: reads the file with a header 

**Returns:**
 
 - <b>`in_file`</b> (pandas.DataFrame):  data or adjacency matrix 


---

<a href="../snha4py/__main__.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `snha`

```python
snha(args)
```

A wrapper to run the St. Nicolas House algorithm based on the arguments given by the parser. 

Argumenst:  args (argparse.Namespace): Namespace object result from the comando line arguments 


---

<a href="../snha4py/__main__.py#L149"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main`

```python
main(parser)
```

Calls the desired function. 



**Arguments:**
 
 - <b>`parser`</b> (argparse.ArgumentParser):  holding information of the CLI input 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
