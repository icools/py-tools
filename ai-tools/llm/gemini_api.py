# gemini_api.py
import os
from enum import Enum
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from dataclasses import dataclass

class GeminiModel(Enum):
    GEMINI_1_5_FLASH_EXP_0827 = "gemini-1.5-flash-exp-0827"
    GEMINI_1_5_FLASH = "gemini-1.5"
    GEMINI_1_5_PRO = "gemini-1.5-pro"
    #GEMINI_1_5_PRO_EXP_0827 = "gemini-1.5-pro-exp-0827"
    GEMINI_1_5_FLASH_8B_EXP_0827 = "gemini-1.5-flash-8b-exp-0827"

@dataclass
class GeminiKey:
    api_key: str

class GeminiApi: 
    DEFAULT_GENERATION_CONFIG = {
        "temperature": 0.8,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    DEFAULT_SAFETY_SETTINGS = {
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }
 
    def __init__(self):
        key = os.getenv("GEMINI_KEY")
        genai.configure(api_key = key)

    def call_gemini_flash_1_5_8B(self, question):
        return self.call_gemini_flash(
            question, 
            gemini_model = GeminiModel.GEMINI_1_5_FLASH_8B_EXP_0827
        )

    def call_gemini_flash_1_5_exp(self, question):
        return self.call_gemini_flash(
            question, 
            gemini_model = GeminiModel.GEMINI_1_5_FLASH_EXP_0827
        )
    
    # TODO rename 
    def call_gemini_flash(
        self, 
        question, 
        generation_config = DEFAULT_GENERATION_CONFIG,
        gemini_model = GeminiModel.GEMINI_1_5_FLASH_8B_EXP_0827,
        safy_settings = DEFAULT_SAFETY_SETTINGS):
        
        print("gemini flash thinking...")
        
        model = genai.GenerativeModel(
            model_name = gemini_model.value,
            generation_config = generation_config,
            safety_settings = safy_settings
        )
        
        chat_session = model.start_chat(history=[])
        return chat_session.send_message(question)

    def to_text(selft,responses):
        return responses.candidates[0].content.parts[0].text