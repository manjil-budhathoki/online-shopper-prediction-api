# mlops_pipeline_project/scripts/validate_data.py

import pandas as pd
from sqlalchemy import create_engine
import sys

def validate_ingested_data():
    """
    Connects to the MariaDB container, reads the ingested data,
    and performs basic quality checks.
    """
    try:
        db_user = "manjil"
        db_password = "Hevenlydemonisback"
        db_host = "localhost"
        db_port = "3306"
        db_name = "shopping_db"
        table_name = "shopping_transactions"
        
        engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

        print(f"Validation Step: Reading data from table '{table_name}'...")
        df = pd.read_sql(table_name, con=engine)
        print(f"Data read successfully. Shape: {df.shape}")

        # Validation Check 1: Check for null values
        if df.isnull().sum().sum() > 0:
            print("ERROR: Data validation failed! Null values found.")
            # Exit with a non-zero status code to make the Airflow task fail
            sys.exit(1)
        
        print("Validation Check 1 PASSED: No null values found.")

        # Validation Check 2: Check for a reasonable number of rows
        min_expected_rows = 1000
        if len(df) < min_expected_rows:
            print(f"ERROR: Data validation failed! Table has only {len(df)} rows, which is fewer than the expected minimum of {min_expected_rows}.")
            sys.exit(1)
            
        print(f"Validation Check 2 PASSED: Row count ({len(df)}) is sufficient.")
        print("--- All data validation checks passed successfully! ---")

    except Exception as e:
        print(f"An error occurred during validation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    validate_ingested_data()