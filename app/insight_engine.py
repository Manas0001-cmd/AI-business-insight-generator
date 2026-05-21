def build_business_prompt(df):

    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    top_category = (
        df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    low_region = (
        df.groupby("Region")["Profit"]
        .sum()
        .idxmin()
    )

    prompt = f"""
    You are a senior retail business analyst.

    Analyze these business metrics:

    Total Sales: {total_sales}

    Total Profit: {total_profit}

    Best Category:
    {top_category}

    Lowest Profit Region:
    {low_region}

    Generate:
    1. Business insights
    2. Reasons behind performance
    3. Product recommendations
    4. Region improvement strategies
    5. Executive summary

    Keep response concise and professional.
    """

    return prompt
