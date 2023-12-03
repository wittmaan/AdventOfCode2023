import fileinput
from typing import List

# --- Day 2: Cube Conundrum ---
# --- Part one ---

sample_input1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".split(
    "\n"
)

sample_input2 = """Game 1: 4 red, 1 green, 15 blue; 6 green, 2 red, 10 blue; 7 blue, 6 green, 4 red; 12 blue, 10 green, 3 red
Game 2: 3 green, 18 blue; 14 green, 4 red, 2 blue; 3 red, 14 green, 15 blue
Game 3: 12 green, 2 blue; 9 green; 1 red, 11 blue, 4 green""".split("\n")

CUBE_COUNTS = {'red': 12, 'green': 13, 'blue': 14}


def detect_games(games_input: List[str]):
    result = {}

    for game in games_input:
        key, values_str = map(str.strip, game.split(":"))
        values_list = values_str.split(";")
        cubes_set = []

        for value in values_list:
            cube_values = value.split(",")
            cube_data = {cube.split()[1].strip(): int(cube.split()[0].strip()) for cube in cube_values}
            cubes_set.append(cube_data)

        result[key] = cubes_set

    return result


def is_possible_game(game):
    for subset in game:
        if not check_set(subset):
            return False
    return True


def check_set(subset):
    current_counts = {"blue": 0, "green": 0, "red": 0}
    for color, count in subset.items():
        current_counts[color] += count
    for color in current_counts:
        if current_counts[color] > CUBE_COUNTS[color]:
            return False
    return True


def find_possible_games(games):
    possible_games = []
    for idx, game in games.items():
        if is_possible_game(game):
            possible_games.append(int(idx.split()[1]))
    return possible_games


assert sum(find_possible_games(detect_games(sample_input1))) == 8
assert sum(find_possible_games(detect_games(sample_input2))) == 3

puzzle_input = [line.rstrip() for line in fileinput.input()]
solution_part1 = sum(find_possible_games(detect_games(puzzle_input)))

assert solution_part1 == 2237
print(f"solution part1: {solution_part1}")


# # --- Part two ---


def check_max_val(subset, current_counts):
    for color, count in subset.items():
        current_counts[color] = max(current_counts[color], count)
    return current_counts


def find_fewest_games(games):
    total_sum = 0

    for game in games.values():
        current_counts = {"blue": 0, "green": 0, "red": 0}

        for subset in game:
            current_counts = check_max_val(subset, current_counts)

        power = 1
        for count in current_counts.values():
            power *= count

        total_sum += power

    return total_sum


assert find_fewest_games(detect_games(sample_input1)) == 2286

solution_part2 = find_fewest_games(detect_games(puzzle_input))
assert solution_part2 == 66681
print(f"solution part2: {solution_part2}")
