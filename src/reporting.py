from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

def create_summary_report(df):
    report = {
        'Total Revenue': df['revenue'].sum(),
        'Total Profit': df['profit'].sum(),
        'Total Orders': df['order_id'].nunique(),
        'Total Customers': df['customer_id'].nunique(),
        'Average Order Value': df['revenue'].sum() / df['order_id'].nunique(),
        'Best City': df.groupby('city')['revenue'].sum().idxmax(),
        'Best Category': df.groupby('category')['revenue'].sum().idxmax(),
        'Best Product': df.groupby('product_name')['revenue'].sum().idxmax()
    }
    pd.DataFrame(report.items(), columns=['Metric','Value']).to_csv(OUT / 'business_summary.csv', index=False)
    return report
