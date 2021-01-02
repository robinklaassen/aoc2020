from typing import List, Dict, Tuple, Optional

from utils import read_input

Location = Direction = Tuple[int, int]
Seats = Dict[Location, bool]
Neighbors = Dict[Location, List[Location]]


def _construct_seats(lines: List[str]) -> Tuple[Seats, int]:
    return {
               (i, j): False
               for i, line in enumerate(lines)
               for j, char in enumerate(line)
               if char == 'L'
           }, len(lines)


def _get_directions() -> List[Location]:
    return [
        (i, j)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if i or j
    ]


def _get_adjacent_locs(loc: Location) -> List[Location]:
    return [
        (loc[0] + i, loc[1] + j)
        for i, j in _get_directions()
    ]


def _construct_seat_neighbors_v1(seats: Seats) -> Neighbors:
    return {
        loc: [
            other_loc
            for other_loc in _get_adjacent_locs(loc)
            if other_loc in seats.keys()
        ]
        for loc in seats.keys()
    }


def _construct_seat_neighbors_v2(seats: Seats, grid_size: int) -> Neighbors:
    return {
        loc: [
            new_loc
            for dir_ in _get_directions()
            if (new_loc := _get_next_visible_seat(seats, grid_size, loc, dir_)) is not None
        ]
        for loc in seats.keys()
    }


def _get_next_visible_seat(seats: Seats,
                           grid_size: int,
                           loc: Location,
                           dir_: Direction) -> Optional[Location]:
    k = 0
    while True:
        k += 1
        new_loc = loc[0] + k * dir_[0], loc[1] + k * dir_[1]

        # Check for out of bounds
        if new_loc[0] < 0 or new_loc[0] >= grid_size or new_loc[1] < 0 or new_loc[1] >= grid_size:
            return None

        if new_loc in seats:
            return new_loc


def next_seat_state(seats: Seats, neighbors: Neighbors, tolerance: int = 4) -> Seats:
    new_seats = {}
    for loc, occupied in seats.items():
        occupied_neighbors = sum(seats[nb_loc] for nb_loc in neighbors[loc])
        flip_seat = True if (not occupied and occupied_neighbors == 0) or \
                            (occupied and occupied_neighbors >= tolerance) else False
        new_seats[loc] = not occupied if flip_seat else occupied
    return new_seats


def find_equilibrium(seats: Seats, neighbors: Neighbors, tolerance: int = 4) -> Seats:
    while True:
        new_seats = next_seat_state(seats, neighbors, tolerance)
        if new_seats == seats:
            return seats
        seats = new_seats.copy()


def main():
    lines = read_input('./input.txt')
    seats, grid_size = _construct_seats(lines)  # assume square grid

    neighbors = _construct_seat_neighbors_v1(seats)
    end_seats = find_equilibrium(seats, neighbors)
    print(f'In the equilibrium state, {sum(end_seats.values())} seats are taken.')

    # Part 2

    neighbors2 = _construct_seat_neighbors_v2(seats, grid_size)
    end_seats2 = find_equilibrium(seats, neighbors2, tolerance=5)

    print(f'Second part equilibrium state has {sum(end_seats2.values())} seats taken.')


if __name__ == '__main__':
    main()
