from sqlalchemy import create_engine, text
from urllib.parse import quote_plus


def get_engine():

    username = "root"
    password = quote_plus("root")
    host = "localhost"

    # Create DB
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/"
    )

    with engine.connect() as conn:
        conn.execute(
            text(
                "CREATE DATABASE IF NOT EXISTS retail_db"
            )
        )

    # Connect DB
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/retail_db"
    )

    return engine