import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_noProps(self):
        node = HTMLNode()
        self.assertTrue(isinstance(node, HTMLNode))

    def test_tagOnly(self):
        node = HTMLNode(tag="p")
        self.assertTrue(
            isinstance(node, HTMLNode) and
            node.tag == "p" and
            node.value is None and
            node.children  is None and
            node.props is None
        )

    def test_valueOnly(self):
        node = HTMLNode(value="this is a paragraph")
        self.assertTrue(
            node.value == "this is a paragraph" and
            node.tag is None and
            node.children is None and
            node.props is None
        )

    def test_childrenOnly(self):
        node = HTMLNode(
            children=[
                HTMLNode(
                    tag="p",
                    value="this is a paragraph"
                )
            ]
        )
        self.assertTrue(
            len(node.children) == 1 and
            node.tag is None and
            node.value is None and
            node.props is None
        )

    def test_propsOnly(self):
        node = HTMLNode(
            props = {
                "href": "https://www.google.com",
            }
        )
        self.assertTrue(
            len(node.props) == 1 and
            node.tag is None and
            node.value is None and
            node.children is None
        )

    def test_propsToHtml(self):
        node = HTMLNode(
            props = {
                "href": "https://www.google.com",
                "target": "_blank"
            }
        )
        self.assertEqual(
            node.props_to_html(),
            " href=\"https://www.google.com\" target=\"_blank\""
        )

if __name__ == "__main__":
    unittest.main()
