# Customer Shopping Behavior Analysis

This project is a comprehensive data analysis of customer shopping behavior, utilizing Python for data processing, SQL for in-depth analysis, and Power BI for visual reporting.

## Project Overview

The goal of this project is to analyze customer purchasing patterns, segment customers, and derive actionable insights to improve business strategies. The project covers the full data pipeline from extraction and transforming to loading and visualization.

## Data Source

The dataset used in this project is sourced from the [Customer Trends Data Analysis](https://github.com/amlanmohanty1/customer-trends-data-analysis-SQL-Python-PowerBI) repository.

## Project Structure

- **`customer_shopping_analysis.py`**: A Python script that loads the raw CSV data, performs data cleaning and feature engineering (e.g., creating age groups, standardizing columns), and uploads the processed data to a PostgreSQL database.
- **`behaviour.sql`**: A collection of SQL queries used to extract key insights from the database, such as revenue by gender, customer segmentation, and product performance.
- **`Customer_Shopping_Dashboard.pbix`**: A Power BI dashboard file that visualizes the data and insights.
- **`customer_shopping_behavior.csv`**: The raw dataset used for analysis (not included in repo, see **Data Source**).

## Prerequisites

To run this project, you will need:

- **Python 3.x**
- **PostgreSQL**: A local installation or access to a PostgreSQL server.
- **Power BI Desktop**: To view and interact with the dashboard.

### Python Libraries

Install the required Python libraries:

```bash
pip install pandas sqlalchemy psycopg2
```

> **Note:** You may need to create a `database.ini` or update the credentials in `customer_shopping_analysis.py` to match your local PostgreSQL configuration.

## Setup & Usage

1.  **Database Setup**:
    - Ensure you have a PostgreSQL database named `customer_behaviour` created.
    - Update the database connection details (username, password, host, port) in `customer_shopping_analysis.py` (lines 45-49).

2.  **Run the Python Script**:
    - Execute the script to clean the data and load it into the database:
      ```bash
      python customer_shopping_analysis.py
      ```
    - This will create and populate the `behavior` table in your database.

3.  **Run SQL Analysis**:
    - Open `behaviour.sql` in your preferred SQL client (e.g., pgAdmin, DBeaver) connected to the `customer_behaviour` database.
    - Execute the queries to generate insights.

4.  **View Dashboard**:
    - Open `Customer_Shopping_Dashboard.pbix` with Power BI Desktop to explore the visualizations.

## Key Analysis Provided

The SQL scripts and dashboard cover various analytical aspects, including:

- **Revenue Analysis**: Total revenue breakdown by gender and age group.
- **Customer Segmentation**: Categorizing customers into New, Returning, and Loyal segments based on purchase history.
- **Product Performance**: Identifying top-rated products and best-sellers within categories.
- **Behavioral Insights**: Analyzing the impact of discounts, shipping types, and subscription status on spending.

