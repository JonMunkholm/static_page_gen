from enum import Enum
from node_functions import text_to_textnodes, text_node_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode
from textnode import TextType


class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "#Heading"
    CODE = "```Code```"
    QUOTE = ">Quote"
    UNORDERED_LIST = "- Unordered List"
    ORDERED_LIST = "1. Ordered List"

def markdown_to_blocks(markdown):
    res = ["\n".join(list(map(lambda a: a.strip(), x.strip().split("\n")))) for x in markdown.strip().split("\n\n")]

    return res

def block_to_block_type(block):
    match block[0]:
        case "#":
            return BlockType.HEADING
        case ">":
            return BlockType.QUOTE
        case "-":
            return BlockType.UNORDERED_LIST
        case "1":
            return BlockType.ORDERED_LIST
        case _:
            if block.startswith("```"):
                return BlockType.CODE
            else:
                 return BlockType.PARAGRAPH

def helper_string_text(text, tag):
    textNodes = text_to_textnodes(text)

    HTMLNodes = []
    if len(textNodes) > 1:
        for node in textNodes:
            node = text_node_to_html_node(node)
            HTMLNodes = HTMLNodes + [node]
    else:
        HTMLNodes = text_node_to_html_node(textNodes[0])


    if tag == "h":

        count = HTMLNodes.value.count("#")
        HTMLNodes.value = HTMLNodes.value.replace("#", "").strip()
        return ParentNode(f"h{count}", [HTMLNodes])

    elif tag == "blockquote":

        HTMLNodes.value = HTMLNodes.value.replace(">", "\n")
        return ParentNode(f"{tag}", HTMLNodes)

    else:
        return ParentNode(f"{tag}", HTMLNodes)

def make_list_item(nodes):

    textNodes = list(filter(lambda a: a.text, text_to_textnodes(nodes[2:].strip())))
    HTMLNodes = []

    for node in textNodes:

        if node.text_type != TextType.TEXT:

            node = text_node_to_html_node(node)

        else:

                node = LeafNode("", node.text)

        HTMLNodes = HTMLNodes + [node]

    return ParentNode("li", HTMLNodes)

def helper_string_code_and_list(text, tag):
    if tag == "code":

        leaf = LeafNode(tag, text.replace("```", "")[1:])
        return ParentNode("pre", [leaf])

    else:

        items = text.split("\n")
        HTMLNodes = []

        for item in items:
            node = make_list_item(item)
            HTMLNodes = HTMLNodes + [node]

        return ParentNode(f"{tag}", HTMLNodes)

    # else:
    #     items = text.split("\n")
    #     HTMLNodes = []

    #     for item in items:
    #         textNodes = list(filter(lambda a: a.text, text_to_textnodes(item[2:].strip())))

    #         for node in textNodes:
    #                 print(f"i need somebody: {node}")

    #                 if node.text_type != TextType.TEXT:

    #                     node = text_node_to_html_node(node)
    #                     # node = ParentNode("li", node)

    #                 else:

    #                     node = LeafNode("", node.text)

    #                 HTMLNodes = HTMLNodes + [node]
    #         HTMLNodes = [ParentNode("li", HTMLNodes)]
    #     return ParentNode(f"{tag}", HTMLNodes)


def markdown_to_html_node(markdown):
    text_list = markdown_to_blocks(markdown)
    res = []
    nodes = []
    for text in text_list:
        block_type = block_to_block_type(text)
        match block_type:
            case BlockType.HEADING:
                text = text.replace("\n"," ")
                nodes = nodes + [helper_string_text(text, "h")]
            case BlockType.QUOTE:
                text = text.replace("\n"," ")
                nodes = nodes + [helper_string_text(text, "blockquote")]
            case BlockType.PARAGRAPH:
                text = text.replace("\n"," ")
                nodes = nodes + [helper_string_text(text, "p")]
            case BlockType.CODE:
                nodes = nodes + [helper_string_code_and_list(text, "code")]
            case BlockType.UNORDERED_LIST:
                nodes = nodes + [helper_string_code_and_list(text, "ul")]
            case BlockType.ORDERED_LIST:
                nodes = nodes + [helper_string_code_and_list(text, "ol")]


    res = res + nodes
    return ParentNode("div", res)
