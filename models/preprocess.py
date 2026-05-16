import pandas as pd


def preprocess_for_ml(df):

    ml_df = df.copy()

    # Date features
    ml_df['year'] = (
        ml_df['date'].dt.year
    )

    ml_df['month'] = (
        ml_df['date'].dt.month
    )

    ml_df['day'] = (
        ml_df['date'].dt.day
    )

    # Remove datetime
    ml_df.drop(
        columns=['date'],
        inplace=True
    )

    # Remove IDs
    if 'product_id' in ml_df.columns:
        ml_df.drop(
            columns=['product_id'],
            inplace=True
        )

    # Encode categoricals
    cat_cols = (
        ml_df
        .select_dtypes(include='object')
        .columns
    )

    ml_df = pd.get_dummies(
        ml_df,
        columns=cat_cols,
        drop_first=True
    )

    return ml_df