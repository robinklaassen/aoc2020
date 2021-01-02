from unittest import TestCase

from day12.solution import _rotate


class Day12TestSuite(TestCase):

    def test_rotate(self):
        self.assertEqual('E', _rotate('N', 'R', 90))
        self.assertEqual('W', _rotate('N', 'L', 90))
        self.assertEqual('W', _rotate('N', 'R', 270))
        self.assertEqual('N', _rotate('S', 'L', 180))
