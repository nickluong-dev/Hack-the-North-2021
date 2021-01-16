import json
from urllib.request import urlopen


def get_total_hours(steam_id):
    key = input("Please enter your steam api key: ")
    # id = input("Please enter your steam id: ")
    total_hours = json.load(urlopen(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}"
                                    f"&steamid={steam_id}&format=json"))
    return total_hours["response"]["games"]


def main():
    print(get_total_hours())


if __name__ == "__main__":
    main()
