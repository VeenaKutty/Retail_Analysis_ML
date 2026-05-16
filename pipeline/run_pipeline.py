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

from etl.utils import load_predictions


def run():

    print("Pipeline Started")

    # Extract
    df = extract_data(
        "data/retail_store_inventory.csv"
    )

    # Transform
    df = transform_data(df)

    # Load dimensions
    load_dimensions(df)

    # Load facts
    load_fact_table(df)

    # Train model
    model, X_test, y_test = (
        train_model(df)
    )

    # Predictions
    results, preds = (
        make_predictions(
            model,
            X_test,
            y_test
        )
    )

    # Evaluation
    evaluate_model(
        y_test,
        preds
    )

    # Load predictions
    load_predictions(results)

    print("Pipeline Completed")


if __name__ == "__main__":
    run()