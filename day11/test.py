from unittest import TestCase

from day11.solution import _construct_seats, _construct_seat_neighbors_v1, find_equilibrium, \
    _construct_seat_neighbors_v2
from utils import read_input


class Day11TestSuite(TestCase):

    def test_part1(self):
        lines = read_input('./test_input.txt')
        seats, grid_size = _construct_seats(lines)
        neighbors = _construct_seat_neighbors_v1(seats)

        end_seats = find_equilibrium(seats, neighbors)
        self.assertEqual(37, sum(end_seats.values()))

    def test_part2(self):
        lines = read_input('./test_input.txt')
        seats, grid_size = _construct_seats(lines)
        neighbors = _construct_seat_neighbors_v2(seats, grid_size)

        end_seats = find_equilibrium(seats, neighbors, tolerance=5)
        self.assertEqual(26, sum(end_seats.values()))
