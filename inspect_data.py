
from pathlib import Path
import pandas as pd

# Locate the project and dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_DIR / "data" / "sample_-_superstore.xls"

if not DATA_FILE.exists():
    print("Dataset not found!")
    print("Expected location:", DATA_FILE)
else:
    # Display available sheets in the Excel workbook
    excel_file = pd.ExcelFile(DATA_FILE)

    print("\nAvailable sheets:")
    print(excel_file.sheet_names)

    # Load the first sheet
    df = pd.read_excel(DATA_FILE, sheet_name=0)

    print("\nFirst five rows:")
    print(df.head())

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nDataset dimensions:")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])

    print("\nColumn data types and non-null values:")
    df.info()

    print("\nMissing values per column:")
    print(df.isnull().sum())