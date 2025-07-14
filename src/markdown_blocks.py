import re
from enum import Enum

from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks_draft = markdown.split("\n\n")
    blocks = []
    for b in blocks_draft:
        b = b.strip()
        if b != "":
            blocks.append(b)
    return blocks

def block_to_block_type(text):
    lines = text.split("\n")
    start = lines[0].split()[0]
    blocktype = None
    number = 1
    match start:
        case "```":
            end = lines[-1].split()[-1]
            if end == "```":
                return BlockType.CODE
            return BlockType.PARAGRAPH
        case ">":
            blocktype = BlockType.QUOTE
        case "-":
            blocktype = BlockType.ULIST
        case "1.":
            blocktype = BlockType.OLIST
        case _:
            if start == "#" * len(start):
                return BlockType.HEADING
            return BlockType.PARAGRAPH
    for l in lines:
        start = l.split()[0]
        match blocktype:
            case BlockType.QUOTE:
                if start != ">":
                    return BlockType.PARAGRAPH
            case BlockType.ULIST:
                if start != "-":
                    return BlockType.PARAGRAPH
            case BlockType.OLIST:
                if start != f"{number}.":
                    return BlockType.PARAGRAPH
                number += 1
    return blocktype

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_node = ParentNode("div", [])
    for b in blocks:
        block_type = block_to_block_type(b)
        tag = None
        node = None
        match block_type:
            case BlockType.QUOTE:
                tag = "blockquote"
            case BlockType.PARAGRAPH:
                tag = "p"
            case BlockType.HEADING:
                level = len(b.split()[0])
                tag = f"h{level}"
            case BlockType.CODE:
                tag = "code"
            case BlockType.ULIST:
                tag = "ul"
            case BlockType.OLIST:
                tag = "ol"
        if tag == "code":
            child = LeafNode(tag, b[3:-3].lstrip())
            node = ParentNode("pre", [child])
        elif tag in ("ol","ul"):
            children = text_to_listchildren(b)
            node = ParentNode(tag, children)
        else:
            children = text_to_children(b, tag)
            node = ParentNode(tag, children)
        parent_node.children.append(node)
    return parent_node

def text_to_children(text, tag=None):
    children = []
    items = text.split("\n")
    for n in range (0, len(items)):
        i = items[n].strip()
        if tag == "blockquote" or tag.startswith("h"):
            i = " ".join(i.split(" ")[1:])
        if n < len(items) - 1:
            i += " "
        text_nodes = text_to_textnodes(i)
        html_nodes = []
        for t in text_nodes:
            html_nodes.append(text_node_to_html_node(t))
        children.extend(html_nodes)
    return children

def text_to_listchildren(text):
    children = []
    items = text.split("\n")
    for i in items:
        prefix = i.split()[0]
        text = i[len(prefix):].lstrip()
        text_nodes = text_to_textnodes(text)
        grandchildren = []
        for t in text_nodes:
            grandchildren.append(text_node_to_html_node(t))
        node = ParentNode("li", grandchildren)
        children.append(node)
    return children
