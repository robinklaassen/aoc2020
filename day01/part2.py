from typing import List


def _get_input(input_path: str) -> List[int]:
    with open(input_path, 'r') as f:
        out = f.readlines()

    return list(map(int, out))


def main():
    numbers = _get_input('./input.txt')
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if i + j + k == 2020:
                    break
            else:
                continue
            break
        else:
            continue
        break

    print(f'Found numbers {i} and {j} and {k}, sums to {i + j + k}, their multiple is {i * j * k}')


if __name__ == "__main__":
    main()
