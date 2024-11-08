from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    """
    Properties:
        text :  Text content of the node
        text_type : The type of text this node contains,
                    which is a member of the TextType enum.
        url :   the URL of the link or image, if the node is one
                of those types.
    """
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    # Returns True if all properties of two TextNode objects are equal.
    def __eq__(self, value) -> bool:
        return (self.text == value.text and 
            self.text_type == value.text_type and 
            self.url == value.url)

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


