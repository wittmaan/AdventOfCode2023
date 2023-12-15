import fileinput
from collections import defaultdict

# --- Day 15: Lens Library ---
# --- Part one ---

DASH = "-"
EQUALS_SIGN = "="

sample_input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"


def hash_algorithm(input_string: str) -> int:
    current_value = 0
    for char in input_string:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value


assert hash_algorithm("HASH") == 52


def sum_of_results(initialization_sequence, mode: str = "part1"):
    steps = initialization_sequence.split(",")
    boxes = defaultdict(dict)

    for step in steps:
        operation_char = DASH if DASH in step else EQUALS_SIGN
        label, focal_length = step.split(operation_char)
        box = hash_algorithm(label)

        if operation_char == DASH:
            if label in boxes[box]:
                del boxes[box][label]
        else:
            boxes[box][label] = int(focal_length)

    if mode == "part1":
        total_sum = sum(hash_algorithm(step) for step in steps)
        return total_sum
    else:
        result = sum(
            (box_num + 1) * (lens_index + 1) * focal_length
            for box_num, lenses in boxes.items()
            for lens_index, focal_length in enumerate(lenses.values())
        )
        return result


assert sum_of_results(sample_input) == 1320

puzzle_input = [_.strip() for _ in fileinput.input()][0]
solution_part1 = sum_of_results(puzzle_input)

assert solution_part1 == 512797
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert sum_of_results(sample_input, mode="part2") == 145

solution_part2 = sum_of_results(puzzle_input, mode="part2")

assert solution_part2 == 262454
print(f"solution part2: {solution_part2}")
