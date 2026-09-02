# Swiggy Exploratory Data Analysis (EDA)

A comprehensive Python-based exploratory data analysis of India's leading food delivery platform, Swiggy. This project investigates pricing trends, geographic restaurant distribution, and customer rating patterns across 148,541 restaurants in 821 cities.

## Project Overview

This repository demonstrates an end-to-end data science workflow, from raw data extraction and modular preprocessing to advanced statistical visualization. The analysis identifies key market concentrations, long-tail geographic distributions, and pricing dynamics within the Indian food delivery ecosystem.

## Key Insights

* **Budget Dominance:** Approximately 90% of listed restaurants (over 133,000) are highly budget-friendly, charging ₹400 or less for a meal.
* **The Rating Gap:** Over 50% of the raw dataset contains a rating of exactly `0.0`, highlighting a massive influx of new, untested, or unrated vendor listings on the platform. Rated restaurants maintain an average score of 3.8.
* **Pricing Outliers:** Data cleaning resolved severe pricing anomalies (including extreme data-entry errors up to ₹300,350) and standardized string variables containing hidden text and currency symbols.

## Repository Structure

```text
├── data/
│   ├── raw/                  # Original, uncleaned Swiggy dataset
│   └── processed/            # Cleaned data (CSV/Parquet) ready for analysis
├── notebooks/                # Jupyter notebooks for EDA and visualization
├── src/                      
│   └── data_cleaning.py      # Modular scripts for regex parsing and type conversion
├── images/              # Auto-generated high-resolution PNG plots
├── .gitignore                # Environment and large file exclusions
└── README.md                 # Project documentation
