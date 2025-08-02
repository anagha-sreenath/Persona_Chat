import os
from dotenv import load_dotenv
import google.generativeai as genai
from personalities import personality_prompts

# Load your API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(user_input, personality_style):
    try:
        # Get the personality's prompt
        personality_prompt = personality_prompts.get(
            personality_style,
            "You are a helpful assistant."
        )

        # Combine personality prompt and user message
        full_prompt = f"{personality_prompt}\n\nUser: {user_input}"

        # Use Gemini 1.5 Flash — free tier model
        model = genai.GenerativeModel("models/gemini-1.5-flash")

        # Generate a response
        response = model.generate_content(full_prompt)

        return response.text.strip()

    except Exception as e:
        return f"⚠️ Oops! Something went wrong: {e}"

# Run the chatbot
if __name__ == "__main__":
    print("👋 Welcome to the Personality Chat App!")
    print("Available Personalities:")
    for style in personality_prompts:
        print(f" - {style}")

    selected = input("\nChoose a personality: ").strip().lower()

    if selected not in personality_prompts:
        print("⚠️ Invalid personality selected. Exiting.")
        exit()

    print(f"\n💬 Chatting in '{selected}' mode! Type 'exit' to quit.\n")

    while True:
        msg = input("You: ")
        if msg.lower() in ["exit", "quit"]:
            print("Bot: See ya! 💻👋")
            break
        reply = ask_gemini(msg, selected)
        print(f"Bot ({selected}): {reply}\n")
