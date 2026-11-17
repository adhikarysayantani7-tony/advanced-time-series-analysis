# Advanced Data Analysis: Time Series Decomposition & Forecasting

## Project Overview
This repository applies **Time Series Analysis & Forecasting**—combining rolling moving averages, multiplicative seasonal decomposition, and Holt-Winters Exponential Smoothing—to 24 months of retail sales data.

## Repository Structure
- `README.md`: Project overview and setup instructions
- `requirements.txt`: Required Python dependencies (`statsmodels`, `pandas`, `scikit-learn`)
- `data/monthly_retail_sales.csv`: 24-month historical retail sales dataset
- `src/time_series_analysis.py`: Modular Python script executing decomposition and 6-month forecasting
- `notebooks/time_series_analysis.ipynb`: Interactive Jupyter Notebook with decomposition and forecast plots
- `docs/time_series_report.md`: Project report explaining the technique, components, and business application

## How to Run
1. Clone the repository:
   `git clone https://github.com/adhikarysayantani7-tony/advanced-time-series-analysis.git`
2. Install dependencies:
   `pip install -r requirements.txt`
3. Run the forecasting script:
   `python src/time_series_analysis.py`
