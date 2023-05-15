import openai
from jproperties import Properties

# Configure the properties file to get the API Key

configs = Properties()
with open('creds.properties', 'rb') as config_file:
    configs.load(config_file)

# Get the API Key from the properties file

openai.api_key = configs.get("api_key").data

print("ChatGPT: Hi, I'm ChatGPT. I'm a helpful assistant")
messages = [
    # system message to set the behavior of the assistant
    {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
]

try:
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat_completion["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
except:
    print("Check if you have set the API key correctly")
    exit()

while True:
    message = input("👤: ")
    # message = input("📄: ")
    if message == "exit":
        break
    if message == "clear":
        print("\033[H\033[J")
        print("ChatGPT: Hi, I'm ChatGPT. I'm a helpful assistant")
        messages = [
            {"role": "system", "content": "Hi ChatGPT, You are a helpful assistant!"},
        ]
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat_completion["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        continue
        
    
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat_completion["choices"][0]["message"]["content"]
    print(f"🤖: {reply}")
    messages.append({"role": "assistant", "content": reply})