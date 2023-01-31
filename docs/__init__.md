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

<a href="../snha4py/__init__.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `__init__.py`
API of snha4py 

Documentation of the St. Nicolas House algorithm for python3.  [Back to github](https://github.com/thake93/snha4py/) 

Classes *Note*: 


- in green: public methods 
- in red: private methods 

```{.kroki echo=false dia=plantuml}
class Snha{
+ data
+ graph
+ graph_pred
+ corr
+ chains

- col_map


- chains2admat()

- check_labels()

- clean_sub_chains(chains)
+ comp_corr(df, mehtod, in_place)
+ conf_mat()
+ create_corr_data(n, steps, mean, sd, noise, prop)
+ get/set() for all attributes
+ graph_stats()

- middle_chains(nodes, df)
+ new_graph(graph_type, nodes, edges, mode, cont)
+ plot_corr(labels, ax)
+ plot_graph(layout, mode, col, labels, labels_e, pred, ax)

- snha(df, alpha)

- snha_bt(df, alpha, n, lbd, method)
+ st_nich_alg(data, alpaha, bt, n, lbd, method)
}

class SnhaDataGen{
+ graph
+ n
+ steps
+ mean
+ sd
+ noise
+ prop
 
+ create_data()
+ get_data()
}

class SnhaNewGraph{
+ nodes
+ edges

- graph
+ mode
+ cont


- band()

- barabasi(m)

- barabasi_m1()

- barabasi_m2()

- circle()

- edge_dir_shuffle()

- hub()
+ get_graph()

- random()

- rnd_chain()
+ set_graph(fct)

- undir2dir(start, visited, g_new, nodes)

- werner()
}

class SnhaPlot{
+ data
+ labels_n
+ ax

+ corr()

- get_orth_vec(vec, scale)
+ graph(layout, mode, col, labels_e)

- scale(layout, a, b)

- unit_length_vec
}


Snha <-- SnhaDataGen
Snha <-- SnhaPlot
SnhaNewGraph -> Snha
``` 





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
