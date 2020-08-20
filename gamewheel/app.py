import random
import sys

from gamewheel.steam import get_owned_games, get_steamid


if __name__ == "__main__":
    STEAM_USERNAMES = [
        # Names go here!
    ]

    if not STEAM_USERNAMES:
        print("You must enter some names before you can run the script!")
        sys.exit(-1)

    steamids = map(get_steamid, STEAM_USERNAMES)
    owned_games = map(get_owned_games, steamids)

    shared_games = set.intersection(*[set(games_list) for games_list in owned_games])
    game = random.choice(list(shared_games))

    print("You should play...")
    print(game)
