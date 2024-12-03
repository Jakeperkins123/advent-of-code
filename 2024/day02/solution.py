from typing import List


def read_input(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        return file.readlines()


def is_safe(reports: List) -> bool:
    is_ascending = True
    is_descending = True
    for i in range(len(reports) - 1):
        nxt = reports[i + 1]
        cur = reports[i]
        diff = nxt - cur
        if abs(diff) > 3 or abs(diff) < 1:
            return False
        if diff < 0:
            is_ascending = False
        if diff > 0:
            is_descending = False
    return is_ascending or is_descending


def part1(input: List) -> int:
    total_safe_reports = 0
    for line in input:
        line = line.strip()
        if not line:
            continue
        reports = list(map(int, line.split()))

        if is_safe(reports):
            total_safe_reports += 1

    return total_safe_reports


def part2(input: List) -> int:
    total_safe_reports = 0
    for line in input:
        line = line.strip()
        if not line:
            continue
        reports = list(map(int, line.split()))

        if is_safe(reports):
            total_safe_reports += 1
            continue

        # check if it can be safe by removing 1 report
        for i in range(len(reports)):
            trimmed_reports = reports[:i] + reports[i + 1 :]
            if is_safe(trimmed_reports):
                total_safe_reports += 1
                break

    return total_safe_reports


if __name__ == "__main__":
    # Read input
    input_lines = read_input("input.txt")

    # Run solutions
    if input_lines:
        print("Part 1:", part1(input_lines))
        print("Part 2:", part2(input_lines))
