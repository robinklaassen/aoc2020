from typing import List, Optional

from utils import read_input


def _sum_exists(preamble: List[int], target: int) -> bool:
    for i in preamble:

        # Prevent using same number twice
        if i * 2 == target:
            continue

        if target - i in preamble:
            return True

    return False


def find_first_invalid(numbers: List[int], preamble_size: int) -> int:
    for i in range(preamble_size, len(numbers)):
        preamble = numbers[i - preamble_size:i]
        target = numbers[i]
        if not _sum_exists(preamble, target):
            print(f'-- invalid number {target} found at index {i}')
            return target

    raise ValueError(f'No invalid target found in sequence.')


def _contiguous_sum(numbers: List[int], target: int) -> Optional[List[int]]:
    sum_ = 0
    for i, n in enumerate(numbers):
        sum_ += n

        if sum_ == target:
            return numbers[:i + 1]
        elif sum_ > target:
            return None


def find_contiguous_sum(numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        result = _contiguous_sum(numbers[i:], target)
        if result is not None:
            return result


def main():
    lines = read_input('./input.txt')
    numbers = [int(line) for line in lines]
    invalid_number = find_first_invalid(numbers, 25)
    print(f'First invalid number encountered is {invalid_number}.')

    contiguous_seq = find_contiguous_sum(numbers, target=invalid_number)
    print(f'Sequence found is {contiguous_seq}, sums up to {sum(contiguous_seq)}')
    print(f'Puzzle answer is {min(contiguous_seq) + max(contiguous_seq)}.')


if __name__ == '__main__':
    main()
