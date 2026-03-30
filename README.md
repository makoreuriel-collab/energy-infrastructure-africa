# ⚡ Energy Access & Infrastructure in Africa

> Visualising electricity access rates across Africa — and the persistent urban-rural divide that leaves hundreds of millions of people without reliable power.

---

## Overview

Energy access is a prerequisite for almost everything else in development: it powers schools, clinics, businesses, and connectivity. Yet Sub-Saharan Africa accounts for over half of the world's unelectrified population, and in some countries the absolute number of people without power has increased even as access rates have risen — because population growth is outpacing electrification.

This project uses World Bank and IEA data to compare national, urban, and rural electricity access rates across 15 African countries, and to track Sub-Saharan Africa's electrification progress over two decades against South Asia and the global average.

---

## Objective

- Compare **national, urban, and rural electricity access rates** across 15 African economies
- Visualise Sub-Saharan Africa's **electrification trajectory (2000–2021)** versus global peers
- Quantify the **urban-rural divide** and identify the countries furthest from universal access

---

## Tools

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| pandas | Data manipulation |
| matplotlib | Visualisation |
| numpy | Grouped bar positioning |

---

## Data Sources

**World Bank – World Development Indicators (WDI)**
- Electricity access, national (%): [`EG.ELC.ACCS.ZS`](https://data.worldbank.org/indicator/EG.ELC.ACCS.ZS)
- Electricity access, rural (%): [`EG.ELC.ACCS.RU.ZS`](https://data.worldbank.org/indicator/EG.ELC.ACCS.RU.ZS)
- Electricity access, urban (%): [`EG.ELC.ACCS.UR.ZS`](https://data.worldbank.org/indicator/EG.ELC.ACCS.UR.ZS)

**IEA – Africa Energy Outlook**
- Regional electrification trends: [iea.org/reports/africa-energy-outlook-2022](https://www.iea.org/reports/africa-energy-outlook-2022)

---

## How to Run

```bash
pip install pandas matplotlib numpy
python analysis.py
```

Chart is saved to `outputs/energy_infrastructure_analysis.png`.

---

## Key Findings

- Sub-Saharan Africa improved from **~23% to ~50% electricity access** between 2000 and 2021 — real progress, but still **42 percentage points behind the global average**
- **South Sudan and Chad** have national access rates below 10%, reflecting the compound effect of fragility, conflict, and absent infrastructure investment
- The **urban-rural gap averages over 45 percentage points** — urban centres are relatively well served while rural communities remain almost entirely off-grid
- **Rwanda** stands out: from under 10% access in 2010 to 46% by 2021, driven by a government-led rural electrification push combining grid extension and off-grid solar
- **Egypt and South Africa** demonstrate that near-universal access is achievable — a relevant reference point for what sustained policy commitment can accomplish

---

## Why This Matters for Development Finance

Energy access is central to the **AfDB's New Deal on Energy for Africa**, and electricity projects are one of the largest components of MDB lending on the continent. This type of access analysis directly informs how DFIs prioritise their energy portfolios — deciding where grid extension makes sense versus mini-grids or off-grid solar, and where blended finance is needed to make projects viable in underserved, low-density markets. The urban-rural gap shown here is precisely the finding that shapes investment cases for distributed energy companies and rural electrification programmes.

---

## Output

![Energy Access Chart](outputs/energy_infrastructure_analysis.png)

---

*Part of a four-project portfolio analysing Africa's development challenges, aligned with the African Development Bank's Four Cardinal Points.*
