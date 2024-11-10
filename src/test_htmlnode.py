import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_no_props(self):
        hn = HTMLNode(tag="p", value="Hello world", children=None, props=None)
        hn_props = ""
        self.assertEqual(hn.props_to_html(), hn_props)

    def test_props_to_html(self):
        hn = HTMLNode(tag="a", value="GitHub link", children=None, props={"href": "https://github.com"})
        hn_props = ' href="https://github.com"'
        self.assertEqual(hn.props_to_html(), hn_props)

    def test_props_to_html_multiple(self):
        hn = HTMLNode(tag="a", value="GitHub link", children=None, props={"href": "https://github.com", "target": "_blank"})
        hn_props = ' href="https://github.com" target="_blank"'
        self.assertEqual(hn.props_to_html(), hn_props)

    def test_repr(self):
        hn = HTMLNode(tag="p", value="This is cool")
        hn_repr = "HTMLNode(p, This is cool, None, None)"
        self.assertEqual(hn.__repr__(), hn_repr)

    def test_init_children(self):
        hn = HTMLNode(tag="div", value=None, children=[
            HTMLNode(tag="p", value="Hey!"),
            HTMLNode(tag="p", value="Wow!"),
            HTMLNode(tag="p", value="Neat!")
        ])
        self.assertEqual(len(hn.children), 3)
        self.assertEqual(hn.children[0].value, "Hey!")
        self.assertEqual(hn.children[1].value, "Wow!")
        self.assertEqual(hn.children[2].value, "Neat!")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        ln = LeafNode("p", "This is some text", None)
        ln_html = "<p>This is some text</p>"
        self.assertEqual(ln.children, None)
        self.assertEqual(ln_html, ln.to_html())

    def test_leaf_to_html_props(self):
        ln = LeafNode("a", "Link", {"href": "https://github.com", "target": "_blank"})
        ln_html = '<a href="https://github.com" target="_blank">Link</a>'
        self.assertEqual(ln_html, ln.to_html())

    def test_leaf_no_tag(self):
        ln = LeafNode(None, "Raw text", None)
        ln_html = "Raw text"
        self.assertEqual(ln_html, ln.to_html())

    def test_leaf_no_value(self):
        ln = LeafNode("p", None, None)
        try:
            print(ln.to_html())
            self.fail()
        except ValueError:
            pass
