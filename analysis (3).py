# ============================================================
# Project: Energy Access & Infrastructure in Africa
# Data:    World Bank WDI + IEA
# Charts:  1. Urban vs rural electricity access by country
#          2. Sub-Saharan Africa access trend vs global peers
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

# ── DATA ────────────────────────────────────────────────────
# Electricity access (% of population) — World Bank: EG.ELC.ACCS.ZS
# Rural access                         — World Bank: EG.ELC.ACCS.RU.ZS
# Urban access                         — World Bank: EG.ELC.ACCS.UR.ZS
# Reference year: approx. 2021

country_data = {
    "Country": [
        "Nigeria", "Ethiopia", "Tanzania", "Kenya", "Mozambique",
        "Niger", "Chad", "Mali", "South Sudan", "Malawi",
        "Ghana", "Senegal", "Rwanda", "South Africa", "Egypt"
    ],
    "National_pct": [
        57.5, 44.3, 38.0, 75.0, 29.0,
        18.5,  8.5, 51.0,  7.8, 11.5,
        85.0, 67.0, 46.0, 84.2, 100.0
    ],
    "Rural_pct": [
        36.0, 31.0, 16.8, 63.0,  5.5,
         3.5,  1.5, 34.0,  1.5,  4.5,
        72.0, 47.0, 36.0, 64.0, 99.9
    ],
    "Urban_pct": [
        85.0, 88.0, 65.0, 93.0, 63.0,
        74.0, 43.0, 87.0, 37.0, 50.0,
        94.0, 90.0, 71.0, 85.0, 100.0
    ]
}

# Time series: Sub-Saharan Africa electricity access vs global peers
# Sources: World Bank, IEA Africa Energy Outlook
time_series = {
    "Year":          [2000, 2005, 2010, 2015, 2017, 2019, 2021],
    "SSA_pct":       [23.0, 25.8, 30.0, 35.8, 40.0, 46.0, 49.5],
    "South_Asia_pct":[51.0, 57.0, 67.0, 79.0, 86.0, 95.5, 98.0],
    "Global_pct":    [73.0, 77.0, 82.0, 87.0, 89.0, 90.5, 91.4]
}

df = pd.DataFrame(country_data)
ts = pd.DataFrame(time_series)

# Sort countries by national access for the chart
df_sorted = df.sort_values("National_pct", ascending=True)

# ── CHART 1: Grouped bar — urban vs rural access ─────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle("Energy Access & Infrastructure Gap in Africa", fontsize=14, fontweight="bold")

ax1 = axes[0]
y = np.arange(len(df_sorted))
h = 0.35   # bar height

ax1.barh(y + h / 2, df_sorted["Urban_pct"],  height=h, color="#1a6e5c",
         label="Urban",  edgecolor="white")
ax1.barh(y - h / 2, df_sorted["Rural_pct"],  height=h, color="#e05c2a",
         label="Rural",  edgecolor="white", alpha=0.85)

ax1.set_yticks(y)
ax1.set_yticklabels(df_sorted["Country"], fontsize=8)
ax1.set_xlabel("% of Population with Electricity Access")
ax1.set_title("Urban vs. Rural Electricity Access", fontweight="bold")
ax1.axvline(100, color="#aaaaaa", linestyle=":", linewidth=0.8)
ax1.set_xlim(0, 110)
ax1.legend(fontsize=9)
ax1.spines[["top", "right"]].set_visible(False)

# Flag the worst cases
ax1.text(10, 2.5, "Chad & South Sudan:\nnational access < 10%",
         fontsize=7.5, color="#e05c2a",
         bbox=dict(boxstyle="round,pad=0.3", facecolor="#fff3f0",
                   edgecolor="#e05c2a", alpha=0.9))

# ── CHART 2: Line chart — access trend over time ─────────────
ax2 = axes[1]

ax2.plot(ts["Year"], ts["Global_pct"],    color="#aaaaaa", linewidth=2,
         marker="o", markersize=5, label="Global Average")
ax2.plot(ts["Year"], ts["South_Asia_pct"],color="#4455aa", linewidth=2,
         marker="s", markersize=5, label="South Asia")
ax2.plot(ts["Year"], ts["SSA_pct"],       color="#1a6e5c", linewidth=2.5,
         marker="D", markersize=6, label="Sub-Saharan Africa")

# Shade the gap between SSA and global average
ax2.fill_between(ts["Year"], ts["SSA_pct"], ts["Global_pct"],
                 alpha=0.1, color="#e05c2a")

# Annotate the current gap
gap = ts.iloc[-1]["Global_pct"] - ts.iloc[-1]["SSA_pct"]
mid = (ts.iloc[-1]["Global_pct"] + ts.iloc[-1]["SSA_pct"]) / 2
ax2.annotate(f"~{gap:.0f}pp gap\nvs. global average",
             xy=(2021, mid), xytext=(2012, 72),
             arrowprops=dict(arrowstyle="->", color="#e05c2a"),
             fontsize=8.5, color="#e05c2a")

ax2.set_xlabel("Year")
ax2.set_ylabel("Electricity Access (%)")
ax2.set_title("Sub-Saharan Africa Electrification\nvs. Global Peers (2000–2021)", fontweight="bold")
ax2.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
ax2.set_ylim(0, 105)
ax2.legend(fontsize=9)
ax2.spines[["top", "right"]].set_visible(False)

plt.tight_layout()

# ── SAVE ────────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/energy_infrastructure_analysis.png", dpi=150, bbox_inches="tight")
print("Saved: outputs/energy_infrastructure_analysis.png")
plt.show()

# ── SUMMARY ─────────────────────────────────────────────────
print("\n── Key Numbers ─────────────────────────────────────")
print(f"Avg national access (Africa sample): {df['National_pct'].mean():.1f}%")
print(f"Avg rural access    (Africa sample): {df['Rural_pct'].mean():.1f}%")
print(f"Avg urban access    (Africa sample): {df['Urban_pct'].mean():.1f}%")
print(f"Avg urban-rural gap:                 {(df['Urban_pct'] - df['Rural_pct']).mean():.1f} pp")
print(f"SSA gap vs global average (2021):    ~{gap:.0f} percentage points")
below_20 = df[df["National_pct"] < 20]["Country"].tolist()
print(f"Countries below 20% national access: {', '.join(below_20)}")
