# main.py

import asyncio
from home_assistant import HomeAssistant

async def main():
    assistant = HomeAssistant()

    print("🏡 Home Assistant is ready! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = await assistant.call(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    asyncio.run(main())
