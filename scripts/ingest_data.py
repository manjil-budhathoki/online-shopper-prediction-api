# mlops_pipeline_project/scripts/ingest_data.py

import pandas as pd
from sqlalchemy import create_engine
import os

def ingest_shopping_data():
    """
    Connects to the MariaDB container, reads shopping data from a local CSV,
    and ingests it into the shopping_db database.
    """
    # --- 1. Database Connection Details ---
    # These are the credentials you set up for your MariaDB container
    db_user = "manjil"
    db_password = "Hevenlydemonisback"
    db_host = "localhost"  # Or the IP if your container is elsewhere
    db_port = "3306"       # The port you mapped with `docker run -p 3306:3306 ...`
    db_name = "shopping_db"
    
    # --- 2. Create the Database Connection Engine ---
    try:
        engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
        print("Successfully connected to the MariaDB container.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return

    # --- 3. Read the Local Data ---
    # Assumes your data is in a 'data' folder at the same level as 'scripts'
    try:
        # Construct the full path to the data file
        script_dir = os.path.dirname(__file__)
        data_path = os.path.join(script_dir, '..', 'data', 'online_shoppers_intention.csv')
        
        df = pd.read_csv(data_path)
        print(f"Successfully loaded data from {data_path}. Shape: {df.shape}")
    except FileNotFoundError:
        print(f"Error: The file was not found at {data_path}")
        return
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # --- 4. Ingest the Data into MariaDB ---
    table_name = "shopping_transactions"  # Choose a name for your table
    try:
        # if_exists='replace': Drops the table before inserting new data.
        # Use 'append' if you want to add to existing data.
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        print(f"Successfully ingested data into the '{table_name}' table in the '{db_name}' database.")
    except Exception as e:
        print(f"Error ingesting data into the database: {e}")

if __name__ == "__main__":
    ingest_shopping_data()