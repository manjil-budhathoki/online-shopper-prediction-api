# mlops_pipeline_project/scripts/preprocess_data.py

import pandas as pd
from sqlalchemy import create_engine
import os
import joblib

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def preprocess_data():
    """
    Reads data from the database, applies all preprocessing transformations,
    and saves the fully processed dataset and the fitted preprocessor.
    """
    try:
        # --- 1. Connect and Read Data ---
        db_user = "manjil"
        db_password = "Hevenlydemonisback"
        db_host = "localhost"
        db_port = "3306"
        db_name = "shopping_db"
        table_name = "shopping_transactions"
        
        engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

        print("Preprocessing Step: Reading data from the database...")
        df = pd.read_sql(table_name, con=engine)
        print(f"Data read successfully. Shape: {df.shape}")

        # --- 2. Define Features and Target ---
        df['Revenue'] = df['Revenue'].astype(int)
        categorical_features = ['Month', 'VisitorType']
        numerical_features = ['Administrative', 'Administrative_Duration', 'Informational', 
                              'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 
                              'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay']
        target = 'Revenue'
        
        X = df[categorical_features + numerical_features]
        y = df[target]

        # --- 3. Create and Fit the Preprocessing Pipeline ---
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
            ],
            remainder='passthrough' # Keep other columns if any
        )

        print("Fitting the preprocessor on the entire dataset...")
        X_processed = preprocessor.fit_transform(X)
        print("Preprocessing applied successfully.")

        # --- 4. Save the Artifacts ---
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'processed_data')
        os.makedirs(output_dir, exist_ok=True)
        print(f"Saving artifacts to: {output_dir}")
        
        # Save the fully processed features and the original target Series
        full_dataset_path = os.path.join(output_dir, 'full_processed_dataset.joblib')
        joblib.dump({'features': X_processed, 'target': y}, full_dataset_path)

        # Save the fitted preprocessor object
        preprocessor_path = os.path.join(output_dir, 'preprocessor.joblib')
        joblib.dump(preprocessor, preprocessor_path)

        print("--- Preprocessing complete. Full dataset and preprocessor saved. ---")

    except Exception as e:
        print(f"An error occurred during preprocessing: {e}")
        import sys
        sys.exit(1)

if __name__ == "__main__":
    preprocess_data()