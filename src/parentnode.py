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
                    return res
                else:
                    for child in children:
                        if isinstance(child, ParentNode):
                            res = f"{child.to_html()}{make_tree(children[1:])}"
                        else:
                            if child.tag:
                                res = res + f"<{child.tag}>" + f"{child.value}" + f"</{child.tag}>"
                            else:
                                res = res + f"{child.value}"

                return f"<{self.tag}>{res}</{self.tag}>"

            return make_tree(self.children)
