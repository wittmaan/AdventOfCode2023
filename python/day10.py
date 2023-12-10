import fileinput
from typing import List, Tuple

# --- Day 10: Pipe Maze ---
# --- Part one ---

sample_input = """.....
.S-7.
.|.|.
.L-J.
.....""".split(
    "\n"
)

UP, DOWN, LEFT, RIGHT = DIRECTIONS = (0, -1), (0, 1), (-1, 0), (1, 0)

PIPES = {'|': (UP, DOWN), '-': (LEFT, RIGHT), '7': (LEFT, DOWN),
         'J': (LEFT, UP), 'L': (UP, RIGHT), 'F': (RIGHT, DOWN)}


class Grid:
    def __init__(self, dat: List[str]):
        self.rows = len(dat)
        self.cols = len(dat[0])
        self.grid, self.starting_position = self.fill(dat)

    def fill(self, dat: List[str]) -> Tuple[dict, Tuple[int, int]]:
        grid = {}
        starting_position = None
        for j in range(self.rows):
            for i in range(self.cols):
                grid[(i, j)] = [(i + di, j + dj) for di, dj in PIPES.get(dat[j][i], ())]
                if dat[j][i] == 'S':
                    si, sj = starting_position = i, j

        grid[starting_position] = [(si + di, sj + dj) for di, dj in DIRECTIONS
                                   if starting_position in grid.get((si + di, sj + dj), [])]
        return grid, starting_position

    def find_longest_distance(self) -> int:
        return len(self.find_loop()) // 2

    def find_loop(self) -> List[Tuple[int, int]]:
        path = [self.starting_position]
        next_position = self.grid[self.starting_position][0]
        while next_position != self.starting_position:
            path.append(next_position)
            next_position = next(nb for nb in self.grid[next_position] if nb != path[-2])
        return path

    def count_enclosed_tiles(self) -> int:
        loop = self.find_loop()
        n = len(loop)
        x, y = zip(*loop)
        # Shoelace formula
        area = int(0.5 * abs(sum(x[i] * y[(i + 1) % n] - x[(i + 1) % n] * y[i] for i in range(n))))
        # Pick's theorem
        return area - n // 2 + 1


assert Grid(sample_input).find_longest_distance() == 4

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = Grid(puzzle_input).find_longest_distance()

assert solution_part1 == 6867
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert Grid(sample_input).count_enclosed_tiles() == 1

solution_part2 = Grid(puzzle_input).count_enclosed_tiles()

assert solution_part2 == 595
print(f"solution part2: {solution_part2}")
