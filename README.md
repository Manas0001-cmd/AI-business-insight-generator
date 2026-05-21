# AI Business Insight Generator

An AI-powered retail analytics dashboard that generates automated business insights using Generative AI, Streamlit, and retail sales data.

---

# Features

- KPI Dashboard
- Sales Trend Analysis
- Profit Analysis
- Top Product Insights
- AI Business Recommendations
- Groq AI Integration
- Interactive Charts
- Retail Analytics

---

# Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## Libraries
- Pandas
- Plotly
- NumPy
- Scikit-Learn
- Groq Generative AI

---

# Project Structure

AI_Business_Insight_Generator/
│
├── data/
│   └── SampleSuperstore.csv
│
├── app/
│   ├── dashboard.py
│   ├── insight_engine.py
│   ├── llm_handler.py
│   ├── analytics.py
│   └── utils.py
│
├── notebooks/
│
├── models/
│
├── screenshots/
│
├── requirements.txt
│
├── .env
│
└── README.md

---

# STEP 1 — Clone or Download Project

Download the project folder and open it in VS Code.

---

# STEP 2 — Create Virtual Environment

Open terminal inside project folder.

Run:

```bash
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

pip install pandas numpy streamlit plotly scikit-learn google-generativeai python-dotenv

streamlit run app/dashboard.py
