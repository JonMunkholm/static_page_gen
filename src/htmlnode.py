
class HTIMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def ___repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        res = ""
        for item in self.props.items():
            res = res + f' {item[0]}="{item[1]}"'
            print(res)

        return res[1:]
