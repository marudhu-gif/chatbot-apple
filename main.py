# program config

import google.generativeai as genai

genai.configure(api_key="AIzaSyB3xo2u8-ttocGJApEKbdMitoaihYmB1lY")

apple = genai.GenerativeModel("gemini-2.5-flash")

chat = apple.start_chat(history=[])
print("hi !! i'm your chat-bot")
while True:
    user_input = input("User:")
    if user_input.lower()=="bye!!":
        break
    
    response = chat.send_message(user_input)
    print("Apple : ",response.text)
