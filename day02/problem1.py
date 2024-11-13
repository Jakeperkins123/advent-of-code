
def get_game_id(s: str) -> int:
    # get the game ID
    return int(s.replace("Game ", "").split(":")[0])

def get_all_pulls_for_game(game_string: str) -> dict:
    # Get all pulls for a game as a dict {color -> count}
    pulls = {}
    pull_strings = game_string.split(',')

    for pull in pull_strings:
        pull_count, pull_color = pull.split()
        pulls[pull_color] = int(pull_count)
       
    return pulls

def get_all_games(s: str) -> list:
    # Get all games as a list
        start_of_games_index = s.find(":") + 1

        games = s[start_of_games_index:].split(';')
        return [game.strip() for game in games]

with open('input.txt', 'r') as file:
    # The maximum amount of cubes of each color
    max_map = {'red': 12, 'green': 13, 'blue': 14}

    # Sum of all valid game id's
    game_id_total = 0

    for s in file:
        s = s.strip()
        if len(s) == 0:
            break
        
        # Get the game ID
        game_id = get_game_id(s)
        # Get games as a list of strings
        games = get_all_games(s)

        # Every game must be valid for a given row in input.txt
        all_games_valid = True

        # Loop through each game
        for game in games:
            # Get all pulls as a dictionary {color -> count} 
            pulls = get_all_pulls_for_game(game)
            # loop through each pull
            for color,count in pulls.items():
                # If the pull is invalid
                if count > max_map[color]:
                    # Flag the row as invalid
                    all_games_valid = False
                    print('game ' + str(game_id) + ' is invalid - reason: ' + color + ' is greater than max ' + str(max_map[color]))
                    break
            # Dont keep checking each game if it's already been declared invalid
            if not all_games_valid:
                break

        # If every game is valid for the row
        if all_games_valid:
            # Add the game ID to the total 
            game_id_total += game_id
    print(str(game_id_total))
