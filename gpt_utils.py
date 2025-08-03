import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_bot_response(user_message):
    system_prompt = """
    You are a helpful assistant working for ADmyBRAND. 
    You help users discover products and services offered, and collect their name, email, and interest if they are interested.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, temperature=0.7
    )

    return response['choices'][0]['message']['content']
