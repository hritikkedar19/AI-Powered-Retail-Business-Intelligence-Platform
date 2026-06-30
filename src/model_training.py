import pandas as pd
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / 'models'
MODELS.mkdir(exist_ok=True)
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

def train_sales_model(df):
    daily = df.groupby('order_date').agg(revenue=('revenue','sum'), quantity=('quantity','sum'), profit=('profit','sum')).reset_index()
    daily['order_date'] = pd.to_datetime(daily['order_date'])
    daily['day'] = daily['order_date'].dt.day
    daily['month'] = daily['order_date'].dt.month
    daily['year'] = daily['order_date'].dt.year
    daily['dayofweek'] = daily['order_date'].dt.dayofweek

    X = daily[['quantity','profit','day','month','year','dayofweek']]
    y = daily['revenue']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)
    model = RandomForestRegressor(n_estimators=120, random_state=42)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    metrics = {'MAE': float(mean_absolute_error(y_test, pred)), 'R2': float(r2_score(y_test, pred))}
    joblib.dump(model, MODELS / 'sales_prediction_model.pkl')
    pd.DataFrame([metrics]).to_csv(OUT / 'sales_model_metrics.csv', index=False)
    return metrics

def train_customer_segments(df):
    latest = df['order_date'].max()
    rfm = df.groupby('customer_id').agg(
        recency=('order_date', lambda x: (latest - x.max()).days),
        frequency=('order_id','count'),
        monetary=('revenue','sum')
    ).reset_index()
    scaler = StandardScaler()
    X = scaler.fit_transform(rfm[['recency','frequency','monetary']])
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    rfm['segment'] = kmeans.fit_predict(X)
    labels = {0:'Budget Buyers',1:'Loyal Customers',2:'Premium Customers',3:'At Risk Customers'}
    rfm['segment_name'] = rfm['segment'].map(labels)
    joblib.dump(kmeans, MODELS / 'customer_segmentation_model.pkl')
    joblib.dump(scaler, MODELS / 'rfm_scaler.pkl')
    rfm.to_csv(OUT / 'customer_segments.csv', index=False)
    return rfm

def train_fraud_model(df):
    fraud_data = df[['quantity','revenue','discount_percent','profit_margin']].fillna(0)
    model = IsolationForest(contamination=0.03, random_state=42)
    df['fraud_flag'] = model.fit_predict(fraud_data)
    df['fraud_status'] = df['fraud_flag'].map({1:'Normal', -1:'Suspicious'})
    joblib.dump(model, MODELS / 'fraud_detection_model.pkl')
    df[['order_id','customer_id','revenue','quantity','fraud_status']].to_csv(OUT / 'fraud_alerts.csv', index=False)
    return df
