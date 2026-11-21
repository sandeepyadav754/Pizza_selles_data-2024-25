# Pizza_selles_data-2024-25
1. Project Title
Pizza Sales Analysis Using Databricks, PySpark, SQL & Power BI

2. Short Description / Purpose
This project focuses on building an end-to-end data pipeline and interactive business intelligence dashboard to analyze pizza sales data.

I developed an ETL pipeline using Databricks and PySpark with a Medallion Architecture (Bronze, Silver, and Gold) to process raw data, followed by a Power BI dashboard to visualize sales performance and generate business insights.

3. Technology Stack
Excel: Initial data inspection and preparation.

Python (PySpark): Data cleaning and transformation.

SQL: Data querying and analysis.

Apache Spark: Distributed data processing.

Databricks: ETL pipeline development using Spark Declarative Pipelines (SDP).

Power BI: Interactive dashboard and data visualization.

4. Data Source
Kaggle – Pizza Sales Dataset (2024–2025)

The dataset contains pizza sales information used to analyze orders, pizza types, sizes, payment categories, restaurants, and sales trends.

5. Features & Project Highlights
A. Business Problem
The business needs to understand pizza sales performance, identify popular pizza categories, compare restaurant performance, and analyze monthly order trends.

B. Goal of the Dashboard
To transform raw pizza sales data into meaningful business insights through an automated ETL pipeline and interactive Power BI dashboard.

C. Databricks ETL Pipeline – Spark Declarative Pipelines (SDP)
Developed a three-layer Medallion Architecture:

1. Bronze Layer – raw_data

Ingested raw pizza sales data.

Created the initial pipeline table using @dp.table.

Maintained the raw data as the starting point for processing.

2. Silver Layer – silver_data_new

Cleaned and transformed raw data using PySpark.

Applied data preparation and quality checks.

Created a materialized view using @dp.materialized_view.

3. Gold Layer – gold_data_new

Prepared business-ready data for reporting and analysis.

Created the final analytical layer using @dp.materialized_view.

Used the processed data for Power BI reporting.

D. Power BI Dashboard – Key Visuals
Monthly Orders: Identifies high- and low-performing months.

Pizza Type: Analyzes different pizza categories.

Payment Category: Compares online and offline payments.

Pizza Size: Analyzes customer preferences by pizza size.

Restaurant Performance: Compares restaurants across locations.

Highest Selling Pizza: Identifies popular pizza categories.

Traffic Impact: Visualizes traffic levels and their relationship with pizza types and restaurants.

E. Business Impact & Insights
Identifies monthly order trends and seasonal performance.

Highlights popular pizza categories.

Helps understand customer payment and size preferences.

Provides restaurant-level performance comparisons.

Supports sales planning, inventory management, and business decision-making.

6. Project Outcome
Successfully developed an end-to-end data processing pipeline using Databricks SDP and PySpark, following Medallion Architecture, and connected the processed data to an interactive Power BI dashboard for business analysis.




Screenshort :-https://github.com/sandeepyadav754/Pizza_selles_data-2024-25/blob/main/Screenshot%202026-11-19%20205436.png
