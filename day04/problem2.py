total = 0
with open("input.txt", "r") as f:
    puzzle_input = f.read()

lines = puzzle_input.strip().split("\n")
cards = [1] * len(lines)
for i, line in enumerate(lines):
    parts = line.split("|")
    win_nums = set(parts[0].split(":")[1].split())  # Extract and split winning numbers
    actual_nums = set(parts[1].split())  # Extract and split actual numbers
    overlap = win_nums & actual_nums

    # For each overlapping match between the winning numbers and play numbers:
    for match_index in range(len(overlap)):
        # Calculate the card index to which the matches propagate
        next_card_index = i + match_index + 1

        # Ensure we don't exceed the list of cards
        if next_card_index < len(cards):
            # Increment the count of copies for the next card by the number of copies of the current card
            cards[next_card_index] += cards[i]

total_cards = sum(cards)
print(total_cards)
