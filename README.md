# 🛍️ AI-Powered Retail Business Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)
![SQL](https://img.shields.io/badge/SQL-Analytics-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive **AI-powered Retail Business Intelligence Platform** that enables businesses to analyze sales, understand customer behavior, forecast demand, monitor inventory, detect fraudulent transactions, and generate actionable business insights through an interactive dashboard.

This project demonstrates the complete data analytics lifecycle, including **data generation, preprocessing, machine learning, business intelligence, visualization, and automated reporting**, making it an excellent portfolio project for **Data Analyst, Business Intelligence, Data Scientist, and AI/ML Engineer** roles.

---

# 📖 Table of Contents

* Project Overview
* Key Features
* Technology Stack
* Folder Structure
* Project Workflow
* Machine Learning Models
* Dashboard Modules
* Installation
* Usage
* Sample Insights
* Skills Demonstrated
* Future Enhancements
* License
* Author

---

# 🚀 Project Overview

Retail businesses generate large amounts of transactional and customer data every day. Without proper analysis, valuable business opportunities remain hidden.

This platform transforms raw retail data into meaningful insights by providing:

* Interactive business dashboards
* Automated data cleaning
* Customer segmentation
* Sales forecasting
* Inventory monitoring
* Fraud detection
* Product recommendations
* Exportable reports

The platform enables decision-makers to make informed, data-driven business decisions.

---

# ✨ Key Features

## 📊 Sales Analytics

* Revenue dashboard
* Profit analysis
* Sales trends
* Category performance
* Brand performance
* Customer growth
* Regional sales analysis
* Payment method analysis
* Top-selling products
* Worst-performing products

---

## 🧹 Automated Data Cleaning

* Missing value handling
* Duplicate removal
* Data type correction
* Outlier detection
* Invalid value correction
* Date formatting
* Category normalization

---

## 👥 Customer Analytics

* Customer Lifetime Value (CLV)
* Purchase frequency
* Average spending
* Repeat purchase rate
* Customer retention
* Churn risk analysis

---

## 🎯 Customer Segmentation

Uses **RFM Analysis** and **K-Means Clustering**.

### RFM Metrics

* Recency
* Frequency
* Monetary Value

Customer Segments

* Platinum
* Gold
* Silver
* Bronze
* Loyal Customers
* High Value Customers
* New Customers
* At Risk Customers

---

## 📈 Sales Prediction

Predict future product sales using:

* Random Forest Regressor

Prediction Inputs

* Historical sales
* Product category
* Discount
* Inventory
* Seasonality
* Month
* Previous demand

Outputs

* Future sales
* Revenue forecast

---

## 📦 Inventory Intelligence

Automatically detects:

* Low stock
* Overstock
* Dead stock
* Fast-moving products
* Slow-moving products

Provides intelligent inventory recommendations to reduce stock-outs and excess inventory.

---

## ⭐ Product Recommendation System

Recommends products using customer purchase history.

Supports:

* Popular products
* Similar products
* Frequently bought together
* Personalized recommendations

---

## 🛡 Fraud Detection

Uses **Isolation Forest** to identify suspicious transactions.

Detects:

* Unusual purchases
* Large order anomalies
* Discount abuse
* Suspicious customer activity
* Fraudulent transactions

---

## 📑 Business Insights Engine

Automatically generates business insights such as:

* Best-performing categories
* High-value customers
* Sales trends
* Inventory risks
* Revenue growth
* Customer behavior
* Product performance

---

## 📤 Export Reports

Export reports in multiple formats:

* CSV
* Excel
* PDF

---

# 🛠 Technology Stack

### Programming

* Python
* SQL

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn
* Random Forest
* K-Means
* Isolation Forest

### Visualization

* Plotly
* Matplotlib

### Dashboard

* Streamlit

### Database

* SQLite / MySQL

### Model Persistence

* Joblib

---

# 📂 Folder Structure

```text
AI_Retail_Business_Intelligence_Platform/
│
├── app.py
├── generate_data.py
├── run_pipeline.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│
├── outputs/
│
├── sql/
│
└── src/
```

---

# 🔄 Project Workflow

```text
Generate Retail Data
          │
          ▼
Data Cleaning & Validation
          │
          ▼
Feature Engineering
          │
          ▼
Customer Analytics
          │
          ▼
RFM Analysis
          │
          ▼
Customer Segmentation
          │
          ▼
Sales Prediction
          │
          ▼
Fraud Detection
          │
          ▼
Inventory Intelligence
          │
          ▼
Business Insights
          │
          ▼
Interactive Dashboard
```

---

# 🤖 Machine Learning Models

| Model                   | Purpose               |
| ----------------------- | --------------------- |
| Random Forest Regressor | Sales Prediction      |
| K-Means Clustering      | Customer Segmentation |
| Isolation Forest        | Fraud Detection       |

---

# 📊 Dashboard Modules

### 🏠 Home

Project overview and KPIs.

### 📈 Sales Dashboard

* Revenue
* Profit
* Orders
* Monthly trends
* Category analysis

### 👥 Customer Dashboard

* Customer insights
* RFM analysis
* Segmentation
* CLV

### 📦 Inventory Dashboard

* Stock monitoring
* Inventory alerts
* Reorder recommendations

### 🤖 AI Dashboard

* Sales forecasting
* Fraud detection
* Product recommendations

### 💡 Business Insights

Automatically generated recommendations based on the analyzed data.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI_Retail_Business_Intelligence_Platform.git

cd AI_Retail_Business_Intelligence_Platform
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Usage

Generate sample retail data:

```bash
python generate_data.py
```

Run preprocessing and machine learning pipeline:

```bash
python run_pipeline.py
```

Launch the dashboard:

```bash
python -m streamlit run app.py
```

Open your browser and visit:

```
http://localhost:8501
```

---

# 📈 Example Business Insights

* Electronics generated the highest revenue this month.
* Customer retention increased by 12%.
* Mumbai contributed the highest regional sales.
* Mobile Accessories showed the highest demand.
* Five products require immediate restocking.
* Three transactions were flagged as potential fraud.
* Premium customers contributed more than 45% of total revenue.
* Sales are expected to increase next month based on historical trends.

---

# 💼 Skills Demonstrated

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* SQL Analytics
* Data Visualization
* Dashboard Development
* Customer Segmentation
* Business Intelligence
* Predictive Analytics
* Fraud Detection
* Inventory Optimization
* Recommendation Systems
* Machine Learning
* Model Evaluation
* End-to-End Data Pipeline
* Report Generation

---

# 🔮 Future Enhancements

* Deep Learning sales forecasting (LSTM)
* Real-time streaming dashboard
* Power BI integration
* REST API using FastAPI
* Docker deployment
* Cloud deployment (AWS/Azure/GCP)
* Role-based authentication
* Email alert system
* Automated report scheduling
* Generative AI business assistant
* Voice-enabled analytics
* Multi-store analytics
* Supplier performance dashboard

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Hritik Kedar**

If you found this project helpful, consider giving it a ⭐ on GitHub.

