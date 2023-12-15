import fileinput
from math import ceil, sqrt
from typing import List

# --- Day 6: Wait For It ---
# --- Part one ---

sample_input = """Time:      7  15   30
Distance:  9  40  200""".split(
    "\n"
)


def parse(raw_input: List[str], mode: str = "part1") -> tuple[List[int], List[int]]:
    times = list(map(int, raw_input[0].split()[1:]))
    distances = list(map(int, raw_input[1].split()[1:]))
    if mode == "part2":
        times = [int("".join(map(str, times)))]
        distances = [int("".join(map(str, distances)))]
    return times, distances


def calc_ways_to_beat_record(time, distance, mode: str = "part1") -> int:
    if mode == "part1":
        return sum(1 for hold_time in range(time + 1) if hold_time * (time - hold_time) > distance)
    else:
        t = ceil((time - sqrt(time**2 - 4 * distance)) / 2)
        return time + 1 - 2 * t


def calc_per_race(raw_input: List[str], mode: str = "part1") -> int:
    total_ways = 1
    times, distances = parse(raw_input, mode)
    for time, distance in zip(times, distances):
        total_ways *= calc_ways_to_beat_record(time, distance)

    return total_ways


assert calc_per_race(sample_input) == 288

puzzle_input = [line.rstrip() for line in fileinput.input()]
solution_part1 = calc_per_race(puzzle_input)

assert solution_part1 == 3316275
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert calc_per_race(sample_input, mode="part2") == 71503

solution_part2 = calc_per_race(puzzle_input, mode="part2")

assert solution_part2 == 27102791
print(f"solution part2: {solution_part2}")
