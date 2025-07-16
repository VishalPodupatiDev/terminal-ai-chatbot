import os
from openai import OpenAI
from prompts import get_prompt_template
from config import OPENAI_API_KEY, MODEL_NAME

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_question(question):
    prompt = get_prompt_template().format(question=question)
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant for data engineers."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("🤖 AI Chatbot: Ask your data engineering questions (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        answer = ask_question(user_input)
        print(f"Bot: {answer}\n")
