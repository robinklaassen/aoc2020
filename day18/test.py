from unittest import TestCase

from day18.solution import _parse_lines, evaluate, evaluate_advanced
from day18.solution2 import evaluate_expression


class Day18TestSuite(TestCase):

    def test_part_1(self):
        line = '1 + (2 * 3)'

        expression = _parse_lines([line])[0]
        self.assertEqual(['1', '+', '(', '2', '*', '3', ')'], expression)

        self.assertEqual(7, evaluate(expression))

        line2 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
        expression2 = _parse_lines([line2])[0]
        self.assertEqual(13632, evaluate(expression2))

    def test_part_2(self):
        lines = [
            '1 + 2 * 3 + 4 * 5 + 6',
            '1 + (2 * 3) + (4 * (5 + 6))',
            '2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
        ]

        expressions = _parse_lines(lines)

        answers = [231, 51, 46, 1445, 669060, 23340]

        for i in range(len(lines)):
            self.assertEqual(answers[i], evaluate_advanced(expressions[i]))

    def test_part_2_v2(self):
        lines = [
            '1 + 2 * 3 + 4 * 5 + 6',
            '1 + (2 * 3) + (4 * (5 + 6))',
            '2 * 3 + (4 * 5)',
            '5 + (8 * 3 + 9 + 3 * 4 * 3)',
            '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))',
            '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2',
        ]

        expressions = _parse_lines(lines)

        answers = [231, 51, 46, 1445, 669060, 23340]

        for i in range(len(lines)):
            output = evaluate_expression(expressions[i])
            answer = int(output[0])
            self.assertEqual(answers[i], answer)
