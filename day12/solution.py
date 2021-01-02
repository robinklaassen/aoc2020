import re

from typing import List, Tuple

from utils import read_input

Instruction = Tuple[str, int]
Position = Tuple[int, int]

# define position as tuple(east-west, north-south)
DIRECTION_MOVEMENT = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0),
}


def _parse_lines(lines: List[str]) -> List[Instruction]:
    instructions = []
    for line in lines:
        result = re.search(r'([A-Z])(\d+)', line)
        instr = result.group(1), int(result.group(2))
        instructions.append(instr)
    return instructions


def _rotate(current_dir: str, way: str, degrees: int) -> str:
    assert current_dir in DIRECTION_MOVEMENT.keys()
    assert way in ['L', 'R']

    steps = degrees // 90
    sorted_dirs = ['N', 'E', 'S', 'W']
    if way == 'L':
        sorted_dirs.reverse()

    new_index = sorted_dirs.index(current_dir) + steps
    return sorted_dirs[new_index % len(sorted_dirs)]


def _rotate_waypoint(current_waypoint: Position, dir_: str, degrees: int) -> Position:
    x, y = current_waypoint
    steps = degrees // 90
    steps_right = steps if dir_ == 'R' else 4 - steps
    if steps_right == 1:
        return y, -x
    elif steps_right == 2:
        return -x, -y
    elif steps_right == 3:
        return -y, x
    else:
        raise ValueError(f"Don't know how to rotate {current_waypoint} by {dir_, degrees}")


def follow_instructions(instructions: List[Instruction]) -> Position:
    x, y = 0, 0
    current_dir = 'E'

    for char, num in instructions:
        if char in ['L', 'R']:
            current_dir = _rotate(current_dir, char, num)
        else:
            the_dir = current_dir if char == 'F' else char
            x_mov, y_mov = DIRECTION_MOVEMENT[the_dir]
            x += num * x_mov
            y += num * y_mov

    return x, y


def follow_instructions_2(instructions: List[Instruction]) -> Position:
    x, y = 0, 0
    way_x, way_y = 10, 1  # relative to the ship!

    for char, num in instructions:
        if dir_ := DIRECTION_MOVEMENT.get(char, False):
            # Move waypoint
            x_mov, y_mov = dir_
            way_x += num * x_mov
            way_y += num * y_mov
        elif char in ['L', 'R']:
            # Rotate waypoint
            way_x, way_y = _rotate_waypoint((way_x, way_y), char, num)
        elif char == 'F':
            # Move towards waypoint
            x += num * way_x
            y += num * way_y
        else:
            raise ValueError(f"Don't know what to do with instruction {char, num}.")

    return x, y


def main():
    lines = read_input('./input.txt')
    instructions = _parse_lines(lines)
    end_pos = follow_instructions(instructions)
    manh_dist = sum(abs(p) for p in end_pos)
    print(f'Final position after instructions is {end_pos}, the Manhattan distance is {manh_dist}.')

    end_pos_2 = follow_instructions_2(instructions)
    manh_dist_2 = sum(abs(p) for p in end_pos_2)
    print(f'With the second intepretation we arrive at {end_pos_2}, with distance {manh_dist_2}.')


if __name__ == '__main__':
    main()
