import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams["font.family"] = "Helvetica"

# Read data from CSV
csv_path = "./resources/proposed_system_and_kami_fall_detect_camera_component_costs.csv"
df = pd.read_csv(csv_path)

systems = ["Proposed Edge-based System", "Kami Fall Detect Camera"]
all_labels = df["Item"].unique().tolist()

# Prepare cost matrix: rows=systems, cols=items
cost_matrix = np.zeros((len(systems), len(all_labels)))
for i, system in enumerate(systems):
    for j, label in enumerate(all_labels):
        match = df[(df["Category"] == system) & (df["Item"] == label)]
        cost_matrix[i, j] = match["Cost"].sum() if not match.empty else 0

cost_labels = all_labels
costs = cost_matrix

# Define target dimensions in pixels
width_px = 665
height_px = 400

# Set a standard or desired DPI (e.g., 100 or 150)
dpi_val = 100

# Calculate the figure size in inches
width_in = width_px / dpi_val
height_in = height_px / dpi_val

# Create the figure and axes with the calculated size in inches and specific DPI
fig, ax = plt.subplots(figsize=(width_in, height_in), dpi=dpi_val)
bar_width = 0.7
ind = np.arange(len(systems))

bottom = np.zeros(len(systems))
colors = ["#4daf4a", "#377eb8", "#ff7f00", "#984ea3", "#e41a1c"]

for i, label in enumerate(cost_labels):
    bars = ax.bar(
        ind, costs[:, i], bar_width, bottom=bottom, label=label, color=colors[i]
    )
    # Add item name and cost labels to each stack, horizontally side-by-side, in black
    for j, bar in enumerate(bars):
        if costs[j, i] > 0:
            height = bar.get_height()
            xpos = bar.get_x() + bar.get_width() / 2
            ypos = bottom[j] + height / 2
            ax.text(
                xpos,
                ypos,
                f"{label}  ${int(costs[j, i])}",
                ha="center",
                va="center",
                fontsize=10,
                color="white",
                fontweight="bold",
            )
    bottom += costs[:, i]


# Add total cost labels above each bar
total_costs = costs.sum(axis=1)
for idx, total in enumerate(total_costs):
    xpos = ind[idx]
    ypos = bottom[idx] + 10  # 10 units above the top
    ax.text(
        xpos,
        ypos,
        f"Total: ${int(total)}",
        ha="center",
        va="bottom",
        fontsize=12,
        color="black",
        fontweight="bold",
    )

ax.set_ylabel("Cost (USD)", fontsize=10)
ax.set_title("Cost Comparison: Edge-Based vs. Kami Fall Detect Camera", fontsize=12)
ax.set_xticks(ind)
ax.set_xticklabels(systems, fontsize=10)
ax.tick_params(axis="y", labelsize=10)
# ax.legend(fontsize=10, loc="upper right", frameon=False)
ax.set_ylim(0, 800)  # Increase y-axis height for total label space
plt.subplots_adjust(top=0.82)  # Add extra top margin to prevent overlap
plt.tight_layout()

# plt.show()
plt.savefig(
    "./resources/compare_system_costs_chart.png", dpi=dpi_val, bbox_inches="tight"
)
