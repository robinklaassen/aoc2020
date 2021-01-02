import re
from typing import List

from utils import read_input


def apply_mask(mask: str, value: int) -> int:
    bval = f'{value:036b}'
    bout = ''
    for c, m in zip(bval, mask):
        bout += c if m == 'X' else m

    return int(bout, 2)


def decode_mem_address(mask: str, value: int) -> List[int]:
    bval = f'{value:036b}'
    masked_address = ''
    for c, m in zip(bval, mask):
        masked_address += c if m == '0' else m

    num_floating = masked_address.count('X')
    output_addresses = [masked_address]
    for _ in range(num_floating):
        new_output_addresses = []
        for addr in output_addresses:
            new_output_addresses.append(addr.replace('X', '0', 1))
            new_output_addresses.append(addr.replace('X', '1', 1))

        output_addresses = new_output_addresses.copy()

    return [int(addr, 2) for addr in output_addresses]


def main():
    lines = read_input('./input.txt')

    # Part 1
    mask = ''
    mem = dict()
    for line in lines:
        left, right = line.split(' = ')

        if left == 'mask':
            mask = right
            continue

        address = re.search(r'mem\[(\d+)\]', left).group(1)
        mem[address] = apply_mask(mask, int(right))

    print(f'Answer to part 1 is {sum(mem.values())}')

    # Part 2
    mask = ''
    mem = dict()
    for line in lines:
        left, right = line.split(' = ')

        if left == 'mask':
            mask = right
            continue

        input_addr = re.search(r'mem\[(\d+)\]', left).group(1)
        addresses = decode_mem_address(mask, int(input_addr))
        for a in addresses:
            mem[a] = int(right)

    print(f'Answer to part 2 is {sum(mem.values())}')


if __name__ == '__main__':
    main()
