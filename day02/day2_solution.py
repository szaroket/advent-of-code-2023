# Advent of code 2023
# Day 2: Cube Conundrum
# https://adventofcode.com/2023/day/2
import re

CUBES_IN_BAG = {
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
    sum = 0
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
            sum += int(game_number)
            print(f"Game {game_number} is possible!")

    print(f"Final result is {sum}.")
