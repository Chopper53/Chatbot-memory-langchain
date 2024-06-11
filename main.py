from dotenv import load_dotenv
import os

from langchain_google_genai import GoogleGenerativeAI
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

def main():
    load_dotenv()
    
    chat = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.3)

    messages = [
        SystemMessage(content="You are a helpful assistant"),
    ]

    print("Hello, I am Gemini Cli")

    while True:
        user_input = input("> ")

        messages.append(HumanMessage(content=user_input))

        prompt = "\n".join([msg.content for msg in messages])

        ai_response = chat(prompt)

        messages.append(AIMessage(content=ai_response))

        print("\nAssistant:\n", ai_response)

        print("history:", messages)


if __name__ == '__main__':
    main()