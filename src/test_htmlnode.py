import unittest

from htmlnode import HTIMLNode

class TestHTIMLNode(unittest.TestCase):

    def test_prpos_to_html(self):
        node_child = HTIMLNode("p", "something", "",{"href": "https://www.google.com", "target": "_blank",})
        self.assertEqual(node_child.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_prpos_to_html2(self):
        node_child = HTIMLNode("p", "something", "",{"href": "https://www.google.com", "target": "_blank",})
        node_parent = HTIMLNode("h1", "I AM THE CAPTAIN NOW", node_child, {"href": "www.linkedin.com"})
        self.assertEqual(node_parent.props_to_html(), 'href="www.linkedin.com"')

    def test_parent_obj(self):
        node_child = HTIMLNode("p", "something", "",{"href": "https://www.google.com", "target": "_blank",})
        node_parent = HTIMLNode("h1", "I AM THE CAPTAIN NOW", node_child, {"href": "www.linkedin.com"})
        self.assertEqual(node_parent.children, node_child)
