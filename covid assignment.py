import pandas as pd

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# Save it locally
df.to_csv("owid-covid-data.csv", index=False)

# Confirm save
print("File saved successfully in your working directory.")


# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("owid-covid-data.csv")

# Display basic info
print("Dataset shape:", df.shape)
print("Column names:", df.columns)

# Check for missing values
print("\nMissing values per column:\n", df.isnull().sum())

# Filter for selected countries and make a copy
countries = ["Kenya", "United States", "India"]
df_filtered = df[df["location"].isin(countries)].copy()

# Convert date column to datetime
df_filtered["date"] = pd.to_datetime(df_filtered["date"])

# Drop rows with missing critical values
df_filtered = df_filtered.dropna(subset=["total_cases", "total_deaths"])

# Fill missing vaccination data with 0
df_filtered["total_vaccinations"] = df_filtered["total_vaccinations"].fillna(0)

# Add death rate column
df_filtered["death_rate"] = df_filtered["total_deaths"] / df_filtered["total_cases"]

# --- EDA & Visualizations ---

# Set the style
sns.set(style="whitegrid")

# Plot total cases over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="total_cases", hue="location")
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="total_deaths", hue="location")
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

# Plot daily new cases
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="new_cases", hue="location")
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

# Plot vaccination progress
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="total_vaccinations", hue="location")
plt.title("COVID-19 Vaccination Progress")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend(title="Country")
plt.tight_layout()
plt.show()

# Plot death rate over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df_filtered, x="date", y="death_rate", hue="location")
plt.title("COVID-19 Death Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Death Rate (Deaths / Cases)")
plt.legend(title="Country")
plt.tight_layout()
plt.show()