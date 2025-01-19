# Fraud Detection Dashboard

## Overview

This project demonstrates the use of a fraud detection dataset to build a dashboard using Looker. The dashboard provides insights into transaction patterns, user behavior, and potential fraudulent activities, making it a valuable addition to your portfolio.

## Dataset Description

The dataset contains 10,000 records of transaction data 

# Steps to Build the Dashboard

## 1. Import Data into Looker

- Upload the CSV dataset to a SQL database (e.g., BigQuery, MySQL, PostgreSQL).

- Connect Looker to your database and create a new LookML project.

- Create a model and explore based on the table imported.

## 2. Define Key Metrics and Dimensions

Metrics:

- Total Transactions: Total number of transactions.

- Total Transaction Amount: Sum of all transaction amounts.

- Fraud Rate: Percentage of flagged fraudulent transactions.

- Average Transaction Amount: Average transaction value.

Dimensions:

- Transaction Date: Filter and group data by date.

- Location: Identify cities with the most flagged transactions.

- Device: Understand which devices are most prone to fraud.

## 3. Create Visualizations

### Suggested Charts:

Overview Tile (KPIs):

- Total Transactions

- Total Transaction Amount

- Fraud Rate

- Average Transaction Amount

### Fraud Trends Over Time:

- Line chart showing the number of flagged transactions over time.

### Fraud by Location:

- Bar chart displaying flagged fraud counts by location.

- Geographic map visualizing flagged transactions per city.

### Fraud by Device:

- Pie chart showing the distribution of flagged transactions across device types.

- Transaction Amount Distribution:

- Histogram displaying the distribution of transaction amounts.

## 4. Add Filters

- Date Range: Filter data by transaction date.

- Location: Focus on specific cities.

- Device Type: Narrow down to a specific device.

- Transaction Amount Range: Filter by low, medium, or high-value transactions.

## 5. Customize the Dashboard

- Add descriptive titles and tooltips for clarity.

- Use conditional formatting to highlight high-risk areas (e.g., locations with high fraud rates).

- Enable drill-throughs for detailed transaction-level analysis.

## Example Dashboard Layout

Header Section:

- KPI tiles for key metrics.

Trend Analysis:

- Line chart of fraud trends over time.

Geographic Analysis:

- Map and bar chart of flagged transactions by location.

Device Analysis:

- Pie chart of flagged transactions by device.

Detailed Table:

- Table displaying transaction-level data for further investigation.

