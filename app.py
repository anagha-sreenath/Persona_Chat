from flask import Flask, render_template, request, jsonify
from personality_responses import get_response
import json
import os
from datetime import datetime

app = Flask(__name__)

# 🧠 In-memory chat history (reset on server restart)
chat_history = []

# 📝 Path to save history (persistent)
HISTORY_FILE = "chat_history.jsonl"

# 👤 Creator Info
CREATOR_INFO = {
    "name": "Anagha Sreenath",
    "linkedin": "https://www.linkedin.com/in/anagha-sreenath",  # change to your actual profile
    "github": "https://github.com/anagha-sreenath",             # change to your actual repo
    "project": "Personality-Based AI Chatbot"
}

@app.route('/')
def home():
    return render_template('index.html')  # make sure index.html exists in templates folder

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    personality = data.get("personality")
    name = data.get("name", "Anonymous")  # Optional: user name

    # 🧠 Generate AI response
    response = get_response(personality, user_input)

    # 🕒 Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 📜 Record the conversation
    entry = {
        "timestamp": timestamp,
        "name": name,
        "personality": personality,
        "user_input": user_input,
        "bot_response": response
    }
    chat_history.append(entry)

    # 💾 Save to file
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(entry) + "\n")

    return jsonify({"response": response})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(chat_history)

@app.route('/about')
def about():
    return jsonify({
        "creator": CREATOR_INFO["name"],
        "linkedin": CREATOR_INFO["linkedin"],
        "github": CREATOR_INFO["github"],
        "project": CREATOR_INFO["project"],
        "message": f"This AI chatbot project was created by {CREATOR_INFO['name']} using Flask and Python. It supports 20 personalities and stores chat history."
    })

if __name__ == '__main__':
    # Runs the server
    app.run(debug=True)
