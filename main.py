import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart.csv")
print("🔍 Preview of dataset:")
print(df.head())

df["DiscountApplied"] = df["Weekly_Sales"] > 1000
df.loc[df["DiscountApplied"], "Weekly_Sales"] *= 0.9

mean_sales = np.mean(df["Weekly_Sales"])
print("Mean Weekly Sales:", mean_sales)

t_stat, p_value = stats.ttest_1samp(df["Weekly_Sales"], 500)
print("T-statistic:", t_stat, "P-value:", p_value)

avg_sales = df.groupby("DiscountApplied")["Weekly_Sales"].mean()
avg_sales.plot(kind="bar")
plt.title("Avg Weekly Sales by Discount Status")
plt.xlabel("Discount Applied")
plt.ylabel("Avg Weekly Sales")
plt.xticks([0, 1], ["No", "Yes"], rotation=0)
plt.show()

df.to_csv("Walmart_updated.csv", index=False)
print("Saved.")