import unittest

from markdown_utils import split_nodes_delimiter
from textnode import TextType, TextNode

class TestSplitDelimiter(unittest.TestCase):
    def test_single_node(self):
        node = TextNode("This node contains some **bold** text!", TextType.NORMAL)
        target = [
            TextNode("This node contains some ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text!", TextType.NORMAL)
        ] 
        self.assertEqual(split_nodes_delimiter([node], "**", TextType.BOLD), target)

        node = TextNode("This node contains some *italic* text!", TextType.NORMAL)
        target = [
            TextNode("This node contains some ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text!", TextType.NORMAL)
        ] 
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), target)

        node = TextNode("This node contains some `code` text!", TextType.NORMAL)
        target = [
            TextNode("This node contains some ", TextType.NORMAL),
            TextNode("code", TextType.CODE),
            TextNode(" text!", TextType.NORMAL)
        ] 
        self.assertEqual(split_nodes_delimiter([node], "`", TextType.CODE), target)

    def test_skip_non_text(self):
        nodes = [
            TextNode("This node contains some **bold** text!", TextType.NORMAL),
            TextNode("But this one is already bold!", TextType.BOLD)
        ]
        target = [
            TextNode("This node contains some ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" text!", TextType.NORMAL),
            TextNode("But this one is already bold!", TextType.BOLD)
        ]
        self.assertEqual(split_nodes_delimiter(nodes, "**", TextType.BOLD), target)

    def test_delimiters_on_edges(self):
        node = TextNode("*What if...* the delimiters are on the *edges?*", TextType.NORMAL)
        target = [
            TextNode("What if...", TextType.ITALIC),
            TextNode(" the delimiters are on the ", TextType.NORMAL),
            TextNode("edges?", TextType.ITALIC)
        ]
        self.assertEqual(split_nodes_delimiter([node], "*", TextType.ITALIC), target)

    def test_invalid_delimiters(self):
        node = TextNode("This delimiter ** doesn't get matched!", TextType.NORMAL)
        try:
            _ = split_nodes_delimiter(node, "**", TextType.BOLD)
            self.fail()
        except Exception:
            pass

    def test_bold_italic(self):
        node = TextNode("This text contains **bold** and *italic*", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        target = [
            TextNode("This text contains ", TextType.NORMAL),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.NORMAL),
            TextNode("italic", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, target)

if __name__ == "__main__":
    unittest.main()

