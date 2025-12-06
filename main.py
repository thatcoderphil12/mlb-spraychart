import pybaseball
from pybaseball import statcast_batter
import matplotlib.pyplot as plt
import matplotlib.patches as patches
player = input("Please enter the player's name (First Last): ")
first_name, last_name = player.split()
id = pybaseball.playerid_lookup(last_name, first_name)['key_mlbam'][0]
fullstats = statcast_batter(start_dt="2025-03-27", end_dt="2025-09-28", player_id=id)
coordinates = fullstats[['hc_x', 'hc_y']]
coordinates = coordinates.dropna(subset=['hc_x', 'hc_y'])
fig, ax = plt.subplots(figsize=(10, 10))
ax.add_patch(patches.Wedge((125, 0), 250, 45, 135, ec="black", facecolor="lightgreen", linewidth=2))
ax.scatter(coordinates['hc_x'], coordinates['hc_y'], alpha=0.5, s=50, color='red')
ax.set_xlim(-50, 300)
ax.set_ylim(-50, 300)
ax.set_aspect('equal')
ax.set_xlabel('X (feet)')
ax.set_ylabel('Y (feet)')
ax.set_title(f'{player} - Spray Chart ({len(coordinates)} hits)')
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('spray_chart.png', dpi=300, bbox_inches='tight')
print(f"Spray chart saved as 'spray_chart.png'")