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

# Usage
Here, I present an in-depth explenation of 

1. [Analysing your data by graph prediction](#analysing-your-data-by-graph-prediction)
2. [Creating correlated data from a directed graph](#creating-correlated-data-from-a-directed-graph)

via the comando-line interface (CLI) or within your python scirpt.

## Analysing your data by graph prediction
I demonstrate the useage of the tool on exemplary data from the 
[olympic decathlon of 1988]()
([further information])(https://rdrr.io/cran/ade4/man/olympic.html).
The data set comprises the results of 33 Athletes competing in 1988 in the events:

- **running**: 100m, 400m, 1500m and 110m hurdles (seconds)
- **jumping**: long jump, high jump and pole vault (meter)
- **throwing**: javelin, discus, shot put (meter)

For demonstration reasons I add a random variable.

### Comando-line interface
### In python script 
Using the tool within your script grants you the most flexibility. So, I recommend you to use it that way.

## Creating correlated data from a directed graph

### Comando-line interface
Assum you want to create correlated data for a graph, which looks like this:
<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/werner.png" width="200" height="200">
</div>
We create correlated data along the edges of the graph.

```shell
python3 -m snha4py --create-data --graph werner.csv -o data.csv --steps 25 --iterations 200 --plot
```

### In python script 
