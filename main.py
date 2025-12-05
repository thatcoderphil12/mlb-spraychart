import pybaseball
from pybaseball import statcast
from pybaseball import  playerid_lookup
from pybaseball import  statcast_batter
player = input("Please enter the player's name (First Last): ")
first_name, last_name = player.split()
id = pybaseball.playerid_lookup(last_name, first_name)['key_mlbam'][0]
fullstats = statcast_batter(start_dt="2025-03-27", end_dt="2025-09-28", player_id=id)
columns_to_extract = ['hc_x', 'hc_y']
extracted_data = fullstats[columns_to_extract]
print(extracted_data)
extracted_data.to_csv('player_stats.csv', index=False)
print("\nData saved to player_stats.csv")