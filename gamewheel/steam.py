import os

import requests

base_url = "http://api.steampowered.com"
key = os.getenv("key")


def get_steamid(username):
    response = requests.get(
        f"{base_url}/ISteamUser/ResolveVanityURL/v0001/",
        params={
            "key" : key,
            "vanityurl": username,
        }
    )
    response.raise_for_status()
    data = response.json()

    success = data["response"]["success"]  # 1 for success, 42 for failure
    if success == 1:
        return data["response"]["steamid"]
    else:
        message = data["response"]["message"]
        print(f"Warning: failed to find steam ID: {message}")


def get_owned_games(steamid):
    response = requests.get(
        f"{base_url}/IPlayerService/GetOwnedGames/v0001/",
        params={
            "include_appinfo": True,
            "include_played_free_games": True,
            "key": key,
            "steamid": steamid,
        }
    )
    response.raise_for_status()
    data = response.json()

    games = []
    for game in data["response"]["games"]:
        games.append(game["name"])

    return games
