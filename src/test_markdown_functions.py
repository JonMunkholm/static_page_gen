import unittest
from markdown_functions import markdown_to_blocks, block_to_block_type, markdown_to_html_node
from markdown_functions import BlockType

class TestMarkdownFunctions(unittest.TestCase):

    def test_markdown_to_blocks(self):
        res = [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ]
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertListEqual(blocks, res)

    def test_block_to_block_type(self):
        res = [
            BlockType.PARAGRAPH,
            BlockType.HEADING,
            BlockType.CODE,
            BlockType.QUOTE,
            BlockType.UNORDERED_LIST,
            BlockType.ORDERED_LIST
        ]

        blocks = [
            block_to_block_type("Just some text, for a paragraph."),
            block_to_block_type("####What a wonderfull Heading this would be."),
            block_to_block_type("```print('Hello World!')```"),
            block_to_block_type(">It is impossible to begin to learn that which one thinks one already knows."),
            block_to_block_type("- Debt: The First 5,000 Years\n- When Reason Goes on Holiday\n- The Great Depression: A Diary"),
            block_to_block_type("1. Silicon Valley\n2. The Day of The Jackal\n3. There is Something in The Rain"),
        ]

        self.assertListEqual(blocks, res)

    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """

        res = "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        node = markdown_to_html_node(md)
        # html = node.to_html()
        # self.assertEqual(html, res)
        self.assertEqual(node, 6)


    # def test_codeblock(self):
    #     md = """
    #         ```
    #         This is text that _should_ remain
    #         the **same** even with inline stuff
    #         ```
    #         """

    #     res = "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>"
    #     node = markdown_to_html_node(md)
    #     html = node.to_html()
    #     self.assertEqual(html, res)
