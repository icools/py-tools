import unittest
import os
from llm.gemini_api import GeminiApi, GeminiModel

class TestGeminiApi(unittest.TestCase):

    def test_call_gemini_flash(self):
        # GEMINI_API_KEY = os.getenv("GEMINI_KEY")
        gemini_api = GeminiApi()
        responses = gemini_api.call_gemini_flash_1_5_8B("電車難題怎麼解")
        self.assertIsNotNone(responses)
        print(gemini_api.to_text(responses))

if __name__ == '__main__':
    unittest.main()