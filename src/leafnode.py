from htmlnode import HTIMLNode

class LeafNode(HTIMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
