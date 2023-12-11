import fileinput
from itertools import combinations
from typing import List

import numpy as np

# --- Day 11: Cosmic Expansion ---
# --- Part one ---


sample_input = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split(
    "\n"
)

EMPTY_SPACE = '.'
GALAXY = '#'


class CosmicExpansion:
    def __init__(self, dat: List[str], inflation: int = 2):
        self.universe = CosmicExpansion.expand([list(line.strip()) for line in dat], inflation)
        self.rows = len(self.universe)
        self.cols = len(self.universe[0])
        self.galaxy_numbers = self.assign_numbers()

    @staticmethod
    def expand(universe, inflation: int = 2):
        expanded_universe = CosmicExpansion.transpose_matrix(CosmicExpansion.expand_row(universe, inflation))
        expanded_universe = CosmicExpansion.transpose_matrix(CosmicExpansion.expand_row(expanded_universe, inflation))
        return expanded_universe

    def assign_numbers(self):
        galaxy_numbers = {}
        current_number = 1
        for i in range(self.rows):
            for j in range(self.cols):
                if self.universe[i][j] == GALAXY:
                    galaxy_numbers[(i, j)] = current_number
                    current_number += 1
        return galaxy_numbers

    @staticmethod
    def expand_row(universe, inflation: int = 2):
        expanded_universe = []
        for row in universe:
            if len(set(row)) == 1:
                expanded_universe.extend([row] * (inflation - 1))
            expanded_universe.append(row)
        return expanded_universe

    @staticmethod
    def transpose_matrix(matrix):
        transposed = list(map(list, zip(*matrix)))
        return transposed

    def print(self):
        for row in self.universe:
            print("".join([_ for _ in row]))

    def sum_of_shortest_paths(self):
        # possible_paths = [_ for _ in combinations(self.galaxy_numbers.keys(), 2)]
        # manhattan_distances = [abs(x2 - x1) + abs(y2 - y1) for (x1, y1), (x2, y2) in possible_paths]
        # return sum(manhattan_distances)
        galaxy_positions = np.array(list(self.galaxy_numbers.keys()))
        possible_paths = np.array(list(combinations(galaxy_positions, 2)))
        manhattan_distances = np.sum(np.abs(possible_paths[:, 1] - possible_paths[:, 0]), axis=1)
        return int(np.sum(manhattan_distances))


assert CosmicExpansion(sample_input).sum_of_shortest_paths() == 374

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = CosmicExpansion(puzzle_input).sum_of_shortest_paths()

assert solution_part1 == 9370588
print(f"solution part1: {solution_part1}")

# --- Part two ---


assert CosmicExpansion(sample_input, inflation=10).sum_of_shortest_paths() == 1030
assert CosmicExpansion(sample_input, inflation=100).sum_of_shortest_paths() == 8410

solution_part2 = CosmicExpansion(puzzle_input, inflation=1000000).sum_of_shortest_paths()

# assert solution_part1 == 9370588
print(f"solution part2: {solution_part2}")
