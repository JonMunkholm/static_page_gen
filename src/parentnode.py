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
                                return f"{child.to_html()}{make_tree(children[1:])}"
                            else:
                                if child.tag:
                                    if child.tag == "a":
                                        child_tag_open = f"a href = {child.props}"
                                    elif child.tag == "img":
                                        child_tag_open = f"img src = {child.props}"
                                    else:
                                        child_tag_open = child.tag

                                    addition = f"<{child_tag_open}>" + f"{child.value}" + f"</{child.tag}>"
                                else:
                                    addition = f"{child.value}"

                            res = res + addition

                    else:
                        if children.tag:
                            if children.tag:
                                    if children.tag == "a":
                                        children_tag_open = f"a href = {children.props}"
                                    elif children.tag == "img":
                                        children_tag_open = f"img src = {children.props}"
                                    else:
                                        children_tag_open = children.tag

                                    addition = f"<{children_tag_open}>" + f"{children.value}" + f"</{children.tag}>"
                        else:
                            addition = f"{children.value}"

                        res = f"{res}{addition}"


                return res

            return f"<{self.tag}>{make_tree(self.children)}</{self.tag}>"
