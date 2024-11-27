import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


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

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        tn = TextNode("This is a text node", TextType.NORMAL)
        hn1 = text_node_to_html_node(tn)
        hn2 = LeafNode(None, "This is a text node")
        self.assertEqual(hn1.to_html(), hn2.to_html())
        self.assertEqual(hn1.tag, hn2.tag)
        self.assertEqual(hn1.value, hn2.value)
        self.assertEqual(hn1.children, hn2.children)
        self.assertEqual(hn1.props, hn2.props)

    def test_bold_italic_code(self):
        def fields_equal(self, hn1, hn2):
            self.assertEqual(hn1.to_html(), hn2.to_html())
            self.assertEqual(hn1.tag, hn2.tag)
            self.assertEqual(hn1.value, hn2.value)
            self.assertEqual(hn1.children, hn2.children)
            self.assertEqual(hn1.props, hn2.props)

        tn = TextNode("This is bold", TextType.BOLD)
        hn1 = text_node_to_html_node(tn)
        hn2 = LeafNode("b", "This is bold")
        fields_equal(self,hn1,hn2)

        tn = TextNode("This is italic", TextType.ITALIC)
        hn1 = text_node_to_html_node(tn)
        hn2 = LeafNode("i", "This is italic")
        fields_equal(self,hn1,hn2)

        tn = TextNode("This is code", TextType.CODE)
        hn1 = text_node_to_html_node(tn)
        hn2 = LeafNode("code", "This is code")
        fields_equal(self,hn1,hn2)

    def test_link(self):
        tn = TextNode("This is a link", TextType.LINK, "https://example.com")
        hn1 = text_node_to_html_node(tn)
        hn2 = LeafNode("a", "This is a link", {"href": "https://example.com"})
        self.assertEqual(hn1.to_html(), hn2.to_html())
        self.assertEqual(hn1.tag, hn2.tag)
        self.assertEqual(hn1.value, hn2.value)
        self.assertEqual(hn1.children, hn2.children)
        self.assertEqual(hn1.props, hn2.props)

    def test_image(self):
        tn = TextNode("This is an image", TextType.IMAGE, "https://example.com/image.jpg")
        hn1 = text_node_to_html_node(tn)
        hn2 = LeafNode("img", "", {"src": "https://example.com/image.jpg", "alt": "This is an image"})
        self.assertEqual(hn1.to_html(), hn2.to_html())
        self.assertEqual(hn1.tag, hn2.tag)
        self.assertEqual(hn1.value, hn2.value)
        self.assertEqual(hn1.children, hn2.children)
        self.assertEqual(hn1.props, hn2.props)

if __name__ == "__main__":
    unittest.main()
