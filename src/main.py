import os, shutil, sys
from pathlib import Path
from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_functions import markdown_to_blocks, markdown_to_html_node

def copy_tree(src, des):

    if not os.path.exists(des):
        os.mkdir(des)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        des_path = os.path.join(des, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, des_path)
        else:
            copy_tree(src_path, des_path)

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


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
            from_path = os.path.join(dir_path_content, filename)
            dest_path = os.path.join(dest_dir_path, filename)
            if os.path.isfile(from_path):
                dest_path = Path(dest_path).with_suffix(".html")
                generate_page(from_path, template_path, dest_path, basepath)
            else:
                generate_pages_recursive(from_path, template_path, dest_path, basepath)


def generate_page(from_path, template_path, dest_path, basepath):
    print("Generating page from from_path to dest_path using template_path")

    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)

    html = html.replace("href = '/", "href = '" + basepath)
    html = html.replace("src = '/", "src = '" + basepath)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', 'href="' + basepath)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)






#directory and root path
docs_dir = "./docs"
static_dir = "./static"
template_dir = "./template.html"
content_dir = "./content"
default_basepath = "/"


def main():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)

    copy_tree(static_dir, docs_dir)
    generate_pages_recursive(content_dir, template_dir, docs_dir, basepath)

if __name__ == "__main__":
    main()
