# snha4py
Snha4py is a Python implementation of the St. Nicholas House algorithm ([_Groth et al. 2019_](https://doi.org/10.1127/anthranz/2019/1027), 
[_Hermanussen et al. 2021_](https://doi.org/10.3390%2Fijerph18041741), 
_Hake et al. 2023_). 
The algorithm infers a graph based on the correlation coefficient between variables of a data set. Here, the nodes and the edges would be the variables of the data set and the correlation coefficient, respectively. 
The correlation coefficient is evaluated in terms of association chains. 
Therfore, the absolute coefficient is ranked and compared pairwise.
An association chain is characterized by a sequence of variables for which reversing the start and end point does not change the order of elements.
These chains then build the graph.

Next, to the algorithm the package offers a variety of graph implementations, as well as a vizualization routine for the graphs and the correlation matrix.

Also, a module to create correlated data along a directed graph based on a Monte Carlo approach is included 
([_Novine et al. 2022_](https://doi.org/10.52905/hbph2021.3.26)).

You can use the St. Nicolas House algorithm and other features of the package as a [command-line interface (CLI)](#command-line-interface) or you can [import the package](#as-import-in-your-own-code) in your own code.

There is also an implementation of the SNHA in
[R](https://github.com/mittelmark/snha)
available.

# Documentation

- [HTML](https://htmlpreview.github.io/?https://github.com/thake93/snha4py/blob/main/docs/__init__.html)
- [Markdown](https://github.com/thake93/snha4py/blob/main/docs/Snha.md)

# Install
```
pip install snha4py
```
```
pip3 install git+https://github.com/thake93/snha4py.git --user
```
after the installation you should be able to run:

```shell
pip show snha4py
```

# Create your 1<sup>st</sup> "St. Nicolas House"

## Command-line interface

We start with creating a directory to store the test files.
```shell
mkdir test_snha
cd test_snha
```

In the first place we create test data in two steps:

1. We create a directed graph.
```shell
python3 -m snha4py --create-graph -t werner -o werner.csv
```

2. We create correlated data along the edges of the graph.
```shell
python3 -m snha4py --create-data --graph werner.csv -o data.csv --steps 25 --iterations 200 --plot
```

Now, we can run the algortihm to predict the graph based on the correlation of the data.
```shell
python3 -m snha4py --snha --data data.csv -o graph_pred.csv -p
```

Also, we are able to apply bootstrapping to increase the prediction (_Hake et al. (2023)_).
```shell
python3 -m snha4py --snha --data data.csv -o graph_pred_bt.csv --bootstrap -i 10 -p
```
**Note**: The result might differ from the picture below.

## As import in your own code
```shell
python3
```
```python
Python 3.x.xx ()

>>> from snha4py.Snha import Snha
>>> import matplotlib.pyplot as plt

>>> s = Snha()
>>> s.new_graph()
>>> s.create_corr_data(200,25)
>>> s.comp_corr(method='spearman')
>>> s.st_nich_alg()

>>> fig,ax = plt.subplots(1,3, figsize=(30,10))

>>> s.plot_graph(pred=False, ax=ax[0])
>>> s.plot_corr(ax=ax[1])
>>> s.plot_graph(ax=ax[2])

>>> ax[0].set_title('True Graph')
>>> ax[1].set_title('Correlation Coefficient')
>>> ax[2].set_title('Predicted Graph')

>>> plt.show()
```
<div align="center">
  <img src="https://github.com/thake93/snha4py/blob/main/examples/pics/example.png">
</div>

# References
Groth, D., Scheffler, C., and Hermanussen, M. (2019). Body height in stunted indonesian children
depends directly on parental education and not via a nutrition mediated pathway - evidence
from tracing association chains by st. nicolas house analysis. *Anthropologischer Anzeiger*,
76(5):445–451. [DOI](https://doi.org/10.1127/anthranz/2019/1027)

Hake, T., Bodenberger, B., Groth, D. (2023). In Python available: St. Nicolas House Algorithm (SNHA)
with bootstrap support for improved performance in dense networks. *Human Biology and Public Health* 4. (Accepted, doi follows)

Hermanussen, M., Aßmann, C., and Groth, D. (2021). Chain reversion for detecting associations
in interacting variables—st. nicolas house analysis. *International Journal of Environmental
Research and Public Health*, 18(4). [DOI](https://doi.org/10.3390%2Fijerph18041741)

Novine, M., Mattsson, C. C., & Groth, D. (2022). Network reconstruction based on synthetic data generated by a Monte Carlo approach. *Human Biology and Public Health, 3*. 
[DOI](https://doi.org/10.52905/hbph2021.3.26)

# License
[MIT License](https://github.com/thake93/snha4py/blob/main/LICENSE)
