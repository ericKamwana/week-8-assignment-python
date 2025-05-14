# 🦠 COVID-19 Global Data Tracker

**Author:** Eric Kamwana  
**Project Type:** Data Analysis & Visualization  
**Platform:** Jupyter Notebook  
**Tools Used:** Python, Pandas, Matplotlib, Seaborn  
**Dataset:** [Our World in Data – COVID-19 Dataset](https://ourworldindata.org/covid-deaths)

---

## 📘 Project Overview

The **COVID-19 Global Data Tracker** is a data analysis project that explores global trends in COVID-19 cases, deaths, and vaccinations using real-world data. This report focuses on three selected countries — **Kenya**, **India**, and the **United States** — and provides insights into how each responded to the pandemic over time.

This analysis was conducted in Python using `pandas`, `matplotlib`, and `seaborn`, and is structured step-by-step with visuals and narrative explanations.

---

## 🎯 Project Objectives

- ✅ Import and clean COVID-19 data
- ✅ Analyze time trends (cases, deaths, vaccinations)
- ✅ Compare metrics across countries
- ✅ Visualize trends using line and bar charts
- ✅ Communicate insights in a clear, professional format

---

## 📂 Project Structure

### 1️⃣ Data Collection
- Source: `owid-covid-data.csv` from Our World in Data
- Stored locally in the Jupyter Notebook working directory

### 2️⃣ Data Loading & Exploration
- Loaded using `pandas.read_csv()`
- Explored data using `.head()`, `.info()`, `.isnull().sum()`
- Identified key columns:
  - `date`
  - `location`
  - `total_cases`, `total_deaths`
  - `new_cases`, `new_deaths`
  - `total_vaccinations`

### 3️⃣ Data Cleaning
- Filtered for: Kenya, India, and the United States
- Converted `date` to datetime using `pd.to_datetime()`
- Dropped rows with missing `total_cases` or `total_deaths`
- Handled missing values using `.fillna(0)` for vaccination data

### 4️⃣ Exploratory Data Analysis (EDA)
- 📈 **Total Cases Over Time:** Line chart for each country
- 📉 **Total Deaths Over Time:** Line chart comparison
- 📊 **Daily New Cases:** Compared daily spikes and trends
- 💀 **Death Rate Analysis:** Computed as `total_deaths / total_cases`

### 5️⃣ Vaccination Progress
- 📈 Line chart: Total vaccinations over time
- 📊 Compared vaccination rollouts between countries

### 6️⃣ Optional Choropleth Map
- ❌ Not implemented (Optional step)

### 7️⃣ Key Insights
- The United States had the highest case numbers but also led in vaccinations.
- India experienced sharp waves but showed strong recovery phases.
- Kenya had fewer total cases but a slower vaccination rollout.
- Death rates varied significantly, revealing healthcare system gaps.

---

## 📊 Visualizations Included

- Line Charts: Total Cases, Deaths, and Vaccinations
- Bar Chart: New Cases Comparison
- Death Rate Calculations
- Clean and readable visuals styled with Seaborn

---

## 🛠 Tools & Libraries

- `pandas` – Data manipulation
- `matplotlib` – Plotting & visualizations
- `seaborn` – Advanced visual styling
- Jupyter Notebook – Development environment

---

## 📝 How to Run the Project

1. Download the dataset: `owid-covid-data.csv`  
   Link: [Our World in Data COVID Dataset](https://ourworldindata.org/covid-deaths)
2. Open the Jupyter Notebook file.
3. Ensure the CSV file is in the same working directory.
4. Run all cells step by step.

---

## 📌 File List

- `covid_data_analysis.ipynb` – Main Jupyter Notebook
- `owid-covid-data.csv` – Source dataset
- `README.md` – Project summary (this file)
- `covid_report.pdf` – Exported PDF (optional, for presentation)

---

## 💬 Credits & Acknowledgments

- **Dataset:** [Our World in Data](https://ourworldindata.org/covid-deaths)
- **Mentorship & Tools:** Powered by the guidance from my PLP Academy training

---

## 📢 Author's Note

This project was part of my journey in becoming a professional data-driven developer and analyst. Special thanks to the PLP Tech Academy for the structure, and to everyone supporting the **Marketash** vision.

For any collaboration or questions, feel free to reach out!

---

**Slogan:** “Track the Virus. Inform the Future.”

