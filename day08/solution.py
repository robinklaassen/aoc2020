from typing import Tuple, List

from utils import read_input


def _parse_string(string: str) -> Tuple[str, int]:
    action, number = string.split(' ')
    return action, int(number)


def run_boot_code(code: List[Tuple[str, int]]) -> Tuple[int, int]:
    accumulator = 0
    index = 0
    passed_indices = []

    while True:
        # Stop if new instruction is already passed
        if index in passed_indices:
            exit_code = 1
            return exit_code, accumulator

        # Stop if new instruction is below last in code
        if index == len(code):
            exit_code = 0
            return exit_code, accumulator

        instr, num = code[index]
        passed_indices.append(index)

        # Execute instruction
        if instr == 'nop':
            index += 1
        elif instr == 'acc':
            accumulator += num
            index += 1
        elif instr == 'jmp':
            index += num
        else:
            raise ValueError(f'Got invalid instruction code `{instr}`.')


def test_code_mutations(base_code: List[Tuple[str, int]]) -> int:
    for i in range(len(base_code)):
        instr, num = base_code[i]

        if instr == 'jmp':
            mutated_code = base_code.copy()
            mutated_code[i] = 'nop', num
        elif instr == 'nop':
            mutated_code = base_code.copy()
            mutated_code[i] = 'jmp', num
        else:
            continue

        exit_code, final_acc = run_boot_code(mutated_code)
        if exit_code == 0:
            return final_acc


def main():
    lines = read_input('./input.txt')
    boot_code = [_parse_string(line) for line in lines]
    exit_code, final_acc = run_boot_code(boot_code)
    print(f'Running normal code, exits with code {exit_code}. Final accumulator value is {final_acc}.')

    # Part 2
    actual_acc = test_code_mutations(boot_code)
    print(f'Testing all code mutations, a correctly exiting one has final accumulator value {actual_acc}.')


if __name__ == '__main__':
    main()
