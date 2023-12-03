# Advent of code 2023
# Day 2: Cube Conundrum
# https://adventofcode.com/2023/day/2
import re
from collections import defaultdict

CUBES_MAX_VALUES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


if __name__ == "__main__":
    input_data = read_input()
    result_part_1 = 0
    result_part_2 = 0
    for line in input_data:
        game_info, cubes_info = line.replace(" ", "").split(":")
        game_number = int(re.findall(r"\d+", game_info)[0])
        iter_cubes = iter(
            list(
                filter(
                    None,
                    re.split(r"(\d+)", cubes_info.replace(";", "").replace(",", "")),
                )
            )
        )
        list_of_cubes = list(zip(iter_cubes, iter_cubes))
        cubes_dict = defaultdict(list)

        for number, colour in list_of_cubes:
            cubes_dict[colour].append(int(number))

        valid_set = True
        dice_multiplier = 1
        for colour in CUBES_MAX_VALUES.keys():
            dice_multiplier *= max(cubes_dict[colour])
            if max(cubes_dict[colour]) > CUBES_MAX_VALUES[colour]:
                valid_set = False

        if valid_set:
            result_part_1 += game_number

        result_part_2 += dice_multiplier

    print(f"Part 1: final result is {result_part_1}.")
    print(f"Part 2: final result is {result_part_2}.")
