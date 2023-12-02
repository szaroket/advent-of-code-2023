# Advent of code 2023
# Day 2: Cube Conundrum
# https://adventofcode.com/2023/day/2
import re
from collections import defaultdict

CUBES_IN_BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = f.read().splitlines()
    return data


def solution_1() -> None:
    input_data = read_input()
    cubes_sum = 0
    for line in input_data:
        splitted_line = line.replace(" ", "").split(":")
        game_number = int(re.findall(r"\d+", splitted_line[0])[0])
        cubes_sets = splitted_line[1].replace(";", "").replace(",", "")
        iter_cubes = iter(list(filter(None, re.split(r'(\d+)', cubes_sets))))
        list_of_cubes = list(zip(iter_cubes, iter_cubes))
        number_of_cubes = len(list_of_cubes)
        correct_result = 0
        for cubes in list_of_cubes:
            if int(cubes[0]) <= CUBES_IN_BAG[cubes[1]]:
                correct_result += 1

        if correct_result == number_of_cubes:
            cubes_sum += int(game_number)

    print(f"Part 2: final result it {cubes_sum}")


def solution_2() -> None:
    input_data = read_input()
    result = 0
    for line in input_data:
        splitted_line = line.replace(" ", "").split(":")
        cubes_sets = splitted_line[1].replace(";", "").replace(",", "")
        iter_cubes = iter(list(filter(None, re.split(r'(\d+)', cubes_sets))))
        list_of_cubes = list(zip(iter_cubes, iter_cubes))
        cubes_dict = defaultdict(list)
        for number, color in list_of_cubes:
            cubes_dict[color].append(int(number))

        green_cubes = 0
        red_cubes = 0
        blue_cubes = 0
        cubes_sum = 0

        for red_number in cubes_dict["red"]:
            for blue_number in cubes_dict["blue"]:
                for green_number in cubes_dict["green"]:
                    if red_number + blue_number + green_number > cubes_sum:
                        cubes_sum = red_number + blue_number + green_number
                        green_cubes = green_number
                        red_cubes = red_number
                        blue_cubes = blue_number

        multiple = red_cubes * green_cubes * blue_cubes
        result += multiple
    print(f"Part 2: final result it {result}")


if __name__ == "__main__":
    solution_1()
    solution_2()
