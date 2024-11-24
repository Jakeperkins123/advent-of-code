matrix = []
num_coords = {}
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


def bfs(matrix, row, col) -> list:
    # returns a list of numbers that have not been checked already

    num_list = []
    for dir in directions:

        newRow = row + dir[0]
        newCol = col + dir[1]

        if oob(newRow, newCol):
            continue

        ch = matrix[newRow][newCol]

        num_string = ""

        if ch.isdigit():
            # while loop to go left and get all digits
            x = newCol
            y = newRow

            # go left as far as possible, keep track of coordinates to find starting coord
            while not oob(y, x) and matrix[y][x].isdigit():
                num_string = matrix[y][x] + num_string
                x -= 1

            starting_coord = (y, x + 1)

            if starting_coord in num_coords:
                continue

            x = newCol + 1

            while not oob(y, x) and matrix[y][x].isdigit():
                num_string += matrix[y][x]
                x += 1

            num = int(num_string)
            num_coords[starting_coord] = num
            num_list.append(num)
    return num_list


def oob(row, col) -> bool:
    return row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])


with open("input.txt", "r") as file:
    for line in file:
        if not line.strip():
            continue
        matrix.append(list(line.strip()))

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            ch = matrix[row][col]
            if ch != "." and not ch.isdigit():
                # check all directions
                num_list = bfs(matrix, row, col)
                total += sum(num_list)

print(total)
