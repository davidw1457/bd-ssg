from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        in_delimiter = True
        for p in n.text.split(delimiter):
            if in_delimiter and p != "":
                new_nodes.append(TextNode(p, TextType.TEXT))
            elif p != "":
                new_nodes.append(TextNode(p, text_type))
            in_delimiter = not in_delimiter
        if in_delimiter:
            raise ValueError(f"unclosed {delimiter} in text")
    return new_nodes


