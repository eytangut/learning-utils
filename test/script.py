import os
import google.generativeai as genai

GOOGLE_API_KEY = ''
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])
while True:
    x = input()
    if x != 'quit':
        print(chat.send_message(x).text)
    else:
        break 