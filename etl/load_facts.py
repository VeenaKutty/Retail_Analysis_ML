import pandas as pd

from config.db_config import get_engine


def load_fact_table(df):

    engine = get_engine()

    # Read dimensions
    region_df = pd.read_sql(
        "SELECT * FROM dim_region",
        con=engine
    )

    category_df = pd.read_sql(
        "SELECT * FROM dim_category",
        con=engine
    )

    date_df = pd.read_sql(
        "SELECT * FROM dim_date",
        con=engine
    )

    # =========================
    # MERGE REGION
    # =========================

    df = df.merge(
        region_df,
        left_on='region',
        right_on='region_name',
        how='left'
    )

    # =========================
    # MERGE DATE
    # =========================

    df = df.merge(
        date_df,
        left_on='date',
        right_on='full_date',
        how='left'
    )

    # =========================
    # FACT TABLE
    # =========================

    fact_sales = df[[
        'product_id',
        'region_id',
        'date_id',
        'inventory_level',
        'units_sold',
        'price',
        'discount',
        'revenue',
        'stock_gap',
        'competitor_pricing'
    ]]

    fact_sales.to_sql(
        'fact_sales',
        con=engine,
        if_exists='replace',
        index=False
    )

    print("Fact Table Loaded")