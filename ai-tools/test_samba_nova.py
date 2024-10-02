import unittest
from unittest.mock import patch
import os,sys

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'llm')))
from llm.samba_nova import chat_with_samba_nova

class TestSambaNova(unittest.TestCase):
    def test_chat(self):
        response = chat_with_samba_nova("測試訊息")
        self.assertIsNotNone(response)
        self.assertTrue(response.choices)
        self.assertIsNotNone(response.choices[0])
        self.assertTrue(hasattr(response.choices[0], 'message'))
        self.assertIsNotNone(response.choices[0].message)
        self.assertTrue(hasattr(response.choices[0].message, 'content'))
        self.assertTrue(response.choices[0].message.content)

if __name__ == '__main__':
    unittest.main()