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
            #stage empty string and add node string value to string ie. "" + "{node str}" + "{node str}" + ...
            ##Itterate through child list nodes and add to string (see above) if node in child list is an instance of ParentNode,
            ##recursively call and return node string and add to staged string (see above).
            def make_tree(children):
                res = ""
                if not children:
                    return res
                else:
                    if type(children) == list:
                        for child in children:
                            if isinstance(child, ParentNode):
                                return res + f"{child.to_html()}{make_tree(children[1:])}"
                            else:
                                if child.tag:
                                    addition = f"<{child.tag}>" + f"{child.value}" + f"</{child.tag}>"
                                else:
                                    addition = f"{child.value}"

                            res = res + addition

                    else:
                        if children.tag:
                            addition = f"<{children.tag}>" + f"{children.value}" + f"</{children.tag}>"
                        else:
                            addition = f"{children.value}"

                        res = res + addition


                    print(f"stuck in a well: {res}")
                return res

            return f"<{self.tag}>{make_tree(self.children)}</{self.tag}>"
