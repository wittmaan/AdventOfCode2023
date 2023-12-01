import fileinput
import re
from typing import List

# --- Day 1: Trebuchet?! ---
# --- Part one ---

sample_input1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".split(
    "\n"
)

sample_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".split("\n")

DIGITS = "1234567890"

WORD_TO_DIGIT = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def extract_digits(line: str) -> int:
    digits = re.findall(r'\d', line)
    return int(digits[0] + digits[-1])


def words_to_digits(line) -> int:
    result = []
    for idx, char in enumerate(line):
        if char.isdigit():
            result.append(char)
        for word, digit in WORD_TO_DIGIT.items():
            if line[idx:].startswith(word):
                result.append(digit)
                break
    return "".join(result)


def get_sum_calibration_values(dat: List[str], mode: str = "part1") -> int:
    if mode == "part1":
        return sum([extract_digits(val) for val in dat])
    else:
        values = 0
        for line in dat:
            values += extract_digits(words_to_digits(line))
        return values


assert get_sum_calibration_values(sample_input1) == 142

puzzle_input = ("".join([_ for _ in fileinput.input()])).split("\n")
solution_part1 = get_sum_calibration_values(puzzle_input)

assert solution_part1 == 54916
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert get_sum_calibration_values(sample_input2, mode="part2") == 281

solution_part2 = get_sum_calibration_values(puzzle_input, mode="part2")
assert solution_part2 == 54728
print(f"solution part2: {solution_part2}")
