class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        prop_str = ""
        for key, value in self.props.items():
            prop_str += f' {key}="{value}"'
        
        return prop_str
    
    def __eq__(self, other):
        return self.tag == other.tag and \
            self.value == other.value and \
            self.children == other.children and \
            self.props == other.props
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"