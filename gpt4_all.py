from gpt4all import GPT4All

bot = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

while True:
    query = input("You: ")
    print("Bot:", bot.generate(query))