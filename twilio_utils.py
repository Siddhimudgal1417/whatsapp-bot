from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from gpt_utils import get_bot_response
from lead_storage import store_lead_info

def handle_incoming_message():
    incoming_msg = request.values.get('Body', '').strip()
    sender = request.values.get('From', '')
    
    response_text = get_bot_response(incoming_msg)
    
    store_lead_info(sender, incoming_msg, response_text)
    
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)
