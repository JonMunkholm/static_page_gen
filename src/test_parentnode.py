import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("i", "Malchom")
        child_node3 = LeafNode("b", "Alexander")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><i>Malchom</i><b>Alexander</b></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild_node2 = LeafNode("i", "Malchom")
        grandchild_node3 = LeafNode("p", "Alexander")
        grandchild_node4 = LeafNode("span", "Forgotten child")
        child_node = ParentNode("span", [grandchild_node, grandchild_node2])
        child_node2 = ParentNode("div", [grandchild_node3, grandchild_node4])
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(),"<div><span><b>grandchild</b><i>Malchom</i></span><div><p>Alexander</p><span>Forgotten child</span></div></div>")
