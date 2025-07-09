import unittest

from parentnode import ParentNode
from leafnode   import LeafNode

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        props = {"class": "test-class", "id": "test-id"}
        node = ParentNode("h1", "inner text", props)
        node2 = ParentNode("h1", "inner text", props)
        self.assertEqual(node, node2)
        
        
    def test_not_eq(self):
        child_node = LeafNode("span", "child")
        self.assertIsNotNone(child_node)
        children = [child_node]
        props = {"class": "test-class", "id": "test-id"}
        
        node = ParentNode("h1", children, props)
        node2 = ParentNode("h2", children, props)
        self.assertNotEqual(node, node2)

        node3 = ParentNode("h1", children, props)
        node4 = ParentNode("h1", None, props)
        self.assertNotEqual(node3, node4)

        node5 = ParentNode("h1", children, None)
        node6 = ParentNode("h1", children, props)
        self.assertNotEqual(node5, node6)

    def test_required_only(self):
        node = ParentNode(None, None)
        self.assertIsNone(node.tag)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_5_props_to_html(self):
        child_node = LeafNode("span", "child")
        props = {
                    "class": "test-class", 
                    "id": "test-id",
                    "name": "test-name",
                    "style": "color: red;",
                    "data-custom": "custom-value"
                 }
        props_str = ' class="test-class" id="test-id" name="test-name" style="color: red;" data-custom="custom-value"'
        node = ParentNode("h1", child_node, props)
        self.assertEqual(node.props_to_html(), props_str)
        
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

if __name__ == "__main__":
    unittest.main()