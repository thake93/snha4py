#! /usr/bin/env python3

"""
API of snha4py

Documentation of the St. Nicolas House algorithm for python3. 

Classes

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
"""
