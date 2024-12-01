from heapq import heappush, heappop
from collections import Counter
from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def part1(input: List[str]) -> int:

    h1, h2 = [], []

    for line in input:
        line = line.strip()
        if line:
            val1, val2 = map(int, line.split())
            heappush(h1, val1)
            heappush(h2, val2)

    total = 0
    while h1:
        total += abs(heappop(h1) - heappop(h2))
    return total


def part2(input: List[str]) -> int:

    l1, l2 = [], []
    for line in input:
        line = line.strip()
        if line:
            parts = line.split()
            l1.append(int(parts[0]))
            l2.append(int(parts[1]))

    counts = Counter(l2)
    total = sum(num * counts[num] for num in l1 if num in counts)
    return total


if __name__ == "__main__":
    # Read input
    input_lines = read_input("input.txt")

    # Run solutions
    if input_lines:
        print("Part 1:", part1(input_lines))
        print("Part 2:", part2(input_lines))
