from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
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

    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case TextType.TEXT:
                return LeafNode(None, text_node.text, text_node.url)
            case TextType.BOLD:
                return LeafNode("b", text_node.text, text_node.url)
            case TextType.ITALIC:
                return LeafNode("i", text_node.text, text_node.url)
            case TextType.CODE:
                return LeafNode("code", text_node.text, text_node.url)
            case TextType.LINK:
                return LeafNode("a", text_node.text, text_node.url)
            case TextType.IMAGE:
                return LeafNode("img", text_node.text, text_node.url)
            case _:
                raise Exception("invalid text type")
