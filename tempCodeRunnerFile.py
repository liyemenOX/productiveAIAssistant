print("Hello user, i am your assistant, how can i help you?")

user = input("enter basic details about yourself:\n")
print("thankyou for sharing your deatils here \n " + user + "\n i will use this information to assist you better\n")

length = len(user)
if(length > 10):
    print("hey user your name is too lengthy\n")
elif(length < 5):
    print("huh !! your name is too short buddy\n")
else:
    print("hey! user your name is of satisfactory length\n")