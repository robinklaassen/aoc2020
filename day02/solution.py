import re
from typing import List, Tuple


def _read_input(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        out = f.readlines()
    return out


def _extract_params(line: str) -> Tuple[int, int, str, str]:
    match = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    if not match:
        raise ValueError(f'Line `{line}` does not match regex')
    return (
        int(match.group(1)),
        int(match.group(2)),
        match.group(3),
        match.group(4),
    )


def _validate_password(low: int, high: int, letter: str, password: str) -> bool:
    counts = password.count(letter)
    return low <= counts <= high


def _validate_password2(low: int, high: int, letter: str, password: str) -> bool:
    low_char = password[low - 1]
    high_char = password[high - 1]
    return (low_char == letter) != (high_char == letter)


def _extract_and_validate(line: str, version2: bool = False) -> bool:
    params = _extract_params(line)
    return _validate_password2(*params) if version2 else _validate_password(*params)


def main():
    lines = _read_input('./input.txt')
    valids = list(map(_extract_and_validate, lines))
    print(f'From {len(lines)} total passwords, {sum(valids)} are valid.')

    valids2 = [_extract_and_validate(line, version2=True) for line in lines]
    print(f'Using the second version, {sum(valids2)} are valid.')


if __name__ == "__main__":
    main()
