import fileinput
from collections import defaultdict
from heapq import heappop, heappush
from math import inf
from typing import List, Optional

# --- Day 17: Clumsy Crucible ---
# --- Part one ---

sample_input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".split(
    "\n"
)


def dijkstra(grid: List[str], min_dist: int, max_dist: int) -> Optional[int]:
    rows, cols = len(grid), len(grid[0])
    distances = defaultdict(lambda: inf)
    heap = [(0, (0, 0, (0, 1))), (0, (0, 0, (1, 0)))]
    visited = set()

    while heap:
        current_cost, (current_row, current_col, direction) = heappop(heap)

        if (current_row, current_col, direction) in visited:
            continue

        visited.add((current_row, current_col, direction))

        if (current_row, current_col) == (rows - 1, cols - 1):
            return current_cost

        if current_cost > distances[current_row, current_col, direction]:
            continue

        direction_row, direction_col = direction

        for new_direction_row, new_direction_col in ((-direction_col, direction_row), (direction_col, -direction_row)):
            new_cost = current_cost

            for dist in range(1, max_dist + 1):
                new_row, new_col = current_row + new_direction_row * dist, current_col + new_direction_col * dist

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    new_cost += int(grid[new_row][new_col])

                    if dist < min_dist:
                        continue

                    new_key = (new_row, new_col, (new_direction_row, new_direction_col))
                    if new_cost < distances[new_key]:
                        distances[new_key] = new_cost
                        heappush(heap, (new_cost, new_key))
    return None


assert dijkstra(sample_input, 1, 3) == 102

puzzle_input = [_.strip() for _ in fileinput.input()]
solution_part1 = dijkstra(puzzle_input, 1, 3)

assert solution_part1 == 859
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert dijkstra(sample_input, 4, 10) == 94

solution_part2 = dijkstra(puzzle_input, 4, 10)

assert solution_part2 == 1027
print(f"solution part2: {solution_part2}")
