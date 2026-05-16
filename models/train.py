from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

from models.preprocess import preprocess_for_ml


def train_model(df):

    ml_df = preprocess_for_ml(df)

    X = ml_df.drop(
        columns=['units_sold']
    )

    y = ml_df['units_sold']

    # Convert all numeric
    X = X.astype(float)

    # Split
    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    # Model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    return model, X_test, y_test