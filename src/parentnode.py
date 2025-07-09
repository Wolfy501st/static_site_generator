from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):            
        if self.tag is None:
            raise ValueError("ParentNode must have a tag.")
        
        full_str = ""
        for child in self.children:
            full_str += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{full_str}</{self.tag}>"
    
    def __eq__(self, other):
        return self.tag == other.tag and \
            self.children == other.children and \
            self.props == other.props
        
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"