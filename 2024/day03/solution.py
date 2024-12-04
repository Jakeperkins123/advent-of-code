from typing import List
import re


def read_input(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def part1(input: List) -> int:
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    total = 0
    for line in input:
        matches = re.findall(pattern, line)
        for match in matches:
            num1 = int(match[0])
            num2 = int(match[1])
            total += num1 * num2
    return total


def part2(input: List) -> int:
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
    total = 0
    add_flag = True
    for line in input:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "don't()":
                add_flag = False
                continue
            elif match == "do()":
                add_flag = True
                continue
            if add_flag:
                start = match.find("(") + 1
                end = match.find(")")
                nums = match[start:end].split(",")
                num1 = int(nums[0])
                num2 = int(nums[1])
                total += num1 * num2
    return total


if __name__ == "__main__":
    # Read input
    input_lines = read_input("input.txt")

    # Run solutions
    if input_lines:
        print("Part 1:", part1(input_lines))
        print("Part 2:", part2(input_lines))
