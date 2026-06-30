import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)
ROOT = Path(__file__).parent
RAW = ROOT / 'data' / 'raw'
RAW.mkdir(parents=True, exist_ok=True)

cities = ['Mumbai', 'Pune', 'Delhi', 'Bengaluru', 'Hyderabad', 'Chennai', 'Kolkata', 'Ahmedabad']
categories = {
    'Electronics': ['Laptop', 'Mouse', 'Keyboard', 'Headphones', 'Smartphone'],
    'Fashion': ['Shoes', 'T-Shirt', 'Jeans', 'Jacket', 'Watch'],
    'Home': ['Chair', 'Table', 'Bedsheet', 'Lamp', 'Cookware'],
    'Grocery': ['Rice', 'Oil', 'Tea', 'Snacks', 'Sugar']
}

products = []
pid = 1001
for cat, names in categories.items():
    for name in names:
        price = np.random.randint(100, 75000) if cat == 'Electronics' else np.random.randint(80, 8000)
        cost = int(price * np.random.uniform(0.55, 0.82))
        stock = np.random.randint(30, 500)
        products.append([pid, name, cat, price, cost, stock])
        pid += 1
products_df = pd.DataFrame(products, columns=['product_id','product_name','category','price','cost','stock'])
products_df.to_csv(RAW / 'products.csv', index=False)

customers = []
for cid in range(1, 801):
    customers.append([cid, f'Customer_{cid}', np.random.choice(cities), np.random.randint(18, 65), np.random.choice(['Male','Female','Other'])])
customers_df = pd.DataFrame(customers, columns=['customer_id','customer_name','city','age','gender'])
customers_df.to_csv(RAW / 'customers.csv', index=False)

orders = []
payments = []
start = pd.Timestamp('2024-01-01')
for oid in range(1, 6001):
    c = customers_df.sample(1).iloc[0]
    p = products_df.sample(1).iloc[0]
    qty = np.random.randint(1, 5)
    date = start + pd.Timedelta(days=int(np.random.randint(0, 730)))
    discount = np.random.choice([0, 5, 10, 15, 20], p=[0.45, 0.2, 0.2, 0.1, 0.05])
    revenue = qty * p['price'] * (1 - discount/100)
    profit = revenue - qty * p['cost']
    orders.append([oid, c.customer_id, p.product_id, date.date(), qty, discount, round(revenue,2), round(profit,2), c.city])
    status = np.random.choice(['Success','Failed','Refunded'], p=[0.9,0.06,0.04])
    method = np.random.choice(['UPI','Credit Card','Debit Card','Net Banking','COD'])
    payments.append([oid, method, status])

orders_df = pd.DataFrame(orders, columns=['order_id','customer_id','product_id','order_date','quantity','discount_percent','revenue','profit','city'])
# create a few suspicious transactions
for i in range(20):
    idx = np.random.randint(0, len(orders_df))
    orders_df.loc[idx, 'quantity'] = np.random.randint(15, 50)
    orders_df.loc[idx, 'revenue'] *= np.random.randint(5, 12)
orders_df.to_csv(RAW / 'orders.csv', index=False)
pd.DataFrame(payments, columns=['order_id','payment_method','payment_status']).to_csv(RAW / 'payments.csv', index=False)
print('Sample retail data created in data/raw')
