from unittest import TestCase

from day05.solution import binary_reduce


class Day05TestSuite(TestCase):

    def test_binary_reduce(self):
        self.assertEqual(44, binary_reduce('FBFBBFF', 'F', 'B'))
        self.assertEqual(5, binary_reduce('RLR', 'L', 'R'))
