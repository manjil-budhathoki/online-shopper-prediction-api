# mlops_pipeline_project/scripts/split_data.py

import joblib
import os
import numpy as np
from sklearn.model_selection import train_test_split

def split_data():
    """
    Reads the fully processed dataset, splits it into training and testing sets,
    and saves the final training/testing artifacts.
    """
    try:
        # --- 1. Load the Processed Dataset ---
        processed_data_dir = os.path.join(os.path.dirname(__file__), '..', 'processed_data')
        full_dataset_path = os.path.join(processed_data_dir, 'full_processed_dataset.joblib')
        
        print(f"Data Splitting Step: Loading data from {full_dataset_path}...")
        data = joblib.load(full_dataset_path)
        X = data['features']
        y = data['target']
        print("Data loaded successfully.")

        # --- 2. Split the Data ---
        print("Splitting data into training and testing sets (80/20)...")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        print(f"Data split successfully. X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

        # --- 3. Save the Final Training/Testing Artifacts ---
        # Define output directory for our final artifacts
        output_dir = os.path.join(os.path.dirname(__file__), '..', 'training_data')
        os.makedirs(output_dir, exist_ok=True)
        print(f"Saving final training and testing data to: {output_dir}")
        
        # Save the split data arrays
        training_data_path = os.path.join(output_dir, 'training_testing_sets.npz')
        np.savez_compressed(training_data_path, 
                            X_train=X_train, 
                            X_test=X_test, 
                            y_train=y_train.to_numpy(), 
                            y_test=y_test.to_numpy())

        print("--- Data splitting complete. Final artifacts saved successfully! ---")

    except Exception as e:
        print(f"An error occurred during data splitting: {e}")
        import sys
        sys.exit(1)

if __name__ == "__main__":
    split_data()