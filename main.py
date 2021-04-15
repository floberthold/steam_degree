from connectors import connector
from connectors.steam import steam_connector

my_connector = steam_connector.SteamConnector()
x = my_connector.retrieve_game_list("carnohan")
print(x)

