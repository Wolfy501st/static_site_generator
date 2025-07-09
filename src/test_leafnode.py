import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        props = {"class": "test-class", "id": "test-id"}
        node = LeafNode("h1", "inner text", props)
        node2 = LeafNode("h1", "inner text", props)
        self.assertEqual(node, node2)
        
        
    def test_not_eq(self):
        props = {"class": "test-class", "id": "test-id"}
        node = LeafNode("h1", "inner text", props)
        node2 = LeafNode("h2", "inner text", props)
        self.assertNotEqual(node, node2)

    def test_required_only(self):
        node = LeafNode("", None)
        self.assertIsNotNone(node.tag)
        self.assertIsNone(node.value)
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
        node = LeafNode("h1", "inner text", props)
        self.assertEqual(node.props_to_html(), props_str)
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()