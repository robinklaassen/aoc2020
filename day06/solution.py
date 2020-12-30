from collections import defaultdict
from typing import List


def _read_input(filepath: str) -> List[List[str]]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

    lines = [line or '-' for line in lines]
    groups = ' '.join(lines).split(' - ')
    return [group.split(' ') for group in groups]


def count_group_any(group: List[str]) -> int:
    single_string = ''.join(group)
    all_letters = [c for c in single_string]
    return len(set(all_letters))


def count_group_every(group: List[str]) -> int:
    num_people = len(group)
    single_string = ''.join(group)
    counts = defaultdict(int)
    for c in single_string:
        counts[c] += 1

    return list(counts.values()).count(num_people)


def main():
    groups = _read_input('./input.txt')
    counts = [count_group_any(group) for group in groups]
    print(f'Counted {len(groups)} groups with sum total {sum(counts)} counts for `any` situation')

    counts2 = [count_group_every(g) for g in groups]
    print(f'In the `every` situation, the sum total is {sum(counts2)}')


if __name__ == '__main__':
    main()
