# Importing Config Parser
import configparser as cfg

# Importing Custom Telegram Module
from telebot import telegram_chatbot

telebot = telegram_chatbot("config.cfg") # Pass Config file 

parser = cfg.ConfigParser() # Instantiate Parser

parser.read("config.cfg")   
token = parser.get('creds', 'tele_token') # Your Bot Token
user_id = parser.get('creds', 'user_id') # Your User ID
update_id = None 

# Run in infinite loop // Get continuous updates
while True:
    updates = telebot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                user_id = str(item["message"]["from"]["id"])
                message = item["message"]
                if 'text' in message:
                    your_text = str(message["text"])
                    # Do something with the text
                    telebot.send_message(reply, user_id)
                elif 'photo' in message:
                    # Do something
                elif 'sticker' in message:
                    # Do something
                elif 'animation' in message:
                    # Do something
                elif 'location' in message:
                    # Do something
                elif "poll" in message:
                    # Do something
                elif "document" in message:
                    # Do something
                elif 'voice' in message:
                    # Do something
                else:
                    print("Message type: Not Coded")
                    print("*"*15+"\nYour Message: " + message + "\n"+"*"*15)                    
            except Exception as e:
                print(e)
                print("\n"+"-"*30)
                print("Message #" + str(item["message"]["message_id"]))
                print(item["message"]["from"]["id"])
                print(item["message"]["from"]["first_name"])
                print(str(item["message"])+"\n")
                print("-"*30+"\n")