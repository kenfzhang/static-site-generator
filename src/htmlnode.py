
class HTMLNode:
    """
    tag :       A string representing the HTML tag name (h1", "div", etc)
    value :     A string representing the value of the HTML tag
                (e.g. the text inside a paragraph)
    children :  A list of HTMLNode objects representing the children of this node
    props :     A dictionary of key-value pairs representing the attributes
                of the HTML tag. (e.g. "href" is an attribute of an <a> tag)
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    # Overridden by child classes
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        props_html = ""
        for p in self.props:
            props_html += f' {p}="{self.props[p]}"'
        return props_html

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
