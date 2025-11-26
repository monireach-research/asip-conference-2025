import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "Times New Roman"

# Read CSV
csv_path = "./resources/cambodia_population_pie_of_pie.csv"
df = pd.read_csv(csv_path)

# Main pie chart data
main_labels = [row[1] for row in df[df["Category"] == "Population"].values]
main_values = [row[2] for row in df[df["Category"] == "Population"].values]

# Sub pie chart data (elderly breakdown)
sub_labels = [row[1] for row in df[df["Category"] == "Elderly"].values]
sub_values = [row[2] for row in df[df["Category"] == "Elderly"].values]

fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot(121)
ax2 = plt.subplot(122)

# Main pie
ax1.pie(
    main_values,
    labels=main_labels,
    autopct=lambda pct: f"{int(pct/100*sum(main_values)):,}",
    startangle=90,
    colors=["#e41a1c", "#377eb8"],
)
ax1.set_title("Cambodia Population by 2030", fontsize=12)

# Sub pie
ax2.pie(
    sub_values,
    labels=sub_labels,
    autopct=lambda pct: f"{int(pct/100*sum(sub_values)):,}",
    startangle=90,
    colors=["#4daf4a", "#ff7f00"],
)
ax2.set_title("Elderly Population Breakdown", fontsize=12)

plt.tight_layout()
plt.savefig(
    "./resources/cambodia_population_pie_of_pie.png", dpi=300, bbox_inches="tight"
)
# plt.show()
