from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
         {
            "role": "system",
            "content": "You are Jarvis, a helpful AI assistant. Always respond in English unless the user explicitly requests another language."
        },
        {
            "role":"user",
            "content":"Hello Jarvis LLM!"
        }
    ]
)

print("LLM Response:")
print(response.choices[0].message.content)