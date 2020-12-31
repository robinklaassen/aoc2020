from unittest import TestCase

from day09.solution import find_first_invalid, find_contiguous_sum
from utils import read_input


class Day09TestSuite(TestCase):

    def test_part1(self):
        lines = read_input('./test_input.txt')
        numbers = [int(line) for line in lines]
        result = find_first_invalid(numbers, 5)
        self.assertEqual(127, result)

    def test_part2(self):
        lines = read_input('./test_input.txt')
        numbers = [int(line) for line in lines]
        contiguous_seq = find_contiguous_sum(numbers, target=127)
        self.assertEqual([15, 25, 47, 40], contiguous_seq)
