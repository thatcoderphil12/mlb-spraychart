import pybaseball
from pybaseball import statcast_batter
from pybaseball import cache
import matplotlib.pyplot as plt
import matplotlib.patches as patches
cache.enable() 
players = input("Please enter the player's name in First Last format (or First1 Last1, First2 Last2, etc. (or First1 Last1, First2 Last2, etc.): ").strip()
playerlist = players.split(", ")
for player in playerlist:
    playerlist = players.split(", ")
for player in playerlist:
    first_name, last_name = player.split()
    savef = first_name.lower()
    savel = last_name.lower()
    id = pybaseball.playerid_lookup(last_name, first_name)['key_mlbam'][0]
    fullstats = statcast_batter(start_dt="2025-03-27", end_dt="2025-09-28", player_id=id)
    coordinates = fullstats[['hc_x', 'hc_y']]
    coordinates = coordinates.dropna(subset=['hc_x', 'hc_y'])
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.add_patch(patches.Wedge((125, 200), 154, -136, -46, ec="black", facecolor="lightgreen", linewidth=2))
    ax.scatter(coordinates['hc_x'], coordinates['hc_y'], alpha=0.5, s=50, color='red')
    ax.set_xlim(-50, 300)
    ax.set_ylim(-50, 250)
    ax.invert_yaxis()
    ax.set_aspect('equal')
    ax.set_xlabel('X (feet)')
    ax.set_ylabel('Y (feet)')
    ax.set_title(f'{player} - Spray Chart ({len(coordinates)} hits)')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'{savef}_{savel}', dpi=300, bbox_inches='tight')
    print(f"Spray chart saved as {savef}_{savel}.png")