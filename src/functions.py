import re

from textnode import TextType, TextNode
from leafnode import LeafNode

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



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    res = []
    for node in old_nodes:

        split = node.text[:].split(delimiter)

        for i in range(len(split)):
            if i % 2 == 0:
                new_node = TextNode(split[i], node.text_type)

            else:
                new_node = TextNode(split[i], text_type)

            res.append(new_node)

    return res

def extract_markdown_images(text):
    res = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return res

def extract_markdown_links(text):
    res = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

    return res


def split_helper(node, cb, tup_prop_type):
    text = node.text[:]
    items = cb(node.text)

    next = 0
    for item in items:


        if next == 0:
            if tup_prop_type == "link":
                text = text.split(f"[{item[0]}]({item[1]})")
            else:
                text = text.split(f"![{item[0]}]({item[1]})")

            text = text[:1] + [list(item[:])] + text[1:]


        else:
            if tup_prop_type == "link":
                text = text[:next] + text[next].split(f"[{item[0]}]({item[1]})")
            else:
                text = text[:next] + text[next].split(f"![{item[0]}]({item[1]})")

            text = text[:next + 1] + [list(item[:])] + text[next + 1 :]

        next = len(text) - 1

    return list(filter(lambda a: a != "", text))

def split_nodes_link(old_nodes):

    res = []

    for node in old_nodes:

        text = split_helper(node, extract_markdown_links, "link")

        for i in range(len(text)):
            if not isinstance(text[i], list) and len(text[i]) > 1:
                new_node = TextNode(text[i], node.text_type)

            elif isinstance(text[i], list):
                new_node = TextNode(text[i][0], TextType.LINK, text[i][1])
            else:
                new_node = TextNode("".join(text), node.text_type, node.url)
                res = res + [new_node]
                break

            res = res + [new_node]

    return res

def split_nodes_image(old_nodes):
    res = []

    for node in old_nodes:

        text = split_helper(node, extract_markdown_images, "image")

        for i in range(len(text)):
            if not isinstance(text[i], list) and len(text[i]) > 1:
                new_node = TextNode(text[i], node.text_type)

            elif isinstance(text[i], list):
                new_node = TextNode(text[i][0], TextType.IMAGE, text[i][1])
            else:
                new_node = TextNode("".join(text), node.text_type, node.url)
                res = res + [new_node]
                break

            res = res + [new_node]

    return res

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_image(new_nodes)
    res = split_nodes_link(new_nodes)
    return res
