
# chart.py
# Author: 23f1002560@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------
# 1. Generate synthetic data
# -------------------------------
np.random.seed(42)
channels = ["Email", "Chat", "Phone", "Social Media"]

data = []
for channel in channels:
    if channel == "Email":
        times = np.random.normal(10, 2, 200)  # slower
    elif channel == "Chat":
        times = np.random.normal(3, 1, 200)   # fastest
    elif channel == "Phone":
        times = np.random.normal(6, 1.5, 200)
    else:  # Social Media
        times = np.random.normal(8, 2, 200)

    for t in times:
        data.append([channel, max(t, 0)])  # no negative times

df = pd.DataFrame(data, columns=["Channel", "ResponseTime"])

# -------------------------------
# 2. Set professional Seaborn style
# -------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------------------
# 3. Create violinplot
# -------------------------------
plt.figure(figsize=(8, 8))  # 512x512 pixels at dpi=64
ax = sns.violinplot(
    data=df,
    x="Channel",
    y="ResponseTime",
    palette="Set2",
    inner="quartile"
)

# -------------------------------
# 4. Add labels and title
# -------------------------------
ax.set_title("Customer Support Response Time by Channel", fontsize=16, weight="bold")
ax.set_xlabel("Support Channel", fontsize=12)
ax.set_ylabel("Response Time (minutes)", fontsize=12)

# -------------------------------
# 5. Save chart
# -------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
