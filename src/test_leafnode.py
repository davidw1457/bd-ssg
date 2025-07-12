import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_oneprop(self):
        node = LeafNode("h1", "Hello, world!", {"color": "green"})
        self.assertEqual(node.to_html(), "<h1 color=\"green\">Hello, world!</h1>")

    def test_leaf_to_html_multiprops(self):
        node = LeafNode(
            "li",
            "List Item",
            {
                "color": "red",
                "style": "bold",
            }
        )
        self.assertEqual(
            node.to_html(),
            "<li color=\"red\" style=\"bold\">List Item</li>"
        )

if __name__ == "__main__":
    unittest.main()
