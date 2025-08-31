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
yamal_values=[0.28,0.41,0.69,0.31,0.44,0.75,0.31,0.75]
salah_values=[0.77,0.48,1.25,0.67,0.38,1.05,0.49,0.87]
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

radar2, vertices2 = radar.draw_radar_solid(yamal_values, ax=ax,
                                           kwargs={'facecolor': '#4361EE',
                                                   'alpha': 0.4,
                                                   'edgecolor': '#4361EE',
                                                   'lw': 2})

radar3, vertices3 = radar.draw_radar_solid(salah_values, ax=ax,
                                           kwargs={'facecolor': '#FF6B6B',
                                                   'alpha': 0.4,
                                                   'edgecolor': '#FF6B6B',
                                                   'lw': 2})
radar4, vertices4 = radar.draw_radar_solid(dembélé_values, ax=ax,
                                           kwargs={'facecolor': '#FFD166',
                                                   'alpha': 0.4,
                                                   'edgecolor': '#FFD166',
                                                   'lw': 2})
                                                   


ax.scatter(vertices1[:, 0], vertices1[:, 1],
           c='#4ECDC4', edgecolors='#4ECDC4', marker='o', s=150, zorder=4)
ax.scatter(vertices2[:, 0], vertices2[:, 1],
           c='#4361EE', edgecolors='#4361EE', marker='o', s=150, zorder=4)
ax.scatter(vertices3[:, 0], vertices3[:, 1],
           c='#FF6B6B', edgecolors='#FF6B6B', marker='o', s=150, zorder=4)
ax.scatter(vertices4[:, 0], vertices3[:, 1],
           c='#FFD166', edgecolors='#FFD166', marker='o', s=150, zorder=4)


range_labels = radar.draw_range_labels(ax=ax, fontsize=20)
param_labels = radar.draw_param_labels(ax=ax, fontsize=20)

#Add title
fig_text(
    0.5, 1.03, "<Raphinha> vs <Lamine Yamal> vs <Mohamed Salah> vs <Ousmane Dembélé>",
    size=16, fig=fig,
    highlight_textprops=[{"color": '#4ECDC4'}, {"color": '#17FF1B'},{"color": '#FF6B6B'},{"color": '#FFD166'}],
    ha="center",color="#000000"
)

#Add subtitle
fig_text(
    0.515, 1.00, "2024/25 Season in their Domestic Leagues Per 90 Minutes. 90 minute games played: <31.5>, <31.7>, <37.5>, <19.2>",
    size=10, fig=fig,
    highlight_textprops=[{"color": '#4ECDC4'}, {"color": '#17FF1B'}, {"color": '#FF6B6B'},{'color': '#FFD166'}],
    ha="center", color="#000000"
)

#Add Raphinha image
ax1 = fig.add_axes([0.10,0.80,0.10,0.25])
ax1.axis('off')
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Raphinha.png')
ax1.imshow(img)

#Add Barcelona club badge
ax2=fig.add_axes([0.20,0.80,0.09,0.25])
ax2.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/FC Barcelona club badge.png')
ax2.imshow(img)

#Add Yamal image
ax3 = fig.add_axes([0.30,0.80,0.10,0.25])
ax3.axis('off')
img = Image.open('/Users/siphuvuyomngxunyeni/Downloads/Yamal.png')
ax3.imshow(img)

#Add Barcelona image
ax4=fig.add_axes([0.40,0.80,0.09,0.25])
ax4.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/FC Barcelona club badge.png')
ax4.imshow(img)

#Add Salah image
ax5=fig.add_axes([0.63,0.80,0.10,0.25])
ax5.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Salah.png')
ax5.imshow(img)

#Add Liverpool image
ax6=fig.add_axes([0.73,0.80,0.09,0.25])
ax6.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liverpool.png')
ax6.imshow(img)

#Add Dembélé image
ax7=fig.add_axes([0.83,0.80,0.10,0.25])
ax7.axis('off')
img=Image.open('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Dembele.png')
ax7.imshow(img)

#Add PSG image
ax8=fig.add_axes([0.93,0.80,0.09,0.25])
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

plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Raphinha vs Yamal vs Salah vs Dembélé.png', dpi=300, bbox_inches='tight')