from textnode import TextNode, TextType

"""
Given a list of TextNodes, split each text type node by
the given delimiter, and create a new node using the delimited
text of the text_type corresponding to the delimiter.
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue

        node_split = node.text.split(delimiter)
        if len(node_split) == 0:
            new_nodes.append(node)
        elif len(node_split) % 2 == 0:
            raise Exception("Matching closing delimiter not found")

        for i in range(len(node_split)):
            if i % 2 == 1:
                new_node = TextNode(node_split[i],text_type)
                new_nodes.append(new_node)
            elif len(node_split[i]) > 0:
                new_node = TextNode(node_split[i], TextType.NORMAL)
                new_nodes.append(new_node)
    return new_nodes
