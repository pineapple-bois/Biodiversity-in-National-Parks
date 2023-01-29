import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# The below program creates a 1x10 grid of colour labels from the `prey_colour` dictionary

# Dictionary of HTML color codes with labels
colours = {'Buzzard': '#8dd3c7', 'Condor': '#ffffb3', 'Eagle': '#bebada', 'Falcon': '#fb8072', 'Harrier': '#80b1d3',
            'Hawk': '#fdb462', 'Kite': '#b3de69', 'Osprey': '#fccde5', 'Owl': '#bc80bd', 'Vulture': '#d9d9d9'}

# Create a figure and a 1x10 grid of subplots
fig, axs = plt.subplots(1, 10, figsize=(20, 2))

# Set the background color of each subplot
for i, color in enumerate(colours):
    rect = mpatches.Rectangle((0, 0), 1, 1, facecolor=colours[color])
    axs[i].add_patch(rect)

# Set the labels for each subplot
for i, color in enumerate(colours):
    axs[i].text(0.5, 0.5, color, ha='center', va='center', fontsize=20)

# Remove the axis labels and tick marks
for ax in axs.ravel():
    ax.set_xticks([])
    ax.set_yticks([])
    ax.axis('off')

# Save the figure
plt.tight_layout(pad=0)
plt.savefig("colour_table.png", bbox_inches='tight')


