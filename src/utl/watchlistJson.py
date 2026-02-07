import json


def load_watchlist(watchlist: str = "config/symbols.json"):
    with open(watchlist, "r") as f:
        return json.load(f)
