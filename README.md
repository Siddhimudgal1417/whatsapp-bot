# 🤖 WhatsApp AI Assistant Bot

A Python Flask-based WhatsApp bot that integrates **OpenAI GPT** and **Twilio** to provide intelligent chat responses and Google Drive file interactions — directly over WhatsApp.

---

## What It Does

- Responds intelligently to WhatsApp messages using GPT
- Accepts Google Drive file links and returns AI-generated summaries
- Stores and manages conversation leads
- Modular architecture — each component (GPT, Twilio, Drive) is separated for easy extension
- Secured with `.env` for all API key management

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask (Python) |
| AI Engine | OpenAI GPT API |
| Messaging | Twilio WhatsApp API |
| File Access | Google Drive API |
| Config | Dotenv |

---

## Project Structure

```
whatsapp-bot/
├── main.py              # Flask app entry point + webhook handler
├── gpt_utils.py         # GPT message handling and response logic
├── twilio_utils.py      # Twilio message parsing and sending
├── lead_storage.py      # Lead/conversation storage logic
├── requirements.txt
└── .env                 # API keys (local only, excluded from git)
```

---

## Setup & Run

```bash
git clone https://github.com/Siddhimudgal1417/whatsapp-bot.git
cd whatsapp-bot

pip install -r requirements.txt

# Add to .env:
# OPENAI_API_KEY=your_key
# TWILIO_ACCOUNT_SID=your_sid
# TWILIO_AUTH_TOKEN=your_token
# TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886

flask run
# Use ngrok to expose localhost for Twilio webhook
ngrok http 5000
```

---

## Key Features

- 💬 GPT-powered intelligent WhatsApp responses
- 📁 Google Drive file summarization via link
- 🗃️ Lead storage for conversation tracking
- 🔐 Secure API key management via environment variables
- ⚡ Modular structure — easy to add new capabilities

---

## Skills Demonstrated

`Python` `Flask` `OpenAI API` `Twilio API` `Google Drive API` `REST API` `Webhook Integration` `Ngrok`

---

**Author:** Siddhi Mudgal · [LinkedIn](https://linkedin.com/in/https://www.linkedin.com/in/siddhi-mudgal/) · [GitHub](https://github.com/Siddhimudgal1417)
