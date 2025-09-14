from mplsoccer import Radar, FontManager, grid
import matplotlib.pyplot as plt
from highlight_text import fig_text
from PIL import Image

#Define parameters throughout the season
params=['Goals','Assists','Goals & Assists\n G+A','Expected Goals\n xG','Expected Assisted Goals\n xAG','Expected Goals &\n Expected Assisted Goals\n xG+xAG',
        'Non-Penalty\n Expected Goals\n npxG', 'npxG+xAG']

#Setting lower and upper bounds
low=[0.05,0.05,0.50,0.05,0.05,0.05,0.05,0.50]
high=[1.20,0.50,1.50,1,0.50,1.50,0.90,1.30]

#Player values. The ones with 100s are divided by 100 to accomodate circle radii. The 10s are divided by 10 for the same reason.
raphinha_values=[0.57,0.29,0.86,0.61,0.40,1.01,0.56,0.96]
dembélé_values=[1.09,0.31,1.40,0.86,0.43,1.29,0.81,1.25]

radar = Radar(params, low, high,
              # whether to round any of the labels to integers instead of decimal places
              round_int=[False]*len(params),
              num_rings=4,  # the number of concentric circles (excluding center circle)
              # if the ring_width is more than the center_circle_radius then
              # the center circle radius will be wider than the width of the concentric circles
              ring_width=1, center_circle_radius=1)

#Plotting the radar
fig, ax = radar.setup_axis()
rings_inner = radar.draw_circles(ax=ax, facecolor='#F8F9FA', edgecolor='#E0E1DD')

radar1, vertices1 = radar.draw_radar_solid(raphinha_values, ax=ax,
                                           kwargs={'facecolor': '#4ECDC4',
                                                   'alpha': 0.4,
                                                   'edgecolor': '#4ECDC4',
                                                   'lw': 2})
radar4, vertices4 = radar.draw_radar_solid(dembélé_values, ax=ax,
                                           kwargs={'facecolor': '#FFD166',
                                                   'alpha': 0.4,
                                                   'edgecolor': '#FFD166',
                                                   'lw': 2})
                                                   


ax.scatter(vertices1[:, 0], vertices1[:, 1],
           c='#01CCBF', edgecolors='#01CCBF', marker='o', s=150, zorder=4)
ax.scatter(vertices4[:, 0], vertices4[:, 1],
           c='#FFD166', edgecolors='#FFD166', marker='o', s=150, zorder=4)


range_labels = radar.draw_range_labels(ax=ax, fontsize=20)
param_labels = radar.draw_param_labels(ax=ax, fontsize=20)

#Add title
fig_text(
    0.5, 1.03, "<Raphinha> vs <Ousmane Dembélé>",
    size=16, fig=fig,
    highlight_textprops=[{"color": "#01CCBF"},{"color": '#FFD166'}],
    ha="center",color="#000000"
)

#Add subtitle
fig_text(
    0.515, 1.00, "2024/25 Season in their Domestic Leagues Per 90 Minutes\n 90 minute games played: <31.5> & <19.2>",
    size=10, fig=fig,
    highlight_textprops=[{"color": "#01CCBF"},{'color': '#FFD166'}],
    ha="center", color="#000000"
)

#Add Raphinha image
ax1 = fig.add_axes([.06,0.89,.13,.13])
ax1.axis('off')
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Raphinha.png')
ax1.imshow(img)

#Add Barcelona club badge
ax2=fig.add_axes([0.18,0.89,0.1,0.135])
ax2.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/FC Barcelona club badge.png')
ax2.imshow(img)

#Add Dembélé image
ax7=fig.add_axes([.83,0.89,.13,.13])
ax7.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Dembele.png')
ax7.imshow(img)

#Add PSG image
ax8=fig.add_axes([0.73,0.89,0.1,0.13])
ax8.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/PSG.png')
ax8.imshow(img)

#Add credits
CREDIT_1="Data: FBREF"
CREDIT_2="Viz: Siphe247"

fig_text(
    0.99, 0.1, f"{CREDIT_1}\n{CREDIT_2}", size=15,
    color="#000000",
    ha="right"
)

plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Raphinha vs Dembélé new.png', dpi=300, bbox_inches='tight')