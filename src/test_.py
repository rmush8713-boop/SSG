from htmlnode import *
import unittest
from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)     
    def test_url(self):
        urlt = TextNode("", "link")
        urlt2 = TextNode("", "link", None)
        self.assertEqual(urlt, urlt2)
    def test_something(self):
        node4 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node4, node3)
    def test_none(self):
        n1 = TextNode(None, None, None)
        n2 = TextNode("", "")
        self.assertNotEqual(n1, n2)

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        t = {
    "href": "https://www.google.com",
    "target": "_blank",
}
        node = HTMLNode(None, None, None, t)
        test = ' href="https://www.google.com" target="_blank"'
        print(node.props_to_html())
        self.assertEqual(node.props_to_html(), test)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello World")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello World</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        print(node.to_html())
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>',)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        print(node.to_html())
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        print(parent_node.to_html())
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

        
if __name__ == "main":
    unittest.main()