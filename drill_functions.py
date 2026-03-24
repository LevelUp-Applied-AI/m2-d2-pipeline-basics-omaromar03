import pandas as pd


def clean_column(series):
    """Fill NaN values with the series median. Returns the cleaned Series."""
    median_value = series.median()
    return series.fillna(median_value)


def compute_revenue(quantity, price):
    """Multiply quantity and price element-wise. Returns a revenue Series."""
    return quantity * price