import streamlit as st
import pandas as pd
import plotly.express as px
from insight_engine import build_business_prompt
from llm_handler import generate_ai_insights

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(page_title="AI Business Insight Generator", layout="wide")
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 AI Business Insight Generator")
st.markdown("AI-powered retail analytics dashboard")

# ---------------------------------------------------
# SIDEBAR CONFIGURATION (Yaha daalna hai Step 1)
# ---------------------------------------------------
st.sidebar.header("🤖 AI Settings")

# Dropdown menu for selecting Groq models
model_choice = st.sidebar.selectbox(
    "Choose AI Model:",
    options=["llama-3.3-70b-versatile", "llama3-8b-8192", "mixtral-8x7b-32768"],
    index=0  # Default selection
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("data/SampleSuperstore.csv", encoding="latin1")
    return df

df = load_data()

# ---------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("🛒 Total Orders", total_orders)
col4.metric("👥 Customers", total_customers)

st.divider()

# ---------------------------------------------------
# SALES BY CATEGORY
# ---------------------------------------------------

st.subheader("Sales by Category")

sales_category = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    sales_category,
    x="Category",
    y="Sales",
    text_auto=True,
    title="Category-wise Sales"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------------------------------------------
# PROFIT BY REGION
# ---------------------------------------------------

st.subheader("Profit by Region")

profit_region = (
    df.groupby("Region")["Profit"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    profit_region,
    names="Region",
    values="Profit",
    title="Regional Profit Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------
# MONTHLY SALES TREND
# ---------------------------------------------------

st.subheader("Monthly Sales Trend")

df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
    .reset_index()
)

fig3 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------------------------------------------------
# TOP PRODUCTS
# ---------------------------------------------------

st.subheader("Top 10 Products")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig4 = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top Selling Products"
)

st.plotly_chart(fig4, use_container_width=True)

# ---------------------------------------------------
# DATA PREVIEW
# ---------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(df.head())
# AI SECTION

st.divider()

st.subheader("🤖 AI Business Insights")

if st.button("Generate AI Insights"):

    with st.spinner("Analyzing business data..."):

        prompt = build_business_prompt(df)

        insights = generate_ai_insights(prompt)

        st.success("AI Analysis Complete!")

        st.write(insights)
