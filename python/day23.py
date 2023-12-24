import fileinput
from collections import deque
from dataclasses import dataclass
from typing import List

# --- Day 23: A Long Walk ---
# --- Part one ---

sample_input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#""".split(
    "\n"
)


@dataclass(unsafe_hash=True)
class Position:
    x: int
    y: int


FILENAME = "input.txt"
PATH = "."
FOREST = "#"
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
SLOPES = "><v^"


def is_valid(grid, position):
    return 0 <= position.x < len(grid) and 0 <= position.y < len(grid[0]) and grid[position.x][position.y] != FOREST


def find_neighbours(grid, position):
    return [
        Position(position.x + row_offset, position.y + col_offset)
        for row_offset, col_offset in DIRECTIONS
        if is_valid(grid, Position(position.x + row_offset, position.y + col_offset))
    ]


def bfs(grid, start, intersections):
    distances = {}
    visited = set()
    queue = deque([(start, 0)])
    while queue:
        position, dist = queue.popleft()
        if position in intersections and position != start:
            distances[position] = dist
            continue
        for new_position in find_neighbours(grid, position):
            if new_position not in visited:
                visited.add(new_position)
                queue.append((new_position, dist + 1))
    return {start: distances}


def dfs(graph, start, end):
    stack = deque([(start, 0, {start})])
    max_distance = 0
    while stack:
        node, current_distance, visited = stack.pop()
        if node == end:
            max_distance = max(max_distance, current_distance)
            continue
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_distance = current_distance + weight
                new_visited = visited | {neighbor}
                stack.append((neighbor, new_distance, new_visited))
    return max_distance


class LongWalk:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.start = Position(0, grid[0].index(PATH))
        self.end = Position(len(grid) - 1, grid[-1].index(PATH))

    def find_longest_hike(
        self,
    ):
        slope_map = {slop: offset for slop, offset in zip(SLOPES, DIRECTIONS)}
        queue = deque([(self.start, set())])
        dist = 0
        while queue:
            position, visited = queue.popleft()
            if position == self.end and len(visited) > dist:
                dist = len(visited)
            elif self.grid[position.x][position.y] in SLOPES:
                row_offset, col_offset = slope_map[self.grid[position.x][position.y]]
                new_position = Position(position.x + row_offset, position.y + col_offset)
                if new_position not in visited:
                    queue.append((new_position, visited | {new_position}))
            else:
                for new_position in find_neighbours(self.grid, position):
                    if new_position not in visited:
                        queue.append((new_position, visited | {new_position}))
        return dist

    def find_longest_hike_extended(self):
        intersections = self.find_intersections()
        nodes = [self.start] + intersections + [self.end]

        graph = {}
        for node in nodes:
            graph |= bfs(self.grid, node, nodes)

        return dfs(graph, self.start, self.end)

    def find_intersections(self):
        intersections = []
        for i, row in enumerate(self.grid):
            for j, tile in enumerate(row):
                if tile != FOREST and len(find_neighbours(self.grid, Position(i, j))) > 2:
                    intersections.append(Position(i, j))
        return intersections


assert LongWalk(sample_input).find_longest_hike() == 94


puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = LongWalk(puzzle_input).find_longest_hike()

assert solution_part1 == 2406
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert LongWalk(sample_input).find_longest_hike_extended() == 154

solution_part2 = LongWalk(puzzle_input).find_longest_hike_extended()

assert solution_part2 == 6630
print(f"solution part2: {solution_part2}")
