# 📦 Retail Inventory Optimization & Demand Forecasting System

An end-to-end Data Engineering, Machine Learning, SQL, and Business Intelligence project built using Python, MySQL, and Power BI.

This project focuses on:
- Retail inventory optimization
- Demand forecasting using Machine Learning
- SQL-based ETL pipeline
- Dimensional data modeling
- Interactive Power BI dashboards
- GitHub version control workflow

---

# 🚀 Project Architecture

```text
CSV Dataset
    ↓
Python ETL Pipeline
    ↓
MySQL Data Warehouse
    ↓
Machine Learning Forecasting
    ↓
Prediction Storage
    ↓
Power BI Dashboard
````

---

# 🏗️ Project Structure

```text
retail_inventory_ml/
│
├── config/
│   └── db_config.py
│
├── data/
│   └── retail_store_inventory.csv
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── load_dimensions.py
│   ├── load_facts.py
│   └── utils.py
│
├── models/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── evaluate.py
│
├── pipeline/
│   └── run_pipeline.py
│
├── sql/
│   ├── schema.sql
│   ├── dimension_queries.sql
│   ├── fact_queries.sql
│   └── analysis_queries.sql
│
├── powerbi/
│   ├── dashboard.pbix
│   └── screenshots/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Tech Stack

| Technology   | Purpose             |
| ------------ | ------------------- |
| Python       | ETL & ML            |
| MySQL        | Data Warehouse      |
| Power BI     | Dashboarding        |
| Scikit-Learn | Machine Learning    |
| SQLAlchemy   | Database Connection |
| Git & GitHub | Version Control     |

---

# 📊 Business Problem

Retail businesses often face:

* Overstocking
* Understocking
* Revenue loss
* Poor demand forecasting

This project solves these challenges using:

* ETL pipelines
* Data warehousing
* Predictive analytics
* Interactive BI dashboards

---

# 🧠 Machine Learning

## Model Used

* Random Forest Regressor

## Target Variable

* `units_sold`

## Features

* Inventory level
* Price
* Discount
* Competitor pricing
* Region
* Category
* Seasonality
* Date-based features

## Evaluation Metrics

* MAE (Mean Absolute Error)
* R² Score

---

# 🏛️ Data Warehouse Design

The project uses a **Star Schema** architecture.

## Fact Table

* `fact_sales`

## Dimension Tables

* `dim_region`
* `dim_category`
* `dim_date`

This improves:

* Query performance
* Dashboard efficiency
* Scalability

---

# 🔄 ETL Pipeline

## Extract

* Read CSV data

## Transform

* Data cleaning
* Null handling
* Revenue calculation
* Stock gap calculation
* Date feature engineering

## Load

* Load dimensions
* Load fact table
* Load ML prediction table

---

# 📈 Power BI Dashboard

## Dashboard Pages

### 1. Executive Overview

* Revenue KPIs
* Sales trends
* Region performance
* Category contribution

### 2. Inventory Analysis

* Stock gap analysis
* Inventory health matrix
* Product-level insights

### 3. Supply Chain Risk

* Overstock analysis
* Understock detection
* Operational risk indicators

### 4. AI Forecasting

* Actual vs predicted sales
* Error distribution
* Forecast accuracy
* ML performance insights

---

# 🎨 Dashboard Features

* Dark executive theme
* Interactive slicers
* Dynamic KPIs
* Forecast analytics
* Business-focused storytelling

---

# 🗄️ MySQL Tables

| Table Name            | Description                |
| --------------------- | -------------------------- |
| dim_region            | Region dimension           |
| dim_category          | Product category dimension |
| dim_date              | Date dimension             |
| fact_sales            | Main transactional table   |
| inventory_predictions | ML prediction results      |

---

# 🚀 How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/retail-inventory-ml.git
```

---

## 2️⃣ Open Project

Open the folder in VS Code.

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4️⃣ Activate Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 5️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Configure Database

Update:

```python
config/db_config.py
```

Add your:

* MySQL username
* MySQL password

---

## 7️⃣ Run Pipeline

```bash
python -m pipeline.run_pipeline
```

---

# 📊 Connect Power BI

1. Open Power BI
2. Get Data → MySQL
3. Connect to:

   * Server: `localhost`
   * Database: `retail_db`
4. Load tables
5. Create relationships

---

# 🔗 Power BI Relationships

| From                       | To                   |
| -------------------------- | -------------------- |
| fact_sales.region_id       | dim_region.region_id |
| fact_sales.date_id         | dim_date.date_id     |
| inventory_predictions.date | dim_date.full_date   |

---

# 📷 Dashboard Screenshots

## Executive Overview

(Add screenshot here)

---

## Inventory Analysis

(Add screenshot here)

---

## AI Forecasting Dashboard

(Add screenshot here)

---

# 📌 Key Business Insights

* Forecast accuracy remained consistently high
* Certain regions showed stronger demand patterns
* Inventory risk detected in specific categories
* ML forecasting improved operational visibility

---

# 📚 Skills Demonstrated

* Data Engineering
* SQL & Warehousing
* ETL Development
* Machine Learning
* Data Visualization
* Power BI Development
* Business Analytics
* Git & GitHub

---

# 🚀 Future Improvements

* Real-time streaming pipeline
* Cloud deployment
* Advanced forecasting models
* API integration
* Automated reporting

---

# 👩‍💻 Author

Veena Kutty

---

# ⭐ If you found this project useful, consider giving it a star!

```
```
