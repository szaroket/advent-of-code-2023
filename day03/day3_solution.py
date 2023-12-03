# Advent of code 2023
# Day 3: Gear Ratios
# https://adventofcode.com/2023/day/3
import itertools
import math
import re

NUMBERS = "01234566789."


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


if __name__ == "__main__":
    board = read_input()
    board_len = len(board)
    # get coordinates of all symbols
    symbols = {
        (row, col): []
        for row in range(board_len)
        for col in range(board_len)
        if board[row][col] not in NUMBERS
    }

    for row_index, line in enumerate(board):
        for number in re.finditer(r"\d+", line):
            dist = number.end() - number.start()
            # get coordinates of all edges
            edges = set(
                [
                    (row, dy)
                    for row in (row_index - 1, row_index, row_index + 1)
                    for (dx, dy) in itertools.product(
                        range(number.start() - 1, number.end() + 1), repeat=2
                    )
                ]
            )

            for edge in edges:
                if edge in symbols.keys():
                    symbols[edge].append(int(number.group()))

    result_part_1 = sum(sum(numbers) for numbers in symbols.values())
    print(f"Part 1: result is {result_part_1}.")
    result_part_2 = sum(
        math.prod(numbers) for numbers in symbols.values() if len(numbers) == 2
    )
    print(f"Part 2: result is {result_part_2}.")
