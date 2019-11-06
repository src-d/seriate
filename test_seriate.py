import unittest

import numpy
from scipy.spatial.distance import pdist, squareform

from seriate import IncompleteSolutionError, InvalidDistanceValues, seriate


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

    def test_empty_pdist(self):
        dists = numpy.empty((0,))
        seq = seriate(dists)
        self.assertEqual(seq, [0])

    def test_empty_squareform(self):
        dists = numpy.empty((0, 0))
        seq = seriate(dists)
        self.assertEqual(seq, [])

    def test_single(self):
        dists = numpy.ones((1, 1))
        seq = seriate(dists)
        self.assertEqual(seq, [0])

    def test_timeout_error(self):
        with self.assertRaises(IncompleteSolutionError):
            seriate(pdist(self.elements), timeout=1e-4)

    def test_timeout_0(self):
        numpy.random.seed(160290)
        big_dist = numpy.random.random((2000, 2000))  # This matrix will increase the timeout once
        seq = seriate(big_dist, timeout=0)
        self.assertIsInstance(seq, list)
        self.assertIsInstance(seq[0], int)

    def test_errors(self):
        with self.assertRaises(InvalidDistanceValues):
            seriate(numpy.array([numpy.inf, 0, 0, 0]))

        with self.assertRaises(InvalidDistanceValues):
            seriate(numpy.array([numpy.nan, 0, 0, 0]))

        with self.assertRaises(InvalidDistanceValues):
            seriate(numpy.array([None, 0, 0, 0]))


if __name__ == "__main__":
    unittest.main()
