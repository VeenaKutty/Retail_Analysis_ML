import pandas as pd


def make_predictions(
    model,
    X_test,
    y_test
):

    preds = model.predict(X_test)

    results = pd.DataFrame({
        'actual_units_sold': y_test,
        'predicted_units_sold': preds
    })

    results['row_error'] = abs(
        results['actual_units_sold']
        - results['predicted_units_sold']
    )

    return results, preds