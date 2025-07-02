# Multi-Personality AI Chatbot (with GPT-3.5)

This Python-based chatbot simulates natural conversations with different personalities using OpenAI's GPT-3.5 model. The bot offers three modes: Business Assistant, Fun Chatbot, and Technical Helper — making it versatile for professional, casual, or technical discussions.

---

## ⚡ Features
✅ Choose from 3 personalities: Business Bot, Fun Bot, or Tech Assistant  
✅ Multi-turn memory — remembers the full conversation context  
✅ AI-generated responses powered by GPT-3.5  
✅ Automatically saves chat logs with timestamps  
✅ Simple to use, no advanced setup required  

---

## 🛠️ Requirements
- Python 3.x  
- `requests` library  
- OpenAI API key stored in a `config.py` file as:  
  ```python
  api_key = "YOUR_OPENAI_API_KEY"
🚀 How to Use
Paste your OPENAI key in .env file.

Run the chatbot:

bash
Copy
Edit
python Chatbot.py
Choose a bot personality:

1 → Business Bot

2 → Fun Bot

3 → Tech Assistant

Start chatting! Type exit or quit to end the session

Chat logs are saved automatically in the chat_logs folder

🤖 Example Output
text
Copy
Edit
🤖 Welcome to GPT-Powered Chatbot

Select Bot Personality:

1 - Business Bot
2 - Fun Bot
3 - Tech Assistant

Enter option number (1/2/3): 1

✅ Business Bot activated. Type 'exit' to quit.

You: Tell me about market trends
Bot: Current market trends indicate increased demand for AI-driven automation...

You: exit

👋 Chatbot session ended. Conversation saved.
📝 Full conversation saved to 'chat_logs/Chat_Business_Bot_20250702_153522.txt'
💡 AI Integration
Model: GPT-3.5-Turbo

Multi-turn chat with memory of previous messages

Personality-based role setting for tailored responses

💼 Ideal Use Cases
✔ AI Chatbots for businesses or websites
✔ Fun conversational bots for entertainment
✔ Technical assistant for basic coding help
✔ Learning AI chat applications in Python
