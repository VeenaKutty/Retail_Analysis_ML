from etl.extract import extract_data
from etl.transform import transform_data

from etl.load_dimensions import (
    load_dimensions
)

from etl.load_facts import (
    load_fact_table
)

from models.train import train_model

from models.predict import (
    make_predictions
)

from models.evaluate import (
    evaluate_model
)

from etl.utils import (
    load_predictions
)


def run():

    print("=" * 50)
    print("RETAIL INVENTORY ML PIPELINE STARTED")
    print("=" * 50)

    # ====================================
    # 1. EXTRACT
    # ====================================

    print("\n[1] Extracting Data...")

    df = extract_data(
        "data/retail_store_inventory.csv"
    )

    print("Data Extracted Successfully")
    print(f"Dataset Shape: {df.shape}")

    # ====================================
    # 2. TRANSFORM
    # ====================================

    print("\n[2] Transforming Data...")

    df = transform_data(df)

    print("Data Transformation Completed")

    # ====================================
    # 3. LOAD DIMENSIONS
    # ====================================

    print("\n[3] Loading Dimension Tables...")

    load_dimensions(df)

    print("Dimension Tables Loaded")

    # ====================================
    # 4. LOAD FACT TABLE
    # ====================================

    print("\n[4] Loading Fact Table...")

    load_fact_table(df)

    print("Fact Table Loaded")

    # ====================================
    # 5. TRAIN MODEL
    # ====================================

    print("\n[5] Training ML Model...")

    (
        model,
        X_test,
        y_test,
        meta_test
    ) = train_model(df)

    print("Model Training Completed")

    # ====================================
    # 6. PREDICTIONS
    # ====================================

    print("\n[6] Generating Predictions...")

    results, preds = make_predictions(
        model,
        X_test,
        y_test,
        meta_test
    )

    print("Predictions Generated")

    # ====================================
    # 7. EVALUATION
    # ====================================

    print("\n[7] Evaluating Model...")

    mae, r2 = evaluate_model(
        y_test,
        preds
    )

    print(f"MAE Score: {mae}")
    print(f"R2 Score: {r2}")

    # ====================================
    # 8. LOAD PREDICTIONS
    # ====================================

    print("\n[8] Loading Prediction Table...")

    load_predictions(results)

    print("Prediction Table Loaded")

    # ====================================
    # PIPELINE COMPLETED
    # ====================================

    print("\n" + "=" * 50)
    print("PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    run()