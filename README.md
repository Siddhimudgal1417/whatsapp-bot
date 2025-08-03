# 🤖 WhatsApp AI Assistant Bot

A Python Flask-based WhatsApp bot that uses **Twilio** and **OpenAI** to chat intelligently and interact with files from Google Drive.

---

## ✅ Features

- Chat with GPT on WhatsApp
- Upload Google Drive files and get summaries
- Easy modular structure
- Secure setup using `.env` for API keys

---

## 🗂 Project Structure

whatsapp-bot/
├── main.py # Flask app entry point
├── gpt.py # GPT message handling
├── whatsapp_utils.py # Twilio message parsing and responses
├── drive_utils.py # File fetching from Google Drive
├── summarizer.py # Summarize document contents
├── sheet_logger.py # Optional: Log user chats to Google Sheets
├── requirements.txt # Required Python libraries
├── .env # Environment variables (DO NOT SHARE)
└── README.md
