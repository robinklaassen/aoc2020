from unittest import TestCase

from day06.solution import _read_input, count_group_any, count_group_every


class Day06TestSuite(TestCase):

    def test_count_group_any(self):
        group = [
            'ab',
            'ac',
        ]

        self.assertEqual(3, count_group_any(group))

    def test_count_group_every(self):
        group = [
            'abcd',
            'abc',
            'ab',
        ]

        self.assertEqual(2, count_group_every(group))

    def test_part1(self):
        groups = _read_input('./test_input.txt')
