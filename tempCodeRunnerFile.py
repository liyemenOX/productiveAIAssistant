
import dbm

print("Hello user, i am your assistant, how can i help you?")


DB_FILE = "ai memory"

def save_chat(user_id, history_data):
    with dbm.open(DB_FILE, "c") as db:
        db[user_id] = history_data
        
def load_chat(user_id):
     with dbm.open(DB_FILE,"c") as db:
         if user_id.encode("utf-8") in db:
             return db[user_id].decode("utf-8")
         return ""


existing_name = load_chat("saved_username")
if existing_name:
    print("Welcome back" + existing_name + "i remember you")
    
else:
    user = input("enter you name")
    save_chat("saved_username",user)






