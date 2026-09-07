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

def prompt_engineering(prompt):

    role = "user"
    message = {
        "role" : role,
        "content" : prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages)
    answer = response.choices[0].message.content

    print(answer)


given_prompt = """
#ROLE
You are an customer support assistant at a mobiles and laptops computers companys.
#TASK
You have to categorise the customer's given complaint.
#BOUNDARY
strictly categorise in categories namely : Technical issue, Returns, Quality/Experience issue.
#OUTPUT FORMAT
Answer in strictly one word only.
#EXAMPLE
If the customer's complaint consists about refund, it goes under Returns.
#FALLBACK
If the customer's complaint does not fall under any of the given categories, mark it as OTHER.


My laptop is not turning on. Please help!
"""

prompt_engineering(given_prompt)