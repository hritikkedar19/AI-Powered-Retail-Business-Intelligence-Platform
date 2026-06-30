from src.data_processing import load_and_clean_data
from src.model_training import train_sales_model, train_customer_segments, train_fraud_model
from src.recommendation import build_recommendations
from src.reporting import create_summary_report

print('Loading and cleaning data...')
df, products, customers = load_and_clean_data()

print('Training sales prediction model...')
train_sales_model(df)

print('Training customer segmentation model...')
train_customer_segments(df)

print('Training fraud detection model...')
train_fraud_model(df)

print('Building recommendation table...')
build_recommendations(df, products)

print('Creating summary report...')
create_summary_report(df)

print('Pipeline completed successfully.')
