from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key = os.getenv("OPEN_API_KEY"))

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [

                {"role":"user", "content":user_input}

                ]
            )

    reply = response.choices[0].message.content
    print(f"Assistant: {reply}")
