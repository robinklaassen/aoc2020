from unittest import TestCase

from day16.solution import _parse_lines, determine_invalid_numbers
from utils import read_input


class Day16TestSuite(TestCase):

    def test_determine_invalid_numbers(self):
        lines = read_input('./test_input.txt')
        rules, my_ticket, other_tickets = _parse_lines(lines)

        self.assertEqual([True, True, False], [rule.number_is_valid(7) for rule in rules])

        invalid_numbers = determine_invalid_numbers(other_tickets, rules)
        self.assertEqual({4, 55, 12}, set(invalid_numbers))
