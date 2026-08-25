import os
import json
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

# Set the main project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / ".env")

# Read file paths from .env
CSV_FILE_NAME = os.getenv("DATA_PATH", "data/billing_sample.csv")
FULL_JSON_NAME = os.getenv("FULL_JSON_PATH", "data/billing_full.json")
SUMMARY_JSON_NAME = os.getenv("SUMMARY_JSON_PATH", "data/billing_summary.json")

# Convert relative paths to absolute paths
DATA_PATH = BASE_DIR / CSV_FILE_NAME
FULL_JSON_PATH = BASE_DIR / FULL_JSON_NAME
SUMMARY_JSON_PATH = BASE_DIR / SUMMARY_JSON_NAME


def load_billing_data(file_path: Path) -> pd.DataFrame:
    """Load the CSV file into a pandas DataFrame."""
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"Data loaded successfully: {len(df)} rows found.")
    return df


def save_full_json(df: pd.DataFrame, output_path: Path) -> None:
    """Save all CSV data as a JSON file."""
    df.to_json(output_path, orient="records", indent=4)
    print(f"Full data saved to: {output_path}")


def save_summary_json(df: pd.DataFrame, output_path: Path) -> None:
    """Save basic data summary as a JSON file."""
    summary = {
        "total_records": int(len(df)),
        "total_billed_cost": float(df["BilledCost"].sum()),
        "providers": df["ProviderName"].dropna().unique().tolist(),
        "services_count": int(df["ServiceName"].nunique()),
        "sample_services": df["ServiceName"].dropna().unique()[:5].tolist()
    }
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)
        
    print(f"Summary saved to: {output_path}")


if __name__ == "__main__":
    df_billing = load_billing_data(DATA_PATH)
    save_full_json(df_billing, FULL_JSON_PATH)
    save_summary_json(df_billing, SUMMARY_JSON_PATH)