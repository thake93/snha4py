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

<a href="../snha4py/SnhaDir.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `SnhaDir.py`
Direction analysis of the St. Nicolas House Algorithm. 

Soon be updated.  [Back to github](https://github.com/thake93/snha4py/) 



---

## <kbd>class</kbd> `SnhaDir`







---

<a href="../snha4py/SnhaDir.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `comp_xi`

```python
comp_xi()
```

Computes Xi correlation matrix for the Snha objects data. 

---

<a href="../snha4py/SnhaDir.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `get_xi`

```python
get_xi()
```

Get the Xi correlation matrix from the Snha object. 



**Returns:**
 
 - <b>`xi`</b>:  Xi correlation matrix 

---

<a href="../snha4py/SnhaDir.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>function</kbd> `xi_corr`

```python
xi_corr(x, y)
```

Computes the Xi correlation between two arrays. 



**Args:**
 
 - <b>`x`</b> (pandas.Series):  Data vector 
 - <b>`y`</b> (pandas.Series):  Data vector 



**Returns:**
 
 - <b>`xi`</b>:  Xi correlation from x to y 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
