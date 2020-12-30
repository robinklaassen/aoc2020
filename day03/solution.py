from typing import List
from functools import reduce


class CircularList(list):
    """
    Very nicely stolen from https://stackoverflow.com/questions/37702651/periodic-list-in-python
    """

    def __getitem__(self, idx):
        return super(CircularList, self).__getitem__(idx % len(self))


def _read_input(filepath: str) -> List[CircularList]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    return [CircularList([c for c in line]) for line in lines]


def _count_trees(lines: List[CircularList], right: int, down: int) -> int:
    trees = 0
    i, j = 0, 0  # starting position

    while True:
        # Try next position
        i, j = i + down, j + right
        if i >= len(lines):
            break

        if lines[i][j] == '#':
            trees += 1

    return trees


def main():
    lines = _read_input('./input.txt')
    print(f'Number of trees for right 3 down 1 is {_count_trees(lines, 3, 1)}')

    # Part 2
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees_per_slope = [_count_trees(lines, *tup) for tup in slopes]
    print(f"Number of trees per slope: {trees_per_slope}")

    print(f"Their multiple is {reduce(lambda x, y: x * y, trees_per_slope)}")


if __name__ == "__main__":
    main()
