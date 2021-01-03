from dataclasses import dataclass
from functools import reduce
from typing import List, Tuple, Dict

from utils import read_input


@dataclass(frozen=True)
class Rule:
    name: str
    bounds: Tuple[Tuple[int, int]]

    @classmethod
    def from_string(cls, string: str) -> 'Rule':
        name_, bounds_string = string.split(': ')
        bounds = tuple(
            tuple(int(i) for i in bound.split('-'))
            for bound in bounds_string.split(' or ')
        )
        return Rule(
            name=name_,
            bounds=bounds
        )

    def number_is_valid(self, number: int) -> bool:
        return any(low <= number <= high for low, high in self.bounds)


@dataclass(frozen=True)
class Ticket:
    raw_numbers: List[int]

    @classmethod
    def from_string(cls, string: str) -> 'Ticket':
        return Ticket([int(i) for i in string.split(',')])

    def is_valid(self, rules: List[Rule]) -> bool:
        # Valid when any of the raw numbers are not valid for all of the rules
        for number in self.raw_numbers:
            invalidity = [not rule.number_is_valid(number) for rule in rules]
            if all(invalidity):
                return False
        return True


def _split_list(sequence, sep):
    # From https://stackoverflow.com/questions/54372218/how-to-split-a-list-into-sublists-based-on-a-separator-similar-to-str-split
    chunk = []
    for val in sequence:
        if val == sep:
            yield chunk
            chunk = []
        else:
            chunk.append(val)
    yield chunk


def _parse_lines(lines: List[str]) -> Tuple[List[Rule], Ticket, List[Ticket]]:
    splitted_lines = list(_split_list(lines, ''))

    rules = [Rule.from_string(line) for line in splitted_lines[0]]
    my_ticket = Ticket.from_string(splitted_lines[1][1])
    other_tickets = [Ticket.from_string(line) for line in splitted_lines[2][1:]]

    return rules, my_ticket, other_tickets


def determine_invalid_numbers(tickets: List[Ticket], rules: List[Rule]) -> List[int]:
    return [
        number for ticket in tickets for number in ticket.raw_numbers
        if all(not rule.number_is_valid(number) for rule in rules)
    ]


def main():
    lines = read_input('./input.txt')
    rules, my_ticket, other_tickets = _parse_lines(lines)

    # Part 1
    invalid_numbers = determine_invalid_numbers(other_tickets, rules)
    print(f'Found {len(invalid_numbers)} invalid numbers. Ticket scanning error rate is {sum(invalid_numbers)}.')

    # Part 2
    valid_other_tickets = [ticket for ticket in other_tickets if ticket.is_valid(rules)]
    print(f'Of {len(other_tickets)} other tickets, only {len(valid_other_tickets)} are valid.')

    numbers_per_position = {
        pos: [ticket.raw_numbers[pos] for ticket in valid_other_tickets]
        for pos in range(len(rules))
    }

    valid_positions_per_rule = {
        rule: [
            pos for pos in numbers_per_position.keys()
            if all(rule.number_is_valid(number) for number in numbers_per_position[pos])
        ]
        for rule in rules
    }

    for rule, valid_pos in valid_positions_per_rule.items():
        print(f'{rule.name} : {len(valid_pos)} : {valid_pos}')

    # Continue by hand :)
    position_names = {
        18: 'train',
        12: 'seat',
        13: 'wagon',
        3: 'arrival location',
        4: 'duration',
        1: 'arrival track',
        9: 'arrival platform',
        10: 'departure platform',
        8: 'departure station',
        11: 'departure track',
        17: 'departure location',
        19: 'departure time',
        0: 'departure date',
        6: 'route',
        14: 'price',
        15: 'row',
        2: 'arrival station',
        5: 'class',
        7: 'zone',
        16: 'type',
    }

    my_departure_numbers = [num for i, num in enumerate(my_ticket.raw_numbers)
                            if position_names[i].startswith('departure')]
    print(f'My departure numbers are {my_departure_numbers}.')

    answer = reduce(lambda x, y: x * y, my_departure_numbers)
    print(f'Answer is {answer}.')


if __name__ == '__main__':
    main()
