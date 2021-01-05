from collections import Counter
from unittest import TestCase

from day17.solution_3d import _parse_lines, _count_neighbors, _next_state
from utils import read_input


class Day17TestSuite(TestCase):

    def test_part_1(self):
        lines = read_input('./test_input.txt')
        cells = _parse_lines(lines)

        self.assertEqual(5, len(cells))

        neighbors = _count_neighbors(cells)

        self.assertIsInstance(neighbors, Counter)

        next_state = _next_state(cells)

        self.assertEqual(11, len(next_state))
