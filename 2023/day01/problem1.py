with open("input.txt", "r") as f:
    input = f.read()

lines = input.strip().split("\n")

total = 0
for line in lines:
    s = ""
    for char in line:
        if char.isdigit():
            s += char
    first_digit = s[0]
    last_digit = s[-1]
    num = int(first_digit + last_digit)
    total += num
print(total)
