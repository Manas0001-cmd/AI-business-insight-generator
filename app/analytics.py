import pandas as pd
import numpy as np

def get_basic_metrics(df):
    """
    Calculates primary business KPIs.
    """
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_sales) * 100 if total_sales > 0 else 0
    total_orders = df["Order ID"].nunique()
    
    return {
        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "profit_margin": round(profit_margin, 2),
        "total_orders": total_orders
    }

def get_category_performance(df):
    """
    Analyzes sales and profit contributions by Product Category.
    """
    category_df = df.groupby("Category").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    ).reset_index()
    
    category_df["Profit_Margin_%"] = (category_df["Total_Profit"] / category_df["Total_Sales"]) * 100
    return category_df.round(2).to_dict(orient="records")

def get_regional_performance(df):
    """
    Identifies high and low performing geographical regions.
    """
    region_df = df.groupby("Region").agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum")
    ).reset_index()
    
    return region_df.round(2).to_dict(orient="records")

def detect_anomalies(df):
    """
    Advanced: Identifies loss-making transactions or high-discount areas
    that are hurting the business bottom-line (Recruiter attraction logic).
    """
    # Finding orders where profit is negative and discount is exceptionally high
    bleeding_products = df[df["Profit"] < 0].sort_values(by="Profit", ascending=True).head(5)
    
    anomalies = []
    for _, row in bleeding_products.iterrows():
        anomalies.append({
            "product_name": row["Product Name"],
            "loss": round(row["Profit"], 2),
            "discount_applied": f"{int(row['Discount'] * 100)}%"
        })
    return anomalies
