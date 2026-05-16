from config.db_config import get_engine
import pandas as pd

def load_dimensions(df):

    engine = get_engine()

    # =========================
    # REGION DIMENSION
    # =========================

    dim_region = (
        df[['region']]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_region.columns = ['region_name']

    dim_region.to_sql(
        'dim_region',
        con=engine,
        if_exists='replace',
        index_label='region_id'
    )

    # =========================
    # CATEGORY DIMENSION
    # =========================

    dim_category = (
        df[['category']]
        .drop_duplicates()
        .reset_index(drop=True)
    )

    dim_category.columns = ['category_name']

    dim_category.to_sql(
        'dim_category',
        con=engine,
        if_exists='replace',
        index_label='category_id'
    )

    # =========================
    # DATE DIMENSION
    # =========================

    dim_date = pd.DataFrame()

    dim_date['full_date'] = (
        df['date'].drop_duplicates()
    )

    dim_date['year'] = (
        dim_date['full_date'].dt.year
    )

    dim_date['month'] = (
        dim_date['full_date'].dt.month
    )

    dim_date['day'] = (
        dim_date['full_date'].dt.day
    )

    dim_date['day_of_week'] = (
        dim_date['full_date'].dt.dayofweek
    )

    dim_date.to_sql(
        'dim_date',
        con=engine,
        if_exists='replace',
        index_label='date_id'
    )

    print("Dimensions Loaded")