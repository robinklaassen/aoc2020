from typing import List


def extend_numbers(numbers: List[int], limit: int) -> None:
    while len(numbers) < limit:
        last_num = numbers[-1]
        history = numbers[:-1]
        if last_num in history:
            index_last = next(i for i in reversed(range(len(history))) if history[i] == last_num)
            numbers.append(len(history) - index_last)
        else:
            numbers.append(0)

        if len(numbers) % 1000 == 0:
            print(f'-- now at {len(numbers)} numbers.')


def determine_nth_number(starting_numbers: List[int], n: int) -> int:
    """
    A more performing solution as this does not require backwards iteration over the history.
    """

    last_turns = dict()
    new_num = 0
    # Put in starting numbers
    for i, num in enumerate(starting_numbers[:-1]):
        last_turns[num] = i

    last_num = starting_numbers[-1]

    # Iterate forward
    for i in range(len(starting_numbers), n):
        new_num = (i - 1) - last_turns[last_num] if last_num in last_turns else 0
        last_turns[last_num] = i - 1

        last_num = new_num

        if i % 1e6 == 0:
            print(f'-- now at turn {i} with number {new_num}')

    return new_num


def main():
    numbers = [6, 3, 15, 13, 1, 0]

    # Part 1
    numbers1 = numbers.copy()
    extend_numbers(numbers1, 2020)
    print(f'The 2020th number is {numbers1[-1]}.')

    # Part 2
    final_num = determine_nth_number(numbers, 30_000_000)
    print(f'The 30 millionth number is {final_num}.')


if __name__ == '__main__':
    main()
