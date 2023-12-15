import fileinput
from typing import List

# --- Day 9: Mirage Maintenance ---
# --- Part one ---

sample_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".split(
    "\n"
)


def extrapolate_next_value(sequence, mode: str = "part1"):
    start_index = -1 if mode == "part1" else 0
    sequence_values = []

    while any(diff != 0 for diff in sequence):
        sequence_values.append(sequence[start_index])

        new_sequence = [val2 - val1 for val1, val2 in zip(sequence[:-1], sequence[1:])]
        sequence = new_sequence

    if mode == "part1":
        return sum(sequence_values)
    else:
        next_value = 0
        for val in sequence_values[::-1]:
            next_value = val - next_value

        return next_value


def sum_of_extrapolated_values(raw_input: List[str], mode: str = "part1"):
    total_sum = 0

    for line in raw_input:
        values = list(map(int, line.split()))
        extrapolated_value = extrapolate_next_value(values, mode)
        total_sum += extrapolated_value

    return total_sum


assert sum_of_extrapolated_values(sample_input) == 114

puzzle_input = [line.rstrip() for line in fileinput.input()]
solution_part1 = sum_of_extrapolated_values(puzzle_input)

assert solution_part1 == 1995001648
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert sum_of_extrapolated_values(sample_input, mode="part2") == 2

solution_part2 = sum_of_extrapolated_values(puzzle_input, mode="part2")

assert solution_part2 == 988
print(f"solution part2: {solution_part2}")
