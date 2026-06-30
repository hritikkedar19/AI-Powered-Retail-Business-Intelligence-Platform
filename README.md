# AI-Powered Retail Business Intelligence Platform

A resume-ready end-to-end Data Analytics + Machine Learning project for retail business decision-making.

## Features

- Sales analytics dashboard
- Data cleaning pipeline
- Customer segmentation using RFM and K-Means
- Sales prediction using Random Forest
- Inventory risk alerts
- Product recommendation system
- Fraud/anomaly detection using Isolation Forest
- Exportable business insights

## Tech Stack

Python, Pandas, NumPy, Scikit-learn, Plotly, Streamlit, SQL, Joblib

## Folder Structure

```text
AI_Retail_Business_Intelligence_Platform/
├── app.py
├── generate_data.py
├── run_pipeline.py
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── outputs/
├── sql/
└── src/
```

## How to Run

```bash
pip install -r requirements.txt
python generate_data.py
python run_pipeline.py
python -m streamlit run app.py
```


## Business Use Case

This project helps a retail company understand revenue trends, identify best-selling products, segment customers, forecast sales, detect suspicious orders and manage inventory.
