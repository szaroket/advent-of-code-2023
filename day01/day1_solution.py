# Advent of code 2023
# Day 1: Trebuchet?!
# https://adventofcode.com/2023/day/1

import re

WORD_TO_NUMBER = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def replace_words(line: str, searched_word: str, to_replace: str) -> str:
    return line.replace(searched_word, to_replace)


if __name__ == "__main__":
    input_data = read_input()
    sum_1 = 0

    for line in input_data:
        digits = re.findall(r"\d", line)
        if len(digits) == 1:
            number = f"{digits[0]}{digits[0]}"
        else:
            number = f"{digits[0]}{digits[len(digits) - 1]}"
        sum_1 += int(number)

    print(f"Solution for part 1: {sum_1}")

    sum_2 = 0
    for line in input_data:
        for key, value in WORD_TO_NUMBER.items():
            line = replace_words(line, key, value)
        digits = re.findall(r"\d", line)
        if len(digits) == 1:
            number = f"{digits[0]}{digits[0]}"
        else:
            number = f"{digits[0]}{digits[len(digits) - 1]}"
        sum_2 += int(number)

    print(f"Solution for part 2: {sum_2}")
