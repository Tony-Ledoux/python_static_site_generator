class HTMLNode:
    def __init__(self, tag= None, value= None,children= None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")
    
    def props_to_html(self):
        if self.props is None or len(self.props)==0:
            return ""
        props = []
        for key, val in self.props.items():
            props.append(f' {key}="{val}"')
        return str.join("",props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    