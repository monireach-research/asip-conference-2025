import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Helvetica"

# Read CSV data
csv_path = (
    "./resources/proposed_system_and_kami_fall_detect_camera_3_year_total_expenses.csv"
)
df = pd.read_csv(csv_path)

# Pivot data for plotting
pivot = df.pivot(index="Month", columns="Category", values="Cost")
months = pivot.index.tolist()

# Create month labels as M1, M2, ..., M36
month_labels = [f"M{i+1}" for i in range(len(months))]
edge_costs = pivot["Proposed Edge-based System"].tolist()
kami_costs = pivot["Kami Fall Detect Camera"].tolist()

# Find break-even point
break_even_idx = None
break_even_x = None
break_even_y = None
for i, (e, k) in enumerate(zip(edge_costs, kami_costs)):
    if k >= e:
        break_even_idx = i
        # Interpolate between previous and current month
        if i > 0:
            e0, k0 = edge_costs[i - 1], kami_costs[i - 1]
            e1, k1 = e, k
            frac = (e0 - k0) / ((k1 - k0) - (e1 - e0)) if (k1 - k0) != (e1 - e0) else 0
            x0, x1 = i - 1, i
            break_even_x = x0 + frac
            break_even_y = e0 + (e1 - e0) * frac
        else:
            break_even_x = i
            break_even_y = e
        break

# Define target dimensions in pixels
width_px = 850
height_px = 400

# Set a standard or desired DPI (e.g., 100 or 150)
dpi_val = 100

# Calculate the figure size in inches
width_in = width_px / dpi_val
height_in = height_px / dpi_val

fig, ax = plt.subplots(figsize=(width_in, height_in), dpi=dpi_val)
ax.plot(
    month_labels, edge_costs, label="Edge-Based System", color="#377eb8", linewidth=2
)
ax.plot(
    month_labels,
    kami_costs,
    label="Kami Fall Detect Camera",
    color="#e41a1c",
    linewidth=2,
)

# Mark break-even point if found
if break_even_idx is not None:
    # Place break-even marker at interpolated position
    # Use numeric x for scatter/annotate, but label with nearest month
    be_month_idx = int(round(break_even_x))
    be_month_label = (
        month_labels[be_month_idx]
        if be_month_idx < len(month_labels)
        else month_labels[-1]
    )
    ax.scatter(
        break_even_x,
        break_even_y,
        color="black",
        zorder=5,
    )
    ax.annotate(
        f"Break-even\n{be_month_label}",
        xy=(break_even_x, break_even_y),
        xytext=(0, 30),
        textcoords="offset points",
        ha="center",
        va="bottom",
        fontsize=12,
        color="black",
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="black"),
    )

# Annotate edge-based system cost (constant value)
ax.annotate(
    f"Edge-Based System\nCost: ${edge_costs[-1]} (one-time)",
    xy=(month_labels[-1], edge_costs[-1] + 30),
    xytext=(-80, 0),  # shift left by 100 points
    textcoords="offset points",
    ha="center",
    va="bottom",
    fontsize=12,
    color="#377eb8",
    fontweight="bold",
    # arrowprops=dict(arrowstyle="->", color="#377eb8"),
)

ax.set_ylabel("Cumulative Cost (USD)", fontsize=10)
ax.set_title(
    "3-Year Expense Comparison: Edge-Based vs. Kami Fall Detect Camera", fontsize=12
)
xtick_labels = month_labels[::3]
if month_labels[-1] not in xtick_labels:
    xtick_labels.append(month_labels[-1])
ax.set_xticks(xtick_labels)
ax.set_xticklabels(xtick_labels, fontsize=10, rotation=0)
ax.tick_params(axis="y", labelsize=10)
ax.legend(fontsize=10, loc="upper left", frameon=False)
ax.set_ylim(
    0, max(max(edge_costs), max(kami_costs)) + 200  # pylint: disable = nested-min-max
)
plt.tight_layout()
plt.savefig(
    "./resources/compare_3_year_expenses_line_chart.png",
    dpi=dpi_val,
    bbox_inches="tight",
)
# plt.show()
