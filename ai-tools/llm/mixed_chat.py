# mixed_chat.py

import random

from llm.groq import GroqApi, GroqModel
from llm.samba_nova import chat_with_samba_nova
from llm.gemini_api import GeminiApi,GeminiModel

class MixedChat:
    def __init__(self):
        self.responses = []
        self.models = [
            ("groq", self.call_groq),
            ("samba_nova", self.call_samba_nova),
            ("gemini_flash", self.call_gemini_flash)
        ]

        # 定義各個屬性的列表
        self.sex_list = ["男生", "女生"]
        self.age_list = list(range(18, 46))  # 年齡範圍：18歲到45歲
        self.hobby_list = [
            "打籃球", "閱讀", "烹飪", "旅行", "編程", "瑜伽",
            "遊戲", "繪畫", "登山", "攝影", "釣魚", "舞蹈",
            "吉他", "烘焙", "滑板", "寫作", "跑步", "園藝",
            "電影", "音樂", "跳舞"
        ]
        # 分別為男性和女性定義名字列表
        self.name_list_male = [
            "志豪", "大衛", "凱文", "阿明", "建國", "大偉",
            "小杰", "志明", "小龍", "阿強", "大志", "凱倫",
            "小宇", "阿宏", "建華"
        ]
        self.name_list_female = [
            "小美", "小芳", "婷婷", "小莉", "小雪", "小華",
            "小燕", "小雯", "小敏", "小娜", "小麗", "小婷"
        ]

    def call_groq(self, prompt):
        try:
            groq_api = GroqApi()
            response = groq_api.call_gemma(prompt, GroqModel.GEMMA2_9B_IT)
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Groq API 錯誤: {e}"

    def call_samba_nova(self, prompt):
        try:
            response = chat_with_samba_nova(prompt)
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Samba Nova 錯誤: {e}"

    def call_gemini_flash(self, prompt):
        try:
            gemini_api = GeminiApi()
            responses = gemini_api.call_gemini_flash(prompt)
            return gemini_api.to_text(responses)
        except Exception as e:
            return f"Gemini Flash 錯誤: {e}"
        
    def generate_character(self):
        sex = random.choice(self.sex_list)
        age = random.choice(self.age_list)
        hobby = random.choice(self.hobby_list)
        # 根據性別選擇名字
        if sex == "男生":
            name = random.choice(self.name_list_male)
        else:
            name = random.choice(self.name_list_female)
        # 拼湊角色設定
        character = f"{sex},{age}歲,喜歡{hobby},{name}"
        return character

    def mixed_chat(self, question):
        random.shuffle(self.models)
        conversation = []
        for model_name, model_func in self.models:
            character = self.generate_character()
            prompt = f"問題是{question},你的角色是{character},直接用繁體中文回答我的問題，並且用台灣PTT鄉民的口氣回答:"
            response = model_func(prompt)
            conversation.append(f"{character} ({model_name}) 回應: {response}")
            self.responses.append({
                'character': character,
                'model_name': model_name,
                'response': response
            })
        return "\n".join(conversation)