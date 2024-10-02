# samba_nova.py

import openai
import os

# @title SambaNova
def chat_with_samba_nova(message):
    SAMBANOVA_API_KEY = os.getenv("SAMBA_NOVA_KEY")
    model = "Meta-Llama-3.1-8B-Instruct" # @param ["Meta-Llama-3.1-8B-Instruct","Meta-Llama-3.1-70B-Instruct","Meta-Llama-3.1-405B-Instruct"]
    client = openai.OpenAI(
        api_key = SAMBANOVA_API_KEY,
        base_url = "https://api.sambanova.ai/v1",
    )

    return client.chat.completions.create(
        model = model,
        messages=[
            {"role":"system","content":"我是一個台灣PTT鄉民，講話酸言酸語，但又很熱心"},
            {"role":"user","content":message}
        ],
        temperature =  0.1,
        top_p = 0.1
    )