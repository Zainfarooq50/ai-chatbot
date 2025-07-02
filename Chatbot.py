import requests
import os
from datetime import datetime
from config import api_key


# --------------- Role Selection ---------------
roles = {
    "1": ("Business Bot", "You are a professional assistant providing clear, concise business information."),
    "2": ("Fun Bot", "You are a humorous, friendly chatbot that loves jokes and light conversation."),
    "3": ("Tech Assistant", "You are a technical assistant providing coding help and technical explanations.")
}

print("\n🤖 Welcome to GPT-Powered Chatbot\n")
print("Select Bot Personality:\n")
print("1 - Business Bot")
print("2 - Fun Bot")
print("3 - Tech Assistant")

role_choice = input("\nEnter option number (1/2/3): ").strip()

if role_choice not in roles:
    print("⚠️ Invalid choice. Defaulting to 'Business Bot'.\n")
    role_name, system_prompt = roles["1"]
else:
    role_name, system_prompt = roles[role_choice]

print(f"\n✅ {role_name} activated. Type 'exit' to quit.\n")

# --------------- API Setup ---------------
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# --------------- Multi-Turn Memory ---------------
conversation_history = [{"role": "system", "content": system_prompt}]
log_lines = [f"--- {role_name} Chat Session ---\n"]

# --------------- Chat Loop ---------------
while True:
    user_input = input("You: ").strip()

    if not user_input:
        print("⚠️ Please enter a message.")
        continue

    if user_input.lower() in ["exit", "quit"]:
        print("👋 Chatbot session ended. Conversation saved.")
        break

    conversation_history.append({"role": "user", "content": user_input})

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": conversation_history,
        "max_tokens": 200
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()
        bot_reply = result["choices"][0]["message"]["content"].strip()

        print(f"Bot: {bot_reply}\n")
        conversation_history.append({"role": "assistant", "content": bot_reply})

        log_lines.append(f"You: {user_input}\n")
        log_lines.append(f"Bot: {bot_reply}\n")

    except Exception as e:
        print(f"❌ Error: {e}\n")


# --------------- Save Conversation ---------------
os.makedirs("chat_logs", exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = f"chat_logs/Chat_{role_name.replace(' ', '_')}_{timestamp}.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.writelines("\n".join(log_lines))

print(f"\n📝 Full conversation saved to '{log_file}'")
