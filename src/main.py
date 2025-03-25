import os
import shutil
from textnode import TextNode, TextType
from leafnode import LeafNode

def copy_tree(src, des):

    def copy(sub_path = "."):
        path_string = os.path.join(src, sub_path)
        items = os.listdir(path_string)
        for item in items:
            if os.path.isdir(os.path.join(path_string, item)):
                os.mkdir(os.path.join(des, sub_path, item))
                copy(sub_path + f"/{item}")

            else:
                shutil.copy(os.path.join(path_string, item),os.path.join(des, sub_path))


    return copy()


def static_to_public():
    public_rel = "./public"
    static_rel = "./static"
    test_file = "./src/main.py"

    shutil.rmtree(os.path.abspath(public_rel), True)
    os.mkdir(os.path.join(os.path.abspath("."), "public"))

    public_path = os.path.abspath(public_rel)
    static_path = os.path.abspath(static_rel)
    copy_tree(static_path, public_path)



def main():

    static_to_public()


    print(TextNode("This is some anchor text", "link", "https://www.boot.dev"))

    print("hello world")

if __name__ == "__main__":
    main()
