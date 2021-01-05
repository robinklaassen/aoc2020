from collections import defaultdict
from typing import List

from utils import read_input


def _parse_lines(lines: List[str]) -> List[List[chr]]:
    return [
        [
            char
            for char in line
            if char != ' '
        ]
        for line in lines
    ]


def operate(val1: int, val2: int, operator: chr) -> int:
    if operator is None:
        return val2
    if operator == '+':
        return val1 + val2
    if operator == '*':
        return val1 * val2
    raise ValueError(f"Don't know how to operate on {val1, val2, operator}.")


def evaluate(expression: List[chr]) -> int:
    level = 0
    values = defaultdict(int)
    operators = defaultdict(lambda: None)
    for char in expression:
        if char.isnumeric():
            values[level] = operate(values[level], int(char), operators[level])
            operators[level] = None
        elif char in ['+', '*']:
            operators[level] = char
        elif char == '(':
            level += 1
        elif char == ')':
            level -= 1
            values[level] = operate(values[level], values[level + 1], operators[level])
            operators[level] = None
        else:
            raise ValueError(f"Don't know what to do with character `{char}`.")

    assert level == 0, f'Unmatched parentheses in {expression}'
    return values[0]


def evaluate_advanced(expression: List[chr]) -> int:
    level = 0
    values = defaultdict(int)
    operators = defaultdict(lambda: None)
    for char in expression:
        if char.isnumeric():
            values[level] = operate(values[level], int(char), operators[level])
            operators[level] = None
        elif char == '*':
            operators[level] = char
            level += 1
        elif char == '+':
            operators[level] = char
        elif char == '(':
            level += 1
        elif char == ')':
            level -= 1
            values[level] = operate(values[level], values[level + 1], operators[level])
            operators[level] = None
        else:
            raise ValueError(f"Don't know what to do with character `{char}`.")

    print('bla')

    while level > 0:
        level -= 1
        values[level] = operate(values[level], values[level + 1], operators[level])

    return values[0]


def main():
    lines = read_input('./input.txt')
    expressions = _parse_lines(lines)
    answers = [evaluate(expr) for expr in expressions]
    print(f'Evaluated {len(expressions)} expressions; the sum of all their answers is {sum(answers)}.')

    advanced_answers = [evaluate_advanced(expr) for expr in expressions]
    print(f'When using advanced math, the sum of all answers is {sum(advanced_answers)}.')


if __name__ == '__main__':
    main()
