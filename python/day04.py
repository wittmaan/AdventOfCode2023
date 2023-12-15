import fileinput
from collections import Counter
from dataclasses import dataclass, field
from typing import List

# --- Day 4: Scratchcards ---
# --- Part one ---

sample_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".split(
    "\n"
)


@dataclass
class ScratchCard:
    card_number: int
    winning_numbers: List[int]
    your_numbers: List[int]

    def get_common_numbers(self):
        winning_numbers_counter = Counter(self.winning_numbers)
        your_numbers_counter = Counter(self.your_numbers)
        return winning_numbers_counter & your_numbers_counter
        # common_numbers = (winning_numbers_counter & your_numbers_counter).elements()
        # return common_numbers

    def get_points(self):
        common_numbers = (self.get_common_numbers()).elements()
        points = sum(1 for _ in common_numbers)
        return 2 ** (points - 1) if points > 0 else 0


class Scratchcards:
    def __init__(self, dat: List[str]):
        self.cards: List[ScratchCard] = Scratchcards.parse(dat)

    @staticmethod
    def parse(dat):
        result = []
        for card_data in dat:
            card_number, numbers_str = card_data.split(":")
            card_number = int(card_number.split()[-1])
            winning_numbers, your_numbers = map(lambda x: list(map(int, x.split())), numbers_str.split("|"))
            result.append(ScratchCard(card_number, winning_numbers, your_numbers))
        return result

    def total_points(self):
        return sum([_.get_points() for _ in self.cards])

    def total_scratchcards(self):
        won_cards = {}
        for card in self.cards:
            won_cards[card.card_number] = list(
                range(card.card_number + 1, card.card_number + 1 + len(card.get_common_numbers()))
            )

        scratchcards_count = {}
        for card_number, cards in reversed(won_cards.items()):
            scratchcards_count[card_number] = [card_number]
            for card in cards:
                scratchcards_count[card_number].extend(scratchcards_count[card])

        return sum(len(v) for v in scratchcards_count.values())


assert Scratchcards(sample_input).total_points() == 13

puzzle_input = [line.rstrip() for line in fileinput.input()]
solution_part1 = Scratchcards(puzzle_input).total_points()

assert solution_part1 == 23028
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert Scratchcards(sample_input).total_scratchcards() == 30

solution_part2 = Scratchcards(puzzle_input).total_scratchcards()

assert solution_part2 == 9236992
print(f"solution part2: {solution_part2}")
