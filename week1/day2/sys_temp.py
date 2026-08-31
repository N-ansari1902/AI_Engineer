import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API key not initialized")

client = Groq(api_key = my_api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt = "I love you!"
message = {
    "role" : role,
    "content" : prompt
}

message_system = {
    "role": "system",
    "content": "You are a stranger passing by on the street of Delhi, India."
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, temperature=2)
#by deafult temperature is 0. range is [0,2]

#print(response)

print("##########################################################################")

answer = response.choices[0].message.content
print(answer)