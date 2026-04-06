import unittest
from htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            "a",
            "click me",
            None,
            {"href": "https://example.com", "target": "_blank"}
        )
        # assert that props_to_html returns the expected string
        self.assertEqual(node.props_to_html(),' href="https://example.com" target="_blank"')

    def test_no_props(self):
        node = HTMLNode("p", "hello")
        # assert that props_to_html returns an empty string when props is None
        self.assertEqual(node.props_to_html(), "")

    def test_repr(self):
            node = HTMLNode("p", "hello", None, None)
            # assert that __repr__ returns a string with the expected content
            self.assertIsInstance(repr(node), str)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaflink(self):
         node = LeafNode("a", "Im in danger", {"bibishka": "amireallyindanger.ca"})
         self.assertEqual(node.to_html(), '<a bibishka="amireallyindanger.ca">Im in danger</a>')


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html() 

if __name__ == "__main__":
    unittest.main()