from dotenv import load_dotenv
import os

from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

def main():
    load_dotenv()
    
    llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.3)

    conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(), verbose=True
        )

    print("Hello, I am Gemini Cli")

    while True:
        user_input = input("> ")

        ai_response = conversation.predict(input=user_input)

        print("\nAssistant:\n", ai_response)



if __name__ == '__main__':
    main()