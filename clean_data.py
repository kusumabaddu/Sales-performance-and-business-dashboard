
from pathlib import Path
import pandas as pd

# Locate the project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "sample_-_superstore.xls"
OUTPUT_FILE = PROJECT_DIR / "data" / "cleaned_superstore.csv"

# 1. Load the dataset
df = pd.read_excel(DATA_FILE)

print("Original dataset shape:", df.shape)

# 2. Clean column names
df.columns = df.columns.str.strip()

# Remove accidental spaces from text values
for column in df.select_dtypes(include=["object"]).columns:
    df[column] = df[column].map(
        lambda value: value.strip() if isinstance(value, str) else value
    )

# 3. Check missing values before making changes
print("\nMissing values before cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 4. Remove only completely identical rows
duplicate_count = int(df.duplicated().sum())
print("\nCompletely duplicated rows:", duplicate_count)

df = df.drop_duplicates()

# 5. Convert date columns to proper dates
for column in ["Order Date", "Ship Date"]:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column], errors="coerce"
        )

# 6. Convert important numeric columns
numeric_columns = [
    "Sales", "Profit", "Quantity", "Discount"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

# 7. Check data quality after cleaning
print("\nDataset shape after cleaning:", df.shape)

print("\nData types:")
print(df.dtypes)

print("\nMissing values after cleaning:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# 8. Basic business summary
if "Sales" in df.columns:
    print("\nTotal Sales:", round(df["Sales"].sum(), 2))

if "Profit" in df.columns:
    print("Total Profit:", round(df["Profit"].sum(), 2))

if "Order ID" in df.columns:
    print("Unique Orders:", df["Order ID"].nunique())

# 9. Export the cleaned dataset
df.to_csv(OUTPUT_FILE, index=False)

print("\nCleaned dataset saved successfully:")
print(OUTPUT_FILE)