import unittest
from google_sheet import log_to_google_sheet

class TestLogToGoogleSheet(unittest.TestCase):
    def test_log_to_google_sheet_success(self):
        try:
            log_to_google_sheet("Hello")
            print("Successfully logged to Google Sheet")
            self.assertTrue
        except Exception as e:
            self.fail(f"Logging to Google Sheet failed: {e}")

if __name__ == '__main__':
    unittest.main()