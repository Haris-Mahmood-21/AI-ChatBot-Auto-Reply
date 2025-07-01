🤖 AI Chatbot Auto Replay

A Python-based desktop automation chatbot that reads the latest message from the screen, sends it to OpenAI's GPT model, and pastes the generated reply back into the chat. Built using pyautogui, pyperclip, and OpenAI, this project mimics a real-time AI auto-responder, acting as a bilingual assistant.

📌 Features
1. Automatically detects the latest message from a chat (via screen selection) like WhatsApp chat

2. Sends only new messages to OpenAI for a reply

3. Responds in Urdu or English based on the user’s message

4. Simulates human-like typing using pyautogui

5. Press q anytime to exit the chatbot safely

🛠️ Technologies Used

Python 3.x

OpenAI Python SDK

PyAutoGUI

Pyperclip

Keyboard

🚀 Setup Instructions

1. Clone the Repository
git clone https://github.com/yourusername/ai-chatbot.git

2. Install Dependencies
pip install openai pyautogui pyperclip keyboard

3. Configure Your API Key
Open the Python file and replace the placeholder with your actual OpenAI API key:

client = OpenAI(api_key="your-api-key-here")

▶️ How to Run

First Open a chat e.g WhatsApp Web and log in.

Run the Python script:

The script will:

Click on your browser icon.

Select the WhatsApp chat region.

Copy the chat, read the latest message, and respond via OpenAI.

Press q at any time to quit.

📌 Notes
Make sure your screen resolution and chat window positions match the coordinates used in the script. You may need to adjust:

pyautogui.moveTo(x, y)
pyautogui.click(x, y)
This script simulates mouse and keyboard actions, so avoid interfering with the mouse while it runs.

📄 License
This project is for educational and personal use only. Use it responsibly and within the terms of OpenAI and WhatsApp.

🙌 Credits

Developed by Muhammad Haris
