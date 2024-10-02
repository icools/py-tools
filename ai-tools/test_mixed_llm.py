import unittest
from unittest.mock import patch
from llm.mixed_chat import MixedChat

class TestMixedChat(unittest.TestCase):
    def setUp(self):
        self.mixed_chat = MixedChat()

    def test_generate_character(self):
        character = self.mixed_chat.generate_character()
        self.assertIsInstance(character, str)
        self.assertIn("歲", character)
        self.assertIn("喜歡", character)

    def test_call_groq(self):
        prompt = "今天天氣怎麼樣？"
        response = self.mixed_chat.call_groq(prompt)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_call_samba_nova(self):
        prompt = "今天天氣怎麼樣？"
        response = self.mixed_chat.call_samba_nova(prompt)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_call_gemini_flash(self):
        prompt = "今天天氣怎麼樣？"
        response = self.mixed_chat.call_gemini_flash(prompt)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")

    def test_mixed_chat(self):
        question = "今天天氣怎麼樣？"
        final_answer = self.mixed_chat.mixed_chat(question)
        self.assertIsInstance(final_answer, str)
        self.assertNotEqual(final_answer, "")
        self.assertEqual(len(self.mixed_chat.responses), 3)

if __name__ == "__main__":
    unittest.main()