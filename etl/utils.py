from config.db_config import get_engine


def load_predictions(results):

    engine = get_engine()

    results.to_sql(
        'inventory_predictions',
        con=engine,
        if_exists='replace',
        index=False
    )

    print("Predictions Loaded")