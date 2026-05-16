CREATE DATABASE IF NOT EXISTS retail_db;

USE retail_db;

CREATE TABLE inventory (
    date DATE,
    product_id VARCHAR(50),
    category VARCHAR(50),
    region VARCHAR(50),
    inventory_level INT,
    units_sold INT,
    price FLOAT,
    discount FLOAT,
    weather_condition VARCHAR(50),
    holiday VARCHAR(20),
    seasonality VARCHAR(50),
    competitor_pricing FLOAT,
    revenue FLOAT,
    stock_gap FLOAT
);

CREATE TABLE inventory_predictions (
    actual_units_sold FLOAT,
    predicted_units_sold FLOAT,
    row_error FLOAT
);