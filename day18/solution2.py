from typing import List, Union

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


def evaluate_expression(expr: List[chr]) -> List[chr]:
    # If expression contains parentheses, extract first innermost and evaluate
    if expr.count('('):
        paren_idx = {
            paren: [i for i, char in enumerate(expr) if char == paren]
            for paren in ['(', ')']
        }

        close_paren = paren_idx[')'][0]
        open_paren = max(i for i in paren_idx['('] if i < close_paren)
        new_expr = expr[:open_paren] + evaluate_expression(expr[open_paren + 1:close_paren]) + expr[close_paren + 1:]
        return evaluate_expression(new_expr)

    # If no parentheses, evaluate the first addition
    if expr.count('+'):
        plus_idx = expr.index('+')
        new_expr = expr[:plus_idx - 1] + [str(int(expr[plus_idx - 1]) + int(expr[plus_idx + 1]))] + expr[plus_idx + 2:]
        return evaluate_expression(new_expr)

    # Then the first multiplication
    if expr.count('*'):
        times_idx = expr.index('*')
        new_expr = expr[:times_idx - 1] + [str(int(expr[times_idx - 1]) * int(expr[times_idx + 1]))] + expr[times_idx + 2:]
        return evaluate_expression(new_expr)

    # If there is one element remaining, return it
    if len(expr) == 1:
        return expr

    raise ValueError(f"Don't know how to handle expression {expr}.")


def main():
    # Solution to part 2 only
    lines = read_input('./input.txt')
    expressions = _parse_lines(lines)

    answers = [evaluate_expression(expr) for expr in expressions]
    answers = [int(answer[0]) for answer in answers]

    print(f'Evaluated {len(expressions)} expressions; the sum of all their answers is {sum(answers)}.')


if __name__ == '__main__':
    main()
