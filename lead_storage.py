import csv
import os

def store_lead_info(sender, user_input, bot_reply):
    # basic heuristic: if user_input contains "interested", assume it's a lead
    if "interested" in user_input.lower():
        with open("leads.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sender, user_input, bot_reply])
