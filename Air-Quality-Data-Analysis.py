
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("air_quality.csv")

print(df.head())
print(df.info())

print("\nAverage AQI:", np.mean(df["AQI"]))
print("Maximum AQI:", np.max(df["AQI"]))
print("Minimum AQI:", np.min(df["AQI"]))
print("Average PM2.5:", np.mean(df["PM2.5"]))
print("Average PM10:", np.mean(df["PM10"]))

print("\nAverage AQI by City:")
print(df.groupby("City")["AQI"].mean())

print("\nAverage PM2.5 by City:")
print(df.groupby("City")["PM2.5"].mean())

print("\nAverage PM10 by City:")
print(df.groupby("City")["PM10"].mean())

sns.barplot(data=df, x="City", y="AQI", estimator="mean")
plt.title("Average AQI by City")
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="City", y="PM2.5", estimator="mean")
plt.title("Average PM2.5 by City")
plt.tight_layout()
plt.show()

sns.barplot(data=df, x="City", y="PM10", estimator="mean")
plt.title("Average PM10 by City")
plt.tight_layout()
plt.show()

sns.lineplot(data=df, x="Date", y="AQI", hue="City", marker="o")
plt.title("AQI Trends by City")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="PM2.5", y="AQI", hue="City")
plt.title("PM2.5 vs AQI")
plt.tight_layout()
plt.show()

sns.histplot(data=df, x="AQI", bins=10, kde=True)
plt.title("AQI Distribution")
plt.tight_layout()
plt.show()

print("\nAir Quality Analysis Completed!")
