from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from models.preprocess import preprocess_for_ml

import pandas as pd


def train_model(df):

    # Preserve metadata
    metadata_cols = [
        'date',
        'product_id',
        'region',
        'category'
    ]

    metadata = df[metadata_cols].copy()

    # ML preprocessing
    ml_df = preprocess_for_ml(df)

    # Features & target
    X = ml_df.drop(columns=['units_sold'])

    y = ml_df['units_sold']

    # Ensure numeric
    X = X.astype(float)

    # Split everything together
    (
        X_train,
        X_test,
        y_train,
        y_test,
        meta_train,
        meta_test
    ) = train_test_split(
        X,
        y,
        metadata,
        test_size=0.2,
        random_state=42
    )

    # Model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    # Train
    model.fit(X_train, y_train)

    return (
        model,
        X_test,
        y_test,
        meta_test
    )