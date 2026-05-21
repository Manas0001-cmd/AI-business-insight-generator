from groq import Groq
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Generate AI Insights
def generate_ai_insights(prompt):

    try:

        response = client.chat.completions.create(

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            model="llama-3.3-70b-versatile"

        )

        return response.choices[0].message.content

    except Exception as e:

        return f"Error generating AI insights: {str(e)}"