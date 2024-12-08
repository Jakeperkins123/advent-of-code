from collections import defaultdict

# Read and parse the grid from the input file
with open("input.txt") as file:
    grid = file.read().strip().split("\n")

grid_height = len(grid)
grid_width = len(grid[0])

# Group antennas by their frequency (a, b, c, etc.)
antennas_by_frequency = defaultdict(list)
for y in range(grid_height):
    for x in range(grid_width):
        if grid[y][x] != ".":
            antennas_by_frequency[grid[y][x]].append((y, x))

# Sets to store results
antinodes_with_distance_ratio = set()  # Part 1: Points that satisfy both alignment and 2:1 distance
collinear_points = set()  # Part 2: Points that are just aligned with two antennas

# Check every point in the grid
for point_y in range(grid_height):
    for point_x in range(grid_width):
        # For each frequency (a, b, c, etc.)
        for frequency, antenna_positions in antennas_by_frequency.items():
            # Check all pairs of antennas with the same frequency
            for antenna1_y, antenna1_x in antenna_positions:
                for antenna2_y, antenna2_x in antenna_positions:
                    # Skip if same antenna
                    if (antenna1_y, antenna1_x) != (antenna2_y, antenna2_x):
                        # Calculate Manhattan distances
                        distance_to_antenna1 = abs(point_y - antenna1_y) + abs(point_x - antenna1_x)
                        distance_to_antenna2 = abs(point_y - antenna2_y) + abs(point_x - antenna2_x)

                        # Calculate vectors from point to each antenna
                        y_vector_to_antenna1 = point_y - antenna1_y
                        x_vector_to_antenna1 = point_x - antenna1_x
                        y_vector_to_antenna2 = point_y - antenna2_y
                        x_vector_to_antenna2 = point_x - antenna2_x

                        # Check if point is collinear with both antennas using cross product
                        if y_vector_to_antenna1 * x_vector_to_antenna2 == x_vector_to_antenna1 * y_vector_to_antenna2:
                            collinear_points.add((point_y, point_x))

                            # Check for 2:1 distance ratio
                            if distance_to_antenna1 == 2 * distance_to_antenna2 or distance_to_antenna2 == 2 * distance_to_antenna1:
                                antinodes_with_distance_ratio.add((point_y, point_x))

print(len(antinodes_with_distance_ratio))  # Part 1
print(len(collinear_points))  # Part 2
