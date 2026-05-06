# 🤖 WhatsApp AI Assistant Bot

A Python-based WhatsApp automation bot that integrates **OpenAI GPT**, **Twilio**, and **Google Drive** to create an intelligent assistant that responds to messages, summarizes documents, and logs interactions — all over WhatsApp.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat&logo=flask)
![Twilio](https://img.shields.io/badge/Twilio-WhatsApp_API-red?style=flat&logo=twilio)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5/4-green?style=flat&logo=openai)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat)

---

## 🚀 What It Does

This bot turns WhatsApp into a smart AI assistant. Users can send messages, share Google Drive file links, and get instant AI-powered responses — no app installation required on their end.

**Built for:** Small businesses, startups, and teams that want to automate WhatsApp customer interactions without building a full mobile app.

---

## ✅ Features

- **AI Chat** — Responds to any WhatsApp message using OpenAI GPT
- **Google Drive Integration** — Users send a Drive link, bot fetches and summarizes the document
- **Lead Storage** — Captures and stores user interactions for follow-up
- **Webhook-based** — Runs via Flask + Twilio webhook, deployable on any server
- **Modular Codebase** — Clean separation of GPT, Twilio, and Drive logic for easy extension
- **Secure Config** — All API keys managed via `.env`, never hardcoded

---

## 🗂 Project Structure

```
whatsapp-bot/
├── main.py             # Flask app entry point, webhook handler
├── gpt_utils.py        # OpenAI GPT message generation
├── twilio_utils.py     # Twilio WhatsApp message parsing & sending
├── lead_storage.py     # Stores user leads/interactions locally
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── README.md
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI | OpenAI GPT API |
| Messaging | Twilio WhatsApp API |
| Storage | Google Drive API |
| Deployment | ngrok (local), Railway/Render (production) |

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Siddhimudgal1417/whatsapp-bot.git
cd whatsapp-bot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
```bash
cp .env.example .env
```

Fill in your `.env`:
```
OPENAI_API_KEY=your_openai_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
```

### 4. Run the Flask server
```bash
python main.py
```

### 5. Expose via ngrok (for local testing)
```bash
ngrok http 5000
```
Set the ngrok URL as your Twilio webhook URL in the Twilio console.

---

## 📡 How It Works

```
User sends WhatsApp message
        ↓
Twilio receives it → sends POST to Flask webhook
        ↓
Flask routes to GPT or Drive handler
        ↓
Response generated → sent back via Twilio
        ↓
Interaction logged in lead_storage
```

---

## 📦 Requirements

```
flask
twilio
openai
python-dotenv
requests
```

---

## 🔮 Planned Features

- [ ] Multi-language support
- [ ] PostgreSQL lead storage (replacing local storage)
- [ ] Admin dashboard for viewing leads
- [ ] Scheduled message broadcasting

---

## 👩‍💻 Author

**Siddhi Mudgal** — Python Backend Developer  
🌐 [Portfolio](https://siddhi-mudgal.netlify.app) | 💼 [LinkedIn](https://www.linkedin.com/in/siddhi-mudgal/) | 🐙 [GitHub](https://github.com/Siddhimudgal1417)

---

## 📄 License

MIT License — free to use and modify.
