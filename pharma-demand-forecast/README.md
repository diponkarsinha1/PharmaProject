
# 📊 Pharma Demand Forecasting

This project forecasts weekly demand for pharmaceutical products using historical sales data. Built using **Facebook Prophet**, this pipeline helps reduce stockouts and improve inventory planning across multiple regions.

## 📁 Structure
- `data/pharma_sales.csv` - Synthetic 3-year weekly sales data
- `notebooks/` - Jupyter notebooks for EDA and model building
- `app/streamlit_app.py` - Interactive Streamlit app
- `requirements.txt` - Python dependencies

## 🚀 Features
- Time series forecasting using Prophet
- Region and product-level filtering
- RMSE, MAPE, R² evaluation
- Web interface for real-time forecasting

## 🔧 Setup
```
pip install -r requirements.txt
cd app
streamlit run streamlit_app.py
```

## 📎 Author
Diponkar Sinha  
Prague, Czech Republic
