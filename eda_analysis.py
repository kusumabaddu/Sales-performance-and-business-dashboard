
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "cleaned_superstore.csv"
REPORTS_DIR = PROJECT_DIR / "reports"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(DATA_FILE, parse_dates=["Order Date"])

# Create useful date columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

# 1. Overall business KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
profit_margin = (total_profit / total_sales * 100) if total_sales else 0
average_order_value = total_sales / total_orders if total_orders else 0

print("\n========== OVERALL BUSINESS KPIs ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Unique Orders: {total_orders:,}")
print(f"Unique Customers: {total_customers:,}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Average Order Value: ${average_order_value:,.2f}")

# 2. Monthly sales and profit
monthly = (
    df.groupby("Year-Month", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .sort_values("Year-Month")
)

monthly.to_csv(REPORTS_DIR / "monthly_performance.csv", index=False)

print("\n========== MONTHLY PERFORMANCE ==========")
print(monthly.to_string(index=False))

# 3. Category performance
category = (
    df.groupby("Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

category.to_csv(REPORTS_DIR / "category_performance.csv", index=False)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category.to_string(index=False))

# 4. Regional performance
region = (
    df.groupby("Region", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Orders=("Order ID", "nunique")
    )
    .sort_values("Sales", ascending=False)
)

region.to_csv(REPORTS_DIR / "regional_performance.csv", index=False)

print("\n========== REGIONAL PERFORMANCE ==========")
print(region.to_string(index=False))

# 5. Sub-category performance
subcategory = (
    df.groupby("Sub-Category", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Profit", ascending=True)
)

subcategory.to_csv(
    REPORTS_DIR / "subcategory_performance.csv",
    index=False
)

print("\n========== LOWEST PROFIT SUB-CATEGORIES ==========")
print(subcategory.head(10).to_string(index=False))

# 6. Top 10 products by sales
products = (
    df.groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
    .head(10)
)

products.to_csv(REPORTS_DIR / "top_10_products.csv", index=False)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(products.to_string(index=False))

# 7. Products with negative total profit
loss_products = (
    df.groupby("Product Name", as_index=False)
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

loss_products = (
    loss_products[loss_products["Profit"] < 0]
    .sort_values("Profit")
)

loss_products.to_csv(
    REPORTS_DIR / "loss_making_products.csv",
    index=False
)

print("\n========== LOSS-MAKING PRODUCTS ==========")
print("Products with negative total profit:", len(loss_products))
print(loss_products.head(10).to_string(index=False))

print("\nEDA completed successfully!")
print("Reports saved to:", REPORTS_DIR)