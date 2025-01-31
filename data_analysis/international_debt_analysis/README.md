# International Debt Analysis Project

## Project Overview
This project explores international debt data collected by **The World Bank**. The data focuses on the debts owed by developing countries across various categories. The goal of this project is to analyze the data and answer key questions about global debt patterns. By doing so, we aim to understand how countries manage their economic needs through debt.

### Key Questions
1. How many distinct countries are present in the database?
2. Which country has the highest amount of total debt?
3. Which country has the lowest amount of repayments for the principal amount?

## Dataset Details
The project uses data from the `international_debt` table, which includes the following columns:

| Column Name        | Description                                               | Data Type  |
|--------------------|-----------------------------------------------------------|------------|
| `country_name`     | Name of the country                                        | `varchar`  |
| `country_code`     | Code representing the country                              | `varchar`  |
| `indicator_name`   | Description of the debt indicator                          | `varchar`  |
| `indicator_code`   | Code representing the debt indicator                       | `varchar`  |
| `debt`             | Value of the debt indicator for the given country (in USD) | `float`    |

## Analysis
The project involves executing SQL queries to answer the key questions:

### 1. Number of Distinct Countries
To find the total number of unique countries in the dataset:

SELECT COUNT(DISTINCT country_name) AS total_distinct_countries
FROM international_debt;

### 2. Country with the Highest Debt
To identify the country with the largest total debt:

SELECT country_name, SUM(debt) AS total_debt
FROM international_debt
GROUP BY country_name
ORDER BY total_debt DESC
LIMIT 1;

### 3. Country with the Lowest Principal Repayments
To find the country with the smallest repayment amount for the principal:

SELECT country_name, indicator_name, MIN(debt) AS lowest_repayment
FROM international_debt
WHERE indicator_code = 'DT.AMT.DLXF.CD'
GROUP BY country_name, indicator_name
ORDER BY lowest_repayment
LIMIT 1; 

### Results
### Example Output
- Total Distinct Countries: 100 (replace with actual result after execution)
- Country with the Highest Debt: Country X (replace with actual result)
- Country with the Lowest Principal Repayments: Country Y (replace with actual result)
### Tools and Technologies
- Database: SQL
- Query Editor: Any SQL client (e.g., MySQL Workbench, pgAdmin, or a web-based IDE)
- Data Source: The World Bank
### How to Run
- Load the international_debt table into your SQL database.
- Execute the SQL queries provided in the Analysis section.
- Interpret the results and document insights.

