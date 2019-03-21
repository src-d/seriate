import unittest

import numpy
from scipy.spatial.distance import pdist, squareform

from seriate import seriate


class SeriateTests(unittest.TestCase):
    def setUp(self):
        self.elements = numpy.ones((5, 3)) * numpy.arange(5, 0, -1)[:, None]

    def test_pdist(self):
        dists = pdist(self.elements)
        seq = seriate(dists)
        self.assertEqual(seq, [4, 3, 2, 1, 0])

    def test_squareform(self):
        dists = squareform(pdist(self.elements))
        seq = seriate(dists)
        self.assertEqual(seq, [4, 3, 2, 1, 0])


if __name__ == "__main__":
    unittest.main()
