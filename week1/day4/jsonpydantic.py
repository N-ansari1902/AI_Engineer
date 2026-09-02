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

#structure it

from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()
response_format = {
    "type" : "json_object"
}

system_prompt = f"""
Extract the information of customer strictly based on this schema format into json.
{schema}
"""

message_system = {
    "role" : "system",
    "content" : system_prompt
}

text = "Hello my name is ABC, i recently purchased one smartphone online from your website. I received it today and it is some other product which is different from my order. my email is abc@xyz.com . Please help me out."
prompt = f"""
This is a customer ticket. Please extract the information from this.
{text}
"""
message = {
    "role" : role,
    "content" : prompt
}

messages = [message_system, message]

response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)

answer = response.choices[0].message.content
print(answer)

#ab jo answer aa raha hai usko developer ka code apne liye kaise padhega? aise:

import json
raw_json = answer
data_file = json.loads(raw_json)
ticket=Ticket(**data_file)
#basically yaha hua kya ki - suppose main hi vo dusra dev hu jiske code ko yeh details read karni hai.
#maine pehle json import kiya and ek raw empty json file create ki and usme LLM ke response(answer) ko load karliya
#ab maine ek data file banayi and uske andar yeh json raw file ko import kar liya using json.loads function.
#then is data file proper structure mein rakhne ke liye jo sabse upar ek ticket class banayi thi uske structure mein rakhne ke liye isko ticket class ki andar as a pointer pass kardiya using double star/asterisk **.

#suppose yeh sab hogya ab mujhe apne side pe isi ko print karna hai, but ab yeh ticket class ke format mein hai so kaise print karunga? aise:

print(ticket.name)
print(ticket.email)
print(ticket.issue)