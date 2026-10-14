# Sales Performance & Business Intelligence Dashboard

## Project Overview

The **Sales Performance & Business Intelligence Dashboard** is a data analytics project developed to analyze sales transactions, evaluate business profitability, and identify trends across product categories and geographic regions.

The project uses Python for data cleaning and exploratory data analysis, PostgreSQL for data storage and SQL-based analysis, and Power BI for interactive dashboard development.

The goal is to transform raw sales data into meaningful business insights that support data-driven decision-making.

## Objectives

- Analyze total sales, profit, and profit margin.
- Identify high-performing product categories and regions.
- Track monthly sales performance.
- Evaluate product-level profitability.
- Identify loss-making products that may require further investigation.
- Build an interactive dashboard for business reporting.

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and exploratory data analysis |
| Pandas | Data manipulation and transformation |
| PostgreSQL | Data storage and querying |
| SQL | Sales, profit, category, and regional analysis |
| Power BI Desktop | Interactive dashboard and visualization |
| DAX | KPI calculations and business measures |
| Git & GitHub | Version control and project documentation |

## Dataset

The project uses a Superstore sample sales dataset containing **10,194 records and 21 columns**.

The dataset includes information about:

- Order and shipping dates
- Customer names and segments
- Product categories and subcategories
- Sales, quantity, discount, and profit
- Geographic information, including city, state, and region

**Note:** Check the dataset's licensing and redistribution terms before uploading the raw or cleaned dataset to a public repository.

## Project Workflow

### 1. Data Inspection and Cleaning — Python

Used Python and Pandas to inspect the dataset, standardize column names, review data quality, and prepare the data for analysis.

Key activities:
- Inspected dataset dimensions and column types.
- Standardized column names.
- Checked missing values and duplicate records.
- Exported the cleaned dataset to CSV format.

### 2. Database Setup — PostgreSQL

Created a PostgreSQL database named `sales_dashboard` and imported the cleaned sales data into the `superstore` table.

Database operations included:
- Creating the database and table.
- Importing the cleaned CSV file.
- Verifying the number of imported records.
- Checking sales and profit totals.

### 3. SQL Analysis

Used SQL queries to analyze:
- Overall sales and profit.
- Profit margin.
- Number of unique orders.
- Sales and profit by category.
- Regional performance.
- Top-selling products.
- Products generating losses.

### 4. Dashboard Development — Power BI

Connected Power BI Desktop to PostgreSQL and created DAX measures for key performance indicators.

Planned dashboard components include:
- Total Sales KPI card
- Total Profit KPI card
- Total Orders KPI card
- Total Customers KPI card
- Profit Margin KPI card
- Sales by Category chart
- Profit by Region chart
- Monthly Sales Trend chart
- Interactive slicers for region, category, and order date
- Product profitability analysis

## Key Business Insights

Based on the SQL analysis:

- **Technology** generated the highest sales and profit among the three main product categories.
- **Furniture** generated substantial sales but considerably lower profit, making its profitability worth investigating.
- The **West region** recorded the highest sales and profit among the four regions.
- The **South region** recorded the lowest sales.
- Product-level analysis highlighted items with negative profit that may require further investigation into discounts, pricing, and costs.

These findings demonstrate how sales data can help identify strong-performing areas and opportunities for further business analysis.

## Key Performance Indicators

The initial PostgreSQL analysis produced the following results:

| KPI | Result |
|---|---:|
| Total Sales | $2,326,534.44 |
| Total Profit | $292,295.93 |
| Unique Orders | 5,111 |
| Profit Margin | 12.56% |

*Note: KPI values should be validated against the final Power BI dashboard before publishing. The customer count should be taken from the verified dashboard measure.*

## Project Structure

```text
sales-performance-dashboard/
├── data/
│   ├── sample_-_superstore.xls
│   └── cleaned_superstore.csv
├── python/
│   ├── inspect_data.py
│   ├── clean_data.py
│   └── eda_analysis.py
├── sql/
│   └── sales_analysis.sql
├── dashboard/
│   └── Sales_Performance_Dashboard.pbix
├── reports/
│   ├── monthly_performance.csv
│   ├── category_performance.csv
│   ├── regional_performance.csv
│   ├── subcategory_performance.csv
│   ├── top_10_products.csv
│   └── loss_making_products.csv
└── README.md
```

*Include only files that actually exist in your project. If you do not have permission to redistribute the dataset, exclude the raw and cleaned data files and document how to obtain the source data.*

## How to Run the Project

### Prerequisites

Install or configure:
- Python
- PostgreSQL
- Power BI Desktop

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd sales-performance-dashboard
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository's actual URL.

### Step 2: Install Python Dependencies

Create and activate a virtual environment in Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the required libraries:

```powershell
python -m pip install pandas openpyxl xlrd
```

Run the scripts from the project root:

```powershell
python python/inspect_data.py
python python/clean_data.py
python python/eda_analysis.py
```

### Step 3: Create the PostgreSQL Database

Create a database named `sales_dashboard` in PostgreSQL.

Create the required `superstore` table using the schema documented in the project, then import the cleaned CSV data.

Ensure that the CSV column order and data types match the database table before importing.

### Step 4: Execute SQL Analysis

Run the SQL analysis file using `psql`:

```powershell
psql -U postgres -d sales_dashboard -f "sql/sales_analysis.sql"
```

If `psql` is not in your system PATH, use its full installation path.

### Step 5: Open the Power BI Dashboard

1. Open `dashboard/Sales_Performance_Dashboard.pbix`.
2. Configure the PostgreSQL connection if prompted.
3. Refresh the data.
4. Verify the KPI cards, charts, and slicers.

## Future Enhancements

- Add customer segmentation and repeat-purchase analysis.
- Analyze discount impact on profitability.
- Add year-over-year and month-over-month comparisons.
- Improve the dashboard layout and visual formatting.
- Automate data refresh and reporting.
- Add screenshots of the completed dashboard to the repository.

## Learning Outcomes

Through this project, I practiced:
- Data cleaning and transformation with Python and Pandas.
- Relational database setup and CSV imports with PostgreSQL.
- SQL aggregation, grouping, and profitability analysis.
- DAX measures and interactive Power BI visuals.
- Converting analytical results into actionable business insights.

## Author

**Kusuma**

Aspiring Data Analyst | Python | SQL | PostgreSQL | Power BI

This project demonstrates my practical learning in data analytics, business intelligence, and data-driven problem-solving.
