import fileinput
from typing import List

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

EMPTY_SPACE = "."
GALAXY = "#"


class CosmicExpansion:
    def __init__(self, dat: List[str]):
        self.galaxy_numbers, self.rows, self.cols, self.empty_rows, self.empty_cols = CosmicExpansion.build(
            [list(line.strip()) for line in dat]
        )

    @staticmethod
    def build(universe):
        rows = len(universe)
        cols = len(universe[0])
        galaxy_numbers = {}
        current_number = 1
        empty_rows = set()
        empty_cols = set()

        for j in range(cols):
            empty_col = True
            for i in range(rows):
                actual_row = universe[i]
                if GALAXY not in actual_row and i not in empty_rows:
                    empty_rows.add(i)
                if universe[i][j] == GALAXY:
                    galaxy_numbers[(i, j)] = current_number
                    current_number += 1
                    empty_col = False
            if empty_col:
                empty_cols.add(j)

        return galaxy_numbers, rows, cols, empty_rows, empty_cols

    @staticmethod
    def get_min_max(a, b):
        return (b, a) if a > b else (a, b)

    def sum_of_shortest_paths(self, inflation: int = 2):
        result = 0
        galaxies_done = set()
        for galaxy1 in self.galaxy_numbers.keys():
            for galaxy2 in self.galaxy_numbers.keys():
                if galaxy1 == galaxy2 or ((galaxy1, galaxy2) in galaxies_done or (galaxy2, galaxy1) in galaxies_done):
                    continue

                galaxies_done.add((galaxy1, galaxy2))

                i1, j1 = galaxy1
                i2, j2 = galaxy2
                manhattan_distance = abs(i1 - i2) + abs(j1 - j2)

                mini, maxi = CosmicExpansion.get_min_max(i1, i2)
                minj, maxj = CosmicExpansion.get_min_max(j1, j2)

                manhattan_distance += sum(1 for empty_row in self.empty_rows if mini < empty_row < maxi) * (
                    inflation - 1
                )
                manhattan_distance += sum(1 for empty_col in self.empty_cols if minj < empty_col < maxj) * (
                    inflation - 1
                )

                result += manhattan_distance

        return result


assert CosmicExpansion(sample_input).sum_of_shortest_paths() == 374

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = CosmicExpansion(puzzle_input).sum_of_shortest_paths()

assert solution_part1 == 9370588
print(f"solution part1: {solution_part1}")

# --- Part two ---


assert CosmicExpansion(sample_input).sum_of_shortest_paths(inflation=10) == 1030
assert CosmicExpansion(sample_input).sum_of_shortest_paths(inflation=100) == 8410

solution_part2 = CosmicExpansion(puzzle_input).sum_of_shortest_paths(inflation=1000000)

assert solution_part2 == 746207878188
print(f"solution part2: {solution_part2}")
