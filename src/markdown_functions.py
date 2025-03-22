from enum import Enum

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
