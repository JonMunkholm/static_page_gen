import unittest
from main import extract_title
import os

class TestMainFunctions(unittest.TestCase):
    def test_extract_title(self):
        res = "Hello World!"
        text = "# Hello World!"
        title = extract_title(text)

        invalid = "### **_Crazy Town_### "

        self.assertEqual(title, res)

        with self.assertRaises(Exception):
            extract_title(invalid)
