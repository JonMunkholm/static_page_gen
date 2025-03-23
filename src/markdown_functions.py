from enum import Enum
from node_functions import text_to_textnodes, text_node_to_html_node
from parentnode import ParentNode

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


def helper_string_nodes(text, tag):
    textNodes = text_to_textnodes(text)
    HTMLNodes = []
    if len(textNodes) > 1:
        for node in textNodes:
            node = text_node_to_html_node(node)
            HTMLNodes = HTMLNodes + [node]
    else:
        HTMLNodes = text_node_to_html_node(textNodes[0])


    if tag == "h":
        count = HTMLNodes[0].value.count("#")
        return ParentNode(f"h{count}", HTMLNodes)
    else:
        return ParentNode(f"{tag}", HTMLNodes)


def markdown_to_html_node(markdown):
    pass
    # text_list = markdown_to_blocks(markdown)
    # res = []
    # for text in text_list:
    #     block_type = block_to_block_type(text)
    #     nodes = []
    #     parent = None
    #     match block_type:
    #         case BlockType.HEADING:
    #             nodes = helper_string_nodes(text, "h")
    #         case BlockType.QUOTE:
    #             nodes = helper_string_nodes(text, "blockquote")
    #         case BlockType.PARAGRAPH:
    #             nodes = helper_string_nodes(text, "p")
    #         case BlockType.CODE:
    #             nodes = ParentNode("code")
    #         case BlockType.UNORDERED_LIST:
    #             pass
    #         case BlockType.ORDERED_LIST:
    #             pass


    #     res = res + [nodes]
    #     #logic related to parent nodes with children that are parent nodes - need to figuer out
    #     #need to reconsider the relationship between textNode and leafNode
    # return res[1].children
# ParentNode("div", res)
