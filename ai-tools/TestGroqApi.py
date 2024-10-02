from typing import Final
import unittest
from unittest.mock import patch, MagicMock
from llm.groq import GroqApi

class TestGroqApi(unittest.TestCase):

    def test_call_gemma(self):
        groq_api = GroqApi()
        
        response = groq_api.call_gemma("測試訊息")
        self.assertIsNotNone(response)
        choices: Final = response.choices
        self.assertTrue(choices)
        self.assertIsNotNone(choices[0])
        self.assertIsNotNone(choices[0].message)
        self.assertTrue(hasattr(choices[0].message, 'content'))
        self.assertTrue(choices[0].message.content)

if __name__ == '__main__':
    unittest.main()