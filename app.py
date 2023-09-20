from filldb import reaction_message, emojis
from database.db_config import db, app


#Hur gör jag för om man vill reagera med flera olika emojis på samma meddelande?
def add_reaction_to_message(message_id, emoji):
    for message in reaction_message:
        if message["message_id"] == message_id:
            if message["emoji"] == "":
                message["emoji"] = emoji
                message["count"] = 1
            elif message["emoji"] == emoji:
                message["count"] += 1
            else:
                print("This message already has a different emoji!")
            return
        print("Message ID not found!")
        
