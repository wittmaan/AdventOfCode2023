import fileinput
from collections import Counter

# --- Day 7: Camel Cards ---
# --- Part one ---

sample_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split(
    "\n"
)


def count_ranks(hand: str, mode: str = "part1") -> list[int]:
    if mode == "part1":
        return sorted(Counter(hand).values(), reverse=True)
    else:
        if "J" in hand and hand != "JJJJJ":
            highest = max(hand.replace("J", ""), key=hand.replace("J", "").count)
            hand = hand.replace("J", highest)
        return sorted(list(hand.count(c) for c in set(hand)), reverse=True)


def map_values_to_ranks(hand: str, mode: str = "part1") -> list[int]:
    card_values = [str(value) for value in range(2, 10)] + ["T", "J", "Q", "K", "A"]
    if mode != "part1":
        card_values = ["J"] + card_values
    return [card_values.index(char) for char in hand]


def calculate_winnings(hands_bids: list[str], mode: str = "part1") -> int:
    hands = [hand_bid.split() for hand_bid in hands_bids]
    sorted_hands = sorted(hands, key=lambda x: (count_ranks(x[0], mode), map_values_to_ranks(x[0], mode)))
    result = sum(rank * int(bid) for rank, (hand, bid) in enumerate(sorted_hands, start=1))

    return result


assert calculate_winnings(sample_input) == 6440

puzzle_input = [line.rstrip() for line in fileinput.input()]
solution_part1 = calculate_winnings(puzzle_input)

assert solution_part1 == 251927063
print(f"solution part1: {solution_part1}")

# --- Part two ---

assert calculate_winnings(sample_input, mode="part2") == 5905

solution_part2 = calculate_winnings(puzzle_input, mode="part2")

print(f"solution part1: {solution_part2}")
