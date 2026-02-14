import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

def summarize_text(text):
    """
    Sends the text to Mistral 7B to generate a summary.
    """
    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant. Summarize the user's text concisely in 2-3 sentences."
        },
        {
            "role": "user",
            "content": text
        }
    ]

    completion = client.chat.completions.create(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        messages=messages
    )

    return completion.choices[0].message.content


if __name__ == "__main__":
    text_to_summarize = input("Enter text to summarize:\n")
    summary = summarize_text(text_to_summarize)
    print("\nSummary:\n", summary)