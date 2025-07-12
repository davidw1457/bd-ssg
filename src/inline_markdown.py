import re

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

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for n in old_nodes:
        if n.text_type != TextType.TEXT:
            new_nodes.append(n)
            continue
        images = extract_markdown_images(n.text)
        if len(images) == 0:
            new_nodes.append(n)
            continue
        text = n.text
        for i in images:
            image_text = f"![{i[0]}]({i[1]})"
            index = text.find(image_text)
            if index > 0:
                new_nodes.append(TextNode(text[:index], n.text_type))
            new_nodes.append(TextNode(i[0], TextType.IMAGE, i[1]))
            text = text[index + len(image_text):]
        if text != "":
            new_nodes.append(TextNode(text, n.text_type))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for n in old_nodes:
        links = extract_markdown_links(n.text)
        if len(links) == 0:
            new_nodes.append(n)
            continue
        text = n.text
        for l in links:
            link_text = f"[{l[0]}]({l[1]})"
            index = text.find(link_text)
            if index > 0:
                new_nodes.append(TextNode(text[:index], n.text_type))
            new_nodes.append(TextNode(l[0], TextType.LINK, l[1]))
            text = text[index + len(link_text):]
        if text != "":
            new_nodes.append(TextNode(text, n.text_type))
    return new_nodes
