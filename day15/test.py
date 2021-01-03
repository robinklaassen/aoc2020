from unittest import TestCase
from day15.solution import determine_nth_number


class Day15TestSuite(TestCase):

    def test_determine(self):
        self.assertEqual(1, determine_nth_number([1, 3, 2], 2020))
        self.assertEqual(10, determine_nth_number([2, 1, 3], 2020))
        self.assertEqual(27, determine_nth_number([1, 2, 3], 2020))

        self.assertEqual(175594, determine_nth_number([0, 3, 6], 30_000_000))
