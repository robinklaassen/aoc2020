from typing import List, Tuple

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from utils import read_input


def count_diffs(numbers: List[int]) -> Tuple[int, int]:
    arr = np.array(numbers)
    diffs = np.diff(arr)
    num_ones = (diffs == 1).sum()
    num_threes = (diffs == 3).sum()
    return num_ones, num_threes


def construct_graph(numbers: List[int]) -> nx.DiGraph:
    graph = nx.DiGraph()
    graph.add_nodes_from(numbers)

    for n in numbers:
        for i in range(1, 4):
            if n + i in graph:
                graph.add_edge(n, n + i)

    return graph


def main():
    lines = read_input('./input.txt')
    numbers = [int(line) for line in lines]
    numbers.append(0)  # add charging outlet
    numbers.append(max(numbers) + 3)  # add device
    numbers.sort()

    num_ones, num_threes = count_diffs(numbers)
    print(f'Puzzle answer for part 1 is {num_ones * num_threes}.')

    # Part 2
    graph = construct_graph(numbers)

    # nx.draw(graph, with_labels=True)
    # plt.show()

    # Written down by hand, these nodes are always passed through
    essential_nodes = [0, 6, 22, 32, 37, 47, 51, 59, 69, 78, 90, 108, 112, 119, 126, 136, 146, 153, 163]

    total_num_paths = 1
    for i in range(len(essential_nodes) - 1):
        source = essential_nodes[i]
        target = essential_nodes[i + 1]
        path_gen = nx.all_simple_paths(graph, source=source, target=target)
        num_paths = len(list(path_gen))
        print(f'- {num_paths} paths between {source} and {target}')
        total_num_paths *= num_paths

    print(f'Total number of paths is {total_num_paths}.')


if __name__ == '__main__':
    main()
