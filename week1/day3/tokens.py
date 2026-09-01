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

#3 prompts
prompt1 = "Explain what is an Apple?"
prompt2 = "Write an essay on AI engineering for freshers and interns in about 1000 words."
prompt3 = "Why are the prices of SSDs and RAMs going so high?"

prompts = [prompt1, prompt2, prompt3]

for prompt in prompts:
    message = {
        "role" : role,
        "content" : prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model, messages=messages, max_tokens=1000) #yaha pe jo max tokens ka limit hai yeh sirf completion wale pe applicable hota hai na ki prompt wale pe.
    usage = response.usage

    print(f"Prompt: {prompt} ; Prompt token usage: {usage.prompt_tokens} ; completion token usage: {usage.completion_tokens} ; total tokens used: {usage.prompt_tokens + usage.completion_tokens} ; Finish reason: {response.choices[0].finish_reason}")
    #finish reason mein "stop" means : khud ba khud end hogya within the limit rokna limit karna nhi pada. "length" means: completion wala response limit se bahar ja rha tha so rokna limit karna pada.