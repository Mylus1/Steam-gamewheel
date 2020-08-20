# Steam Game Roulette Wheel

Put in some usernames, and spin the wheel to find out what you should play.

## Setup

Obtain a Steam Web API key.

Create a `.env` file in the project root with the following contents:

```
key=STEAM_API_KEY
```

Finally, install the project requirements.

```shell
pipenv install --dev
```

## Usage

Put some Steam usernames into the `STEAM_USERNAMES` list in `gamewheel/app.py`, then run the following command:

```shell
pipenv run python gamewheel/app.py
```

## Upcoming Features

* Discord bot
* Filtering for multiplayer games
* Web frontend
