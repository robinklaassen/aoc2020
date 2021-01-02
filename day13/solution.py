from typing import List, Tuple, Dict

from utils import read_input


def _parse_lines(lines: List[str]) -> Tuple[int, List[str]]:
    start_time = int(lines[0])
    buses = lines[1].split(',')
    return start_time, buses


def _get_key_by_value(dict_: Dict[int, int], value: int) -> int:
    for key, val in dict_.items():
        if val == value:
            return key
    raise ValueError(f'Value {value} not in given dict')


def main():
    lines = read_input('./input.txt')
    start_time, buses = _parse_lines(lines)

    # Part 1
    actual_buses = [int(b) for b in buses if b != 'x']
    next_times = {
        bus: (bus - start_time % bus)
        for bus in actual_buses
    }
    shortest_time = min(next_times.values())
    bus_to_take = _get_key_by_value(next_times, shortest_time)
    print(f'Take bus {bus_to_take} in {shortest_time} minutes, puzzle answer is {bus_to_take * shortest_time}.')

    # Part 2
    timestamp = 0
    increment = actual_buses[0]
    for offset, bus in enumerate(buses):
        if bus == 'x' or offset == 0:
            continue

        bus = int(bus)
        while True:
            timestamp += increment
            if (timestamp + offset) % bus == 0:
                print(f'Found timestamp {timestamp} for bus {bus} with offset {offset}')
                break

        increment *= bus

    print(f'First timestamp with the stupid requirement is {timestamp}.')


if __name__ == '__main__':
    main()
