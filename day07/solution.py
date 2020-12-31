import re
from typing import List, Tuple, Optional, Dict

import networkx as nx

relation = Tuple[str, Optional[Dict[str, int]]]


def _read_input(filepath: str) -> List[str]:
    with open(filepath, 'r') as f:
        lines = f.read().splitlines()
    return lines


def _parse_string(string: str) -> relation:
    result = re.search(r'(.+) bags contain (.+)\.', string)
    parent = result.group(1)
    children = result.group(2)

    if children == 'no other bags':
        return parent, None

    child_counts = dict()
    for child_string in children.split(', '):
        result2 = re.search(r'(\d+) (.+) bag', child_string)
        child_count = int(result2.group(1))
        child_type = result2.group(2)
        child_counts[child_type] = child_count

    return parent, child_counts


def _construct_graph(relations: List[relation]) -> nx.DiGraph:
    graph = nx.DiGraph()
    for parent, children in relations:
        graph.add_node(parent)

        if not children:
            continue

        for child_type, child_count in children.items():
            graph.add_node(child_type)
            graph.add_edge(parent, child_type, count=child_count)
    return graph


def _graph_from_input(filepath: str) -> nx.DiGraph:
    lines = _read_input(filepath)
    relations = [_parse_string(line) for line in lines]
    return _construct_graph(relations)


def count_contains(bag_type: str, bag_count: int, relations: List[relation]) -> int:
    rel = next(filter(lambda r: r[0] == bag_type, relations))
    if rel[1] is None:
        return 0

    count = 0
    for subbag_type, subbag_count in rel[1].items():
        count += subbag_count
        count += subbag_count * count_contains(subbag_type, subbag_count, relations)
    return count


def main():
    graph = _graph_from_input('./input.txt')
    target = 'shiny gold'
    paths = [nx.has_path(graph, n, target) for n in graph if n != target]
    print(f'From {len(graph)} bag types, {sum(paths)} lead to shiny gold bag.')

    # Part 2, without graph
    lines = _read_input('./input.txt')
    relations = [_parse_string(line) for line in lines]
    num_contained_bags = count_contains(target, 1, relations)
    print(f'One shiny gold bag contains in total {num_contained_bags} other bags.')


if __name__ == '__main__':
    main()
