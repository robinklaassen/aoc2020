from unittest import TestCase

from day04.solution import _read_input


class Day04TestSuite(TestCase):

    def test_required_fields(self):
        passports = _read_input('./test_input.txt')
        valids = [p.has_required_fields for p in passports]
        self.assertEqual([True, False, True, False], valids)

    def test_valid(self):
        passports = _read_input('./test_input_2.txt')
        valids = [p.is_valid for p in passports]
        expected = [False] * 4 + [True] * 4
        self.assertEqual(expected, valids)
