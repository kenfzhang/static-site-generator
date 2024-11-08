import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node_repr = "TextNode(This is a text node, normal, None)"
        self.assertEqual(node.__repr__(), node_repr)

    def test_diff_type_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_text_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is definitely a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_no_url_neq(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL, "http://example.com")
        self.assertNotEqual(node, node2)



if __name__ == "__main__":
    unittest.main()
