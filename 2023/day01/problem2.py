import re

num_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


with open("input.txt", "r") as f:
    input = f.read()

lines = input.strip().split("\n")

total = 0
for line in lines:
    nums_found = []
    for i, char in enumerate(line):
        start_index = 0
        if char.isdigit():
            nums_found.append((i, char))

    # Find spelled-out numbers
    for num_string, num in num_map.items():
        # Use re.finditer to capture all occurrences
        for match in re.finditer(num_string, line):
            start_index = match.start()
            nums_found.append((start_index, num))

    nums_found.sort()

    first_num = nums_found[0][1]
    last_num = nums_found[-1][1]
    total_to_add = int(first_num + last_num)
    total += total_to_add
print(total)
