from htmlnode import HTIMLNode

class ParentNode(HTIMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError
        elif not self.children:
            raise ValueError("Think about the children (Oooohhh Nooooo)!")
        else:
            def make_tree(children):
                res = ""
                if not children:
                    return ""
                    # return f"<{self.tag}>{self.value}</{self.tag}>"
                else:
                    res = f"{self.children[0].to_html()}{make_tree(self.children[1:])}"
                    res = f"<{self.tag}>" + res + f"</{self.tag}>"
                    return res

            return make_tree(self.children)
