from unittest import TestCase

from day03.solution import _read_input, _count_trees


class Day03TestSuite(TestCase):

    def test_count_trees(self):
        lines = _read_input('./test_input.txt')
        self.assertEqual(7, _count_trees(lines, 3, 1))
