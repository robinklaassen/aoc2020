from dataclasses import dataclass


def binary_reduce(string: str, lower: chr, upper: chr) -> int:
    numbers = list(range(2 ** len(string)))

    for char in string:
        if char == lower:
            numbers = numbers[:len(numbers) // 2]
        elif char == upper:
            numbers = numbers[len(numbers) // 2:]

    assert len(numbers) == 1
    return numbers[0]


@dataclass
class Seat:
    row: int
    col: int

    @classmethod
    def from_string(cls, string: str) -> 'Seat':
        row = binary_reduce(string[:7], 'F', 'B')
        col = binary_reduce(string[-3:], 'L', 'R')
        return Seat(row=row, col=col)

    @property
    def id(self):
        return self.row * 8 + self.col

    def __hash__(self):
        return hash(repr(self))


def main():
    with open('./input.txt', 'r') as f:
        lines = f.read().splitlines()

    seats = [Seat.from_string(line) for line in lines]
    seat_ids = [s.id for s in seats]
    print(f'Scanned {len(seats)} seats and found highest ID {max(seat_ids)}')

    for i in range(1024):
        if i not in seat_ids and i - 1 in seat_ids and i + 1 in seat_ids:
            my_id = i
            break

    print(f'My seat ID is {my_id}')


if __name__ == '__main__':
    main()
