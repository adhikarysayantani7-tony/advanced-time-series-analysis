"""
Advanced Data Analysis: Time Series Decomposition & Forecasting
Internship Track: Week 4 - Task 4
Author: Sayantani Adhikary
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error


def load_time_series(filepath: str) -> pd.Series:
    """Load monthly sales CSV as a datetime-indexed Series."""
    df = pd.read_csv(filepath, parse_dates=["Date"], index_col="Date")
    df = df.asfreq("MS")
    return df["Sales_USD"]


def run_time_series_analysis(series: pd.Series):
    """Perform moving average smoothing, decomposition, and Holt-Winters forecasting."""
    # 1. Rolling Moving Average (3-month window)
    rolling_3m = series.rolling(window=3).mean()
    print("[INFO] Computed 3-month rolling average.")

    # 2. Seasonal Decomposition (multiplicative model, 12-month period)
    decomposition = seasonal_decompose(series, model="multiplicative", period=12)
    print("[INFO] Completed multiplicative seasonal decomposition (Trend + Seasonal + Residual).")

    # 3. Train/Test Split (last 4 months held out for validation)
    train, test = series.iloc[:-4], series.iloc[-4:]

    # Fit Holt-Winters Exponential Smoothing (trend + seasonal)
    model = ExponentialSmoothing(
        train,
        trend="add",
        seasonal="mul",
        seasonal_periods=12
    ).fit()

    preds = model.forecast(len(test))
    mae = mean_absolute_error(test, preds)
    mape = mean_absolute_percentage_error(test, preds) * 100

    print("\n=== Forecast Validation Metrics (4-Month Holdout) ===")
    print(f"MAE  : ${mae:,.2f}")
    print(f"MAPE : {mape:.2f}%")

    # Refit on full series and forecast next 6 months
    final_model = ExponentialSmoothing(
        series,
        trend="add",
        seasonal="mul",
        seasonal_periods=12
    ).fit()
    future_forecast = final_model.forecast(6)

    print("\n=== 6-Month Future Sales Forecast ===")
    for dt, val in future_forecast.items():
        print(f"{dt.strftime('%Y-%m')}: ${val:,.2f}")

    return decomposition, future_forecast


if __name__ == "__main__":
    sales_series = load_time_series("data/monthly_retail_sales.csv")
    run_time_series_analysis(sales_series)
