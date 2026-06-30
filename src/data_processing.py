import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
PROCESSED = ROOT / 'data' / 'processed'
PROCESSED.mkdir(parents=True, exist_ok=True)

def load_and_clean_data():
    orders = pd.read_csv(RAW / 'orders.csv')
    products = pd.read_csv(RAW / 'products.csv')
    customers = pd.read_csv(RAW / 'customers.csv')
    payments = pd.read_csv(RAW / 'payments.csv')

    orders = orders.drop_duplicates()
    orders['order_date'] = pd.to_datetime(orders['order_date'], errors='coerce')
    orders = orders.dropna(subset=['order_date','customer_id','product_id'])
    orders['quantity'] = orders['quantity'].clip(lower=1)
    orders['discount_percent'] = orders['discount_percent'].fillna(0).clip(0, 80)

    df = orders.merge(products, on='product_id', how='left')
    df = df.merge(customers, on='customer_id', how='left', suffixes=('', '_customer'))
    df = df.merge(payments, on='order_id', how='left')

    df['month'] = df['order_date'].dt.to_period('M').astype(str)
    df['year'] = df['order_date'].dt.year
    df['dayofweek'] = df['order_date'].dt.dayofweek
    df['avg_order_value'] = df['revenue'] / df['quantity']
    df['profit_margin'] = (df['profit'] / df['revenue']).replace([float('inf'), -float('inf')], 0).fillna(0)

    df.to_csv(PROCESSED / 'retail_cleaned.csv', index=False)
    return df, products, customers
