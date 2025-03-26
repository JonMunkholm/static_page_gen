import os
import shutil
from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_functions import markdown_to_blocks, markdown_to_html_node

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

def extract_title(text):
    f_title = ""
    blocks = markdown_to_blocks(text)
    for block in blocks:
        if block.startswith("# "):
            f_title = block[1:].strip()
            break

    if f_title:
        return f_title
    else:
        raise Exception("Invalid file - markdown file, does not have a title.")

def generate_page(from_path, template_path, dest_path):
    print("Generating page from from_path to dest_path using template_path")
    f_text = open(os.path.join(from_path, "index.md"))

    f_content = f_text.read()
    template_content = open(template_path).read()

    HTML_content = markdown_to_html_node(f_content)
    # title = extract_title(f_content)

    # template_content.replace("{{ Title }}", title)
    # template_content.replace("{{ Content }}", title)

    # with open(dest_path, "index.html") as file:
    #     file.write(template_content)





def static_to_public():
    public_rel = "./public"
    static_rel = "./static"
    template_rel = "./template.html"
    content_rel = "./content"

    shutil.rmtree(os.path.abspath(public_rel), True)
    os.mkdir(os.path.join(os.path.abspath("."), "public"))

    public_path = os.path.abspath(public_rel)
    static_path = os.path.abspath(static_rel)
    content_rel_path = os.path.abspath(content_rel)
    template_path = os.path.abspath(template_rel)
    copy_tree(static_path, public_path)
    generate_page(content_rel, template_path, public_path)






def main():

    static_to_public()


    # print(TextNode("This is some anchor text", "link", "https://www.boot.dev"))

    # print("hello world")

if __name__ == "__main__":
    main()
