# seriate
Optimal ordering of elements in a set given their distance matrix.

[![Travis build status](https://travis-ci.com/src-d/seriate.svg?branch=master)](https://travis-ci.com/src-d/seriate)
[![Code coverage](https://codecov.io/github/src-d/seriate/coverage.svg)](https://codecov.io/github/src-d/seriate)
[![PyPi package status](https://img.shields.io/pypi/v/seriate.svg)](https://pypi.python.org/pypi/seriate)
![stability: stable](https://svg-badge.appspot.com/badge/stability/stable?color=007ec6)
[![Apache 2.0 license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

![example](doc/example.png)

[Overview](#overview) • [How To Use](#how-to-use) • [Contributions](#contributions) • [License](#license)

## Overview

This is a Python implementation of [Seriation](http://nicolas.kruchten.com/content/2018/02/seriation/)
algorithm. Seriation is an approach for ordering elements in a set so that the
sum of the sequential pairwise distances is minimal. We state this task
as a Travelling Salesman Problem (TSP) and leverage the powerful [Google's or-tools](https://github.com/google/or-tools)
to do heavy-lifting. Since TSP is NP-hard, it is not possible to calculate
the precise solution for a big number of elements. However, the or-tools'
heuristics work very well in practice, and they are used in e.g. Google Maps.

Any [`numpy.roll`-ed](https://docs.scipy.org/doc/numpy-1.16.0/reference/generated/numpy.roll.html)
result is equivalent.

## How To Use

```python
import numpy
from scipy.spatial.distance import pdist
from seriate import seriate

elements = numpy.array([
    [3, 3, 3],
    [5, 5, 5],
    [4, 4, 4],
    [2, 2, 2],
    [1, 1, 1]
])

print(seriate(pdist(elements)))

# Output: [4, 3, 0, 2, 1]
```

The example above shows how we order 5 elements: `[3, 3, 3]`,
`[5, 5, 5]`, `[4, 4, 4]`, `[2, 2, 2]` and `[1, 1, 1]`. The result
is expected:

1. `[1, 1, 1]` 
2. `[2, 2, 2]` 
3. `[3, 3, 3]` 
4. `[4, 4, 4]` 
5. `[5, 5, 5]`

`pdist` from [`scipy.spatial.distance`](https://docs.scipy.org/doc/scipy/reference/spatial.distance.html)
uses Euclidean (L2) dstance metric by default, so the distance between
`[x, x, x]` and `[x + 1, x + 1, x + 1]` is constant: √3. Any other distance
is bigger, so the optimal ordering is to list our elements in the increasing
norm order.

## Contributions

Contributions are very welcome and desired! Please follow the [code of conduct](doc/code_of_conduct.md)
and read the [contribution guidelines](doc/contributing.md).

## License

Apache-2.0, see [LICENSE.md](LICENSE.md).
