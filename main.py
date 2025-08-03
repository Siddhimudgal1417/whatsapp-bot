from flask import Flask, request
from twilio_utils import handle_incoming_message

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp():
    print("✅ Received a message from Twilio Sandbox!")
    print("📨 Incoming data:", request.form)  
    return handle_incoming_message()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
