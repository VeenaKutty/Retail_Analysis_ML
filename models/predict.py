import pandas as pd


def make_predictions(
    model,
    X_test,
    y_test,
    meta_test
):

    # Predictions
    preds = model.predict(X_test)

    # Prediction table
    results = meta_test.copy()

    results['actual_units_sold'] = (
        y_test.values
    )

    results['predicted_units_sold'] = preds

    # Error
    results['row_error'] = abs(
        results['actual_units_sold']
        - results['predicted_units_sold']
    )

    return results, preds