from typing import List

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def read_input(file_path: str) -> List:
    with open(file_path, "r") as file:
        return [list(line.strip()) for line in file if line.strip()]


def get_start(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "^":
                return (row, col)


def oob(row, col):
    return row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0])


def part1(matrix, start):
    visited = set()
    direction = 0
    loc = start
    visited.add(start)
    while matrix[loc[0]][loc[1]] == "." or matrix[loc[0]][loc[1]] == "^":
        dir_vec = directions[direction]
        next_row = loc[0] + dir_vec[0]
        next_col = loc[1] + dir_vec[1]

        if oob(next_row, next_col):
            break
        elif matrix[next_row][next_col] == "#":
            direction = (direction + 1) % 4
            continue
        loc = (next_row, next_col)
        visited.add(loc)

    print(len(visited))


def is_cycle(matrix, start) -> bool:
    r, c = start
    direction = 0
    seen_states = set()
    initial_state = (r, c, direction)
    seen_states.add(initial_state)
    while True:
        # get the next direction that we're headed to
        dr, dc = directions[direction]
        next_r, next_c = r + dr, c + dc

        # if the next cell is out of bounds, we didn't find a cycle
        if next_r < 0 or next_r >= len(matrix) or next_c < 0 or next_c >= len(matrix[0]):
            return False
        # if the next cell is a wall, turn right and update the location
        if matrix[next_r][next_c] == "#":
            direction = (direction + 1) % 4
            state = (r, c, direction)
            if state in seen_states:
                return True
            seen_states.add(state)
            continue
        # if we have seen this row, col, and dir before, we have a cycle
        r, c = next_r, next_c
        state = (r, c, direction)
        if state in seen_states:
            return True
        # add the next cell to the seen set
        seen_states.add(state)


def part2(matrix, start):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])
    candidates = [(r, c) for r in range(rows) for c in range(cols) if (r, c) != start and matrix[r][c] == "."]
    for r, c in candidates:
        matrix[r][c] = "#"
        if is_cycle(matrix, start):
            count += 1
        matrix[r][c] = "."
    print(count)


if __name__ == "__main__":
    matrix = read_input("input.txt")
    start = get_start(matrix)
    part1(matrix, start)
    part2(matrix, start)
