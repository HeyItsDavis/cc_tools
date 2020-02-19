import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    games = json_data["games"]
    for game in games:
        platform = game["platform"]
        new_platform = test_data.Platform(platform["name"], platform["launchYear"])
        new_game = test_data.Game(game["title"], new_platform, game["year"])
        game_library.add_game(new_game)

    return game_library


#Part 2
input_json_file = "data/test_data.json"

with open(input_json_file, "r") as reader:
    game_library_json = json.load(reader)

new_library = make_game_library_from_json(game_library_json)
print(new_library)


