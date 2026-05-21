from groq import Groq
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Generate AI Insights
def generate_ai_insights(prompt, model_name="llama-3.3-70b-versatile"):
    """
    Sends the generated business prompt to the Groq API using the selected model
    and returns the AI's analysis.
    """
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=model_name,  # Ab yaha hardcoded string ki jagah variable use hoga
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating insights with {model_name}: {str(e)}"
