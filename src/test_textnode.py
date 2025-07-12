import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_noteqtext(self):
        node = TextNode("node 1", TextType.ITALIC_TEXT, "url")
        node2 = TextNode("node 2", TextType.ITALIC_TEXT, "url")
        self.assertNotEqual(node, node2)

    def test_noteqtype(self):
        node = TextNode("This is a text node", TextType.IMAGE, "url")
        node2 = TextNode("This is a text node", TextType.LINK, "url")
        self.assertNotEqual(node, node2)

    def test_notequrl(self):
        node = TextNode("This is a text node", TextType.TEXT, "url")
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
