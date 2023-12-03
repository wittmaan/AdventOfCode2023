# --- Day 3: Gear Ratios ---
# --- Part one ---

import fileinput
from dataclasses import dataclass
from re import finditer
from typing import List, Dict

PERIOD = '.'

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split("\n")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


@dataclass
class Number:
    start: Coordinate
    end: Coordinate
    val: int

    def is_adjacent_to_symbol(self, symbol: Coordinate):
        x_range = range(self.start.x - 1, self.end.x + 2)
        y_range = range(self.start.y - 1, self.start.y + 2)
        return symbol.x in x_range and symbol.y in y_range


@dataclass
class Schematic:
    numbers: List[Number]
    symbols: Dict[Coordinate, str]

    def sum_part_number(self):
        result = []
        for number in self.numbers:
            for symbol in self.symbols:
                if number.is_adjacent_to_symbol(symbol):
                    result.append(number.val)
                    break
        return sum(result)


def fill(schematic_input: List[str]):
    numbers: List[Number] = []
    symbols: Dict[Coordinate, str] = {}

    for idy, line in enumerate(schematic_input):
        # fill numbers
        matches = finditer(r'\d+', line)
        for match in matches:
            numbers.append(Number(Coordinate(match.start(), idy), Coordinate(match.end() - 1, idy),
                                  int(line[match.start():match.end()])))
        # fill symbols
        for idx, symbol in enumerate(line):
            if not symbol.isdigit() and symbol != PERIOD:
                symbols[Coordinate(idx, idy)] = symbol

    return numbers, symbols


assert Schematic(*fill(schematic_input=sample_input)).sum_part_number() == 4361

puzzle_input = [line.rstrip() for line in fileinput.input()]
solution_part1 = Schematic(*fill(schematic_input=puzzle_input)).sum_part_number()

assert solution_part1 == 535078
print(f"solution part1: {solution_part1}")


# # --- Part two ---


# assert find_fewest_games(detect_games(sample_input)) == 2286
#
# solution_part2 = find_fewest_games(detect_games(puzzle_input))
# assert solution_part2 == 66681
# print(f"solution part2: {solution_part2}")
