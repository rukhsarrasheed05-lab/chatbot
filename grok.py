from groq import Groq

import os
from dotenv import load_dotenv

load_dotenv()


client = Groq(api_key=os.getenv("GROK_KEY"))

# while True:
#     inp = input("You: ")

#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=[{"role": "user", "content": inp}]
#     )

#     print("Bot:", response.choices[0].message.content)


def summarize_text(text):
    """
    Sends a summarization prompt to Groq llama-3.1-8b-instant model
    """
    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant. Summarize the user's text in 2-3 concise sentences."
        },
        {
            "role": "user",
            "content": text
        }
    ]

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    return response.choices[0].message.content


while True:
    user_input = input("Enter text to summarize (or type 'exit' to quit):\n")
    if user_input.lower() in ["exit", "quit"]:
        break

    summary = summarize_text(user_input)
    print("\nSummary:\n", summary)
    print("\n" + "="*50 + "\n")