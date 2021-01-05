from collections import Counter
from typing import Tuple, List

from utils import read_input

Cell = Direction = Tuple[int, int, int]

DIRECTIONS = [
    (i, j, k)
    for i in (-1, 0, 1)
    for j in (-1, 0, 1)
    for k in (-1, 0, 1)
    if i or j or k
]


def _parse_lines(lines: List[str]) -> List[Cell]:
    return [
        (i, j, 0)
        for i, line in enumerate(lines)
        for j, char in enumerate(line)
        if char == '#'
    ]


def _shift_cells(cells: List[Cell], direction: Direction) -> List[Cell]:
    dx, dy, dz = direction
    return [(x + dx, y + dy, z + dz) for x, y, z in cells]


def _count_neighbors(cells: List[Cell]) -> Counter:
    return Counter([
        cell
        for direction in DIRECTIONS
        for cell in _shift_cells(cells, direction)
    ])


def _next_state(cells: List[Cell]) -> List[Cell]:
    neighbors = _count_neighbors(cells)
    return [
        cell
        for cell in neighbors.keys()
        if (cell in cells and neighbors[cell] in [2, 3])
           or (cell not in cells and neighbors[cell] == 3)
    ]


def simulate(starting_cells: List[Cell], cycles: int) -> List[Cell]:
    cells = starting_cells.copy()
    for _ in range(cycles):
        cells = _next_state(cells)
    return cells


def main():
    lines = read_input('./input.txt')
    cells = _parse_lines(lines)

    print(f'After 6 cycles there are {len(simulate(cells, 6))} active cells.')


if __name__ == '__main__':
    main()
