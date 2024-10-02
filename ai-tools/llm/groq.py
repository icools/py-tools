# groq.py
from groq import Groq
import os
from enum import Enum

class GroqModel(Enum):
    GEMMA2_9B_IT = "gemma2-9b-it"
    MIXTRAL_8X7B_32768 = "mixtral-8x7b-32768"
    LLAMA_3_1_70B_VERSATILE = "llama-3.1-70b-versatile"

class GroqApi:
    def __init__(self):
        self.api_key = os.getenv("GROQ_KEY")
        self.client = Groq(api_key=self.api_key)

    def call_gemma(self, question,model: GroqModel = GroqModel.GEMMA2_9B_IT):
        print("groq gemma2 thinking...")
        
        completion = self.client.chat.completions.create(
            model="gemma2-9b-it",
            messages=[{"role": "user", "content": question}],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion #.choices[0].message.content.strip()