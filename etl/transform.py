import pandas as pd


def transform_data(df):

    # Clean columns
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Date conversion
    df['date'] = pd.to_datetime(
        df['date']
    )

    # Revenue
    df['revenue'] = (
        df['units_sold']
        * df['price']
    )

    # Stock gap
    df['stock_gap'] = (
        df['inventory_level']
        - df['units_sold']
    )

    # Fill nulls
    num_cols = df.select_dtypes(
        include='number'
    ).columns

    df[num_cols] = (
        df[num_cols]
        .fillna(df[num_cols].median())
    )

    return df