from typing import List


def read_input(file_path: str) -> List:
    with open(file_path, "r") as file:
        matrix = [list(line.strip()) for line in file if line.strip()]
        return matrix


directions = [
    [0, -1],  # Left
    [1, -1],  # Down-Left
    [1, 0],  # Down
    [1, 1],  # Down-Right
    [0, 1],  # Right
    [-1, 1],  # Up-Right
    [-1, 0],  # Up
    [-1, -1],  # Up-Left
]


def part1(matrix: List) -> int:
    count = 0
    word = "XMAS"
    rows = len(matrix)
    cols = len(matrix[0])

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == word[0]:
                for dir in directions:
                    match = True
                    for i, char in enumerate(word):
                        nrow = row + i * dir[0]  # new col
                        ncol = col + i * dir[1]  # new row
                        if not in_bounds(nrow, ncol) or matrix[nrow][ncol] != char:
                            match = False
                            break

                    if match:
                        count += 1
    return count


def part2(matrix) -> int:
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    right_diag = [(-1, 1), (1, -1)]
    left_diag = [(-1, -1), (1, 1)]

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "A":
                match = True
                search_chars = set(["M", "S"])
                for dir in right_diag:
                    nrow = row + dir[0]
                    ncol = col + dir[1]
                    if not in_bounds(nrow, ncol):
                        match = False
                        break
                    elif matrix[nrow][ncol] not in search_chars:
                        match = False
                        break
                    else:
                        search_chars.remove(matrix[nrow][ncol])
                search_chars = set(["M", "S"])
                for dir in left_diag:
                    nrow = row + dir[0]
                    ncol = col + dir[1]
                    if not in_bounds(nrow, ncol):
                        match = False
                        break
                    elif matrix[nrow][ncol] not in search_chars:
                        match = False
                        break
                    else:
                        search_chars.remove(matrix[nrow][ncol])
                if match:
                    count += 1
    return count


if __name__ == "__main__":
    # Read input
    input_lines = read_input("input.txt")
    # Run solutions
    if input_lines:
        print("Part 1:", part1(input_lines))
        print("Part 2:", part2(input_lines))
