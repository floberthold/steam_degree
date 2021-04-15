import requests
import connectors.connector


class SteamConnector(connectors.connector.Connector):
    def retrieve_game_list(self, steam_id):
        return requests.get(f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=&steamid={steam_id}&format=json")
