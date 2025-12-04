import pybaseball
from pybaseball import statcast
from pybaseball import  playerid_lookup
from pybaseball import  statcast_batter
from pybaseball import batting_stats
player = input("Please enter the player's name (First Last): ")
first_name, last_name = player.split()
id = pybaseball.playerid_lookup(last_name, first_name)['key_mlbam'][0]
fullstats = statcast_batter(start_dt="2025-03-27", end_dt="2025-09-28", player_id=id)