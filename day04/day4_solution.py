# Advent of code 2023
# Day 4: Scratchcards
# https://adventofcode.com/2023/day/4


import re
from collections import Counter, defaultdict


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


if __name__ == "__main__":
    input_data = read_input()
    result = 0
    cards = defaultdict(int)
    for card_number, line in enumerate(input_data, 1):
        cards[card_number] += 1
        all_numbers = re.sub(r"Card +\d+:", "", line)
        all_numbers_list = [
            int(number) for number in re.findall(r"\d+", all_numbers)
        ]
        counter_numbers = Counter(all_numbers_list)
        how_many_winning_numbers = len(
            [number for number in counter_numbers.values() if number == 2]
        )
        points = 0
        if how_many_winning_numbers != 0:
            points = pow(2, how_many_winning_numbers - 1)
            number_of_operations = cards[card_number]
            for operation in range(number_of_operations):
                for idx in range(
                    card_number + 1, card_number + 1 + how_many_winning_numbers
                ):
                    cards[idx] += 1
        result += points

    print(f"Part 1: result it {result}.")

    results_2 = sum(cards.values())
    print(f"Part 2: result it {results_2}.")
