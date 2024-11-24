total = 0
with open("input.txt", "r") as file:
    for line in file:
        if not line.strip():
            continue
        card_start = line.find(":") + 1
        card_end = line.find("|")
        winning_numbers = list(map(int, line[card_start:card_end].split()))
        card_end += 1
        play_nums = list(map(int, line[card_end:].split()))
        line_total = 0
        for num in play_nums:
            if num in winning_numbers:
                if line_total == 0:
                    line_total += 1
                else:
                    line_total *= 2
        total += line_total
print(total)
