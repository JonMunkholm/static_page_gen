from enum import Enum


class TextType(Enum):
    TEXT = "Normal Text"
    BOLD = "**Bold**"
    ITALIC = "_Italic_"
    CODE = "`Code`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        text = self.text == other.text
        text_type = self.text_type == other.text_type
        url = self.url == other.url

        return text == text_type == url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
