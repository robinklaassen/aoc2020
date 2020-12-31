from typing import List


def read_input(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    return lines
