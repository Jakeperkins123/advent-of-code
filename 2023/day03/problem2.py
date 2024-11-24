directions = [
    [-1, 0],  # up
    [-1, 1],  # upper right
    [0, 1],  # right
    [1, 1],  # bottom right
    [1, 0],  # down
    [1, -1],  # bottom left
    [0, -1],  # left
    [-1, -1],  # upper left
]
total = 0
already_checked = {}  # {key: [y,x] coord


#   val: char (doesn't matter)
#  }
def oob(row, col) -> bool:
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return True
    return False


def get_unique(matrix, row, col) -> list[int]:
    # Check for valid inputs
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return []

    unique = []
    for dir in directions:
        new_row = dir[0] + row
        new_col = dir[1] + col

        if matrix[new_row][new_col].isdigit():
            s = ""
            scan_col = new_col

            while not oob(new_row, scan_col) and matrix[new_row][scan_col].isdigit():
                s = matrix[new_row][scan_col] + s
                scan_col -= 1
            start_coords = (new_row, scan_col + 1)
            if start_coords in already_checked:
                continue
            scan_col = new_col
            scan_col += 1

            while not oob(new_row, scan_col) and matrix[new_row][scan_col].isdigit():
                s += matrix[new_row][scan_col]
                scan_col += 1

            whole_num = int(s)
            already_checked[start_coords] = whole_num
            unique.append(whole_num)
    return unique


with open("input.txt", "r") as file:
    matrix = []
    for line in file:
        if not line.strip():
            continue
        matrix.append(list(line.strip()))

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            cur = matrix[row][col]
            touching = []

            if not cur.isdigit() and cur != ".":
                t = get_unique(matrix, row, col)
                for num in t:
                    touching.append(num)

                if len(touching) == 2:
                    gear_ratio = touching[0] * touching[1]
                    total += gear_ratio
print(total)
