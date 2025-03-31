import os, shutil, sys
from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_functions import markdown_to_blocks, markdown_to_html_node

def copy_tree(src, des):
    print(f"mapping file path: {src}")
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


def generate_pages_recursive(src, temp, des, base):
###something wrong with this function +++++++++++++++++++++++++++++++
    if src.endswith(".md"):

        src_path = os.path.join(des, src)
        src_text = open(src_path).read()

        HTML_content = markdown_to_html_node(src_text).to_html()
        title = extract_title(src_text)

        template_text = open(temp).read()

        new_content = template_text.replace("{{ Title }}", title)
        new_content = new_content.replace("{{ Content }}", HTML_content)
        template = new_content.replace('href="/', 'href="' + base)
        template = new_content.replace('src="/', 'src="' + base)
        src_name = f"{os.path.basename(src_path).split(".")[0]}.{os.path.basename(temp).split(".")[1]}"


        # Create a new src
        with open(src_path, "w") as src:
            src.write(new_content)

        # Rename the src
        os.rename(src_path, os.path.join(des, src_name))

        # Verify the rename
        if os.path.exists(os.path.join(des, src_name)):
            print("src renamed successfully!")
        else:
            print("src rename failed.")

    else:
        return



def md_to_HTML(des, temp, base):

    def update_file(sub_path = ""):

        path_string = os.path.join(des, sub_path)
        items = os.listdir(path_string)

        for item in items:
            if os.path.isdir(os.path.join(path_string, item)):

                new_string = sub_path + f"{item}/"
                update_file(new_string)

            else:

                generate_pages_recursive(item, temp, path_string, base)



    return update_file()


def generate_page(content_dir, template_dir, docs_dir, basepath):
    print("Generating page from from_path to dest_path using template_path")

    print(f"help me: {basepath}")
    copy_tree(content_dir, docs_dir)
    md_to_HTML(docs_dir, template_dir, basepath)





#directory and root path
docs_dir = "./docs"
static_dir = "./static"
template_dir = "./template.html"
content_dir = "./content"
default_basepath = "/"

def static_to_docs():

    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)

    copy_tree(static_dir, docs_dir)
    generate_page(content_dir, template_dir, docs_dir, basepath)






def main():

    static_to_docs()


    # print(TextNode("This is some anchor text", "link", "https://www.boot.dev"))

    # print("hello world")

if __name__ == "__main__":
    main()
