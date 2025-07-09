# 📊 Cleaned Netflix Dataset Analysis with Pandas & NumPy

This project focuses on cleaning and analyzing the [Netflix Movies and TV Shows dataset](https://www.kaggle.com/datasets) using **Pandas** and **NumPy** in Python. The dataset contains information about movies and shows available on Netflix, including title, director, country, release year, genre, and more.

## 📁 Files Included

- `Netflix_Dataset.csv` – Raw dataset
- `Cleaned_Netflix_Dataset.csv` – Cleaned and preprocessed dataset
- `Cleaning.py` – Python script for cleaning, filtering, and analyzing the dataset

---

## 🧹 Data Cleaning Tasks

- Removed duplicates
- Filled missing values in `director` and `country` columns
- Created a new column `is_recent` for content released after 2020
- Extracted top genres and directors
- Filtered movies vs TV shows
- Filtered Indian movies, comedy content, and "Love" in titles
- Analyzed release trends and country-wise distribution

---

## 📊 Analysis Highlights

- 📈 Total Movies and TV Shows count
- 🎭 Top 10 frequent genres
- 🎬 Top 5 most-featured directors
- 🌍 Country-wise distribution of titles
- 🆕 Recent genre trends (2020 onwards)

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy

---

## 🚀 Getting Started

1. Clone the repo or download the folder.
2. Make sure you have the required packages:

``bash
pip install pandas numpy
Run the script:

python Cleaning.py

📌 Notes
This project is for data cleaning and EDA practice.

The dataset was sourced from Kaggle and may change over time.

The cleaned dataset can be used for visualization and ML in future steps.

📚 Future Work
Data Visualization using Matplotlib and Seaborn

Build a Netflix recommendation system

Publish visual dashboards on Streamlit or Tableau

📬 Contact
Made with 💻 by [Amaar Ali]
For feedback or collaboration: GitHub
