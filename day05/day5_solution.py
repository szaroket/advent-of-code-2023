# Advent of code 2023
# Day 5: If You Give A Seed A Fertilizer
# https://adventofcode.com/2023/day/5
import re
from collections import defaultdict


def read_input() -> list[str]:
    with open("input.txt", "r") as f:
        data = list(line for line in (l.strip() for l in f) if line)
    return data


def solution_part_1(
    seeds: list[int], maps: defaultdict[str, list[list[int]]]
) -> None:
    new_seeds = []
    for seed_idx, seed in enumerate(seeds):
        for key, values in maps.items():
            changed = False
            for (
                destination_range_start,
                source_range_start,
                range_length,
            ) in values:
                if (
                    source_range_start
                    <= seed
                    <= (source_range_start + range_length)
                    and not changed
                ):
                    seed = seed - source_range_start + destination_range_start
                    changed = True
        new_seeds.append(seed)

    result_1 = min(new_seeds)
    print(f"Part 1: the result is {result_1}.")


if __name__ == "__main__":
    input_data = read_input()
    maps = defaultdict(list)
    seeds = [int(number) for number in re.findall(r"\d+", input_data[0])]
    indices = [
        idx
        for idx, value in enumerate(input_data)
        if re.search(r"map:", value)
    ]
    for idx, position in enumerate(indices):
        map_name = input_data[position].replace(" map:", "")
        if idx == len(indices) - 1:
            for line_number in range(position + 1, len(input_data)):
                maps[map_name].append(
                    [
                        int(number)
                        for number in re.findall(
                            r"\d+", input_data[line_number]
                        )
                    ]
                )
        else:
            for line_number in range(position + 1, indices[idx + 1]):
                maps[map_name].append(
                    [
                        int(number)
                        for number in re.findall(
                            r"\d+", input_data[line_number]
                        )
                    ]
                )

    solution_part_1(seeds, maps)
