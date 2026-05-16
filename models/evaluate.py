from sklearn.metrics import (
    mean_absolute_error,
    r2_score
)


def evaluate_model(y_test, preds):

    mae = mean_absolute_error(
        y_test,
        preds
    )

    r2 = r2_score(
        y_test,
        preds
    )

    print(f"MAE: {mae}")
    print(f"R2: {r2}")

    return mae, r2