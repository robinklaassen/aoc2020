from unittest import TestCase

from day07.solution import _read_input, _parse_string, count_contains


class Day07TestSuite(TestCase):

    def test_part2(self):
        lines = _read_input('./test_input.txt')
        relations = [_parse_string(line) for line in lines]

        target = 'shiny gold'
        num_contained_bags = count_contains(target, 1, relations)

        self.assertEqual(32, num_contained_bags)
