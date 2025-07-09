import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        childnode = HTMLNode("p", "child text")
        props = {"class": "test-class", "id": "test-id"}
        node = HTMLNode("h1", "inner text", [childnode], props)
        node2 = HTMLNode("h1", "inner text", [childnode], props)
        self.assertEqual(node, node2)
        
        
    def test_not_eq(self):
        childnode = HTMLNode("p", "child text")
        props = {"class": "test-class", "id": "test-id"}
        node = HTMLNode("h1", "inner text", [childnode], props)
        node2 = HTMLNode("h2", "inner text", [childnode], props)
        self.assertNotEqual(node, node2)

    def test_all_none(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_5_props_to_html(self):
        props = {
                    "class": "test-class", 
                    "id": "test-id",
                    "name": "test-name",
                    "style": "color: red;",
                    "data-custom": "custom-value"
                 }
        props_str = ' class="test-class" id="test-id" name="test-name" style="color: red;" data-custom="custom-value"'
        node = HTMLNode("h1", "inner text", props=props)
        self.assertEqual(node.props_to_html(), props_str)
        


if __name__ == "__main__":
    unittest.main()