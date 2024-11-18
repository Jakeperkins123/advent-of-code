
with open('input.txt', 'r') as file:
    total_power = 0
    for line in file:
        # find the maximum red, green, and blue
        start_of_games_index = line.find(":") + 1
        # get just the games
        games = line[start_of_games_index:].strip()
        # get each pull as "1 red" or "2 blue" etc.
        pulls = games.replace(";", ",").split(",") 
        # create a map to store the max of each
        max_map = {"red": 0, "green": 0, "blue": 0}
        # set max values for each color
        for pull in pulls:
            if not pull.strip():
                continue
            number, color = pull.split()
            number = int(number)
            max_map[color] = max(number, max_map[color])
            
        # multiply the colors max count together
        power = 1
        for color, count in max_map.items():
            power *= count
        # add the total for this game to the total power
        total_power += power
        
    print(total_power)