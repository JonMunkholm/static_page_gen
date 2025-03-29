import os, shutil, sys
from textnode import TextNode, TextType
from leafnode import LeafNode
from markdown_functions import markdown_to_blocks, markdown_to_html_node

def copy_tree(src, des):

    def copy(sub_path = ""):

        path_string = os.path.join(src, sub_path)
        items = os.listdir(path_string)
        for item in items:

            if os.path.isdir(os.path.join(path_string, item)):

                os.mkdir(os.path.join(des, sub_path, item))
                copy(sub_path + f"{item}/")

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


def generate_pages_recursive(file, temp, path_string):

    if file.endswith(".md"):

        file_path = os.path.join(path_string, file)
        file_text = open(file_path).read()

        HTML_content = markdown_to_html_node(file_text).to_html()
        title = extract_title(file_text)

        template_text = open(temp).read()

        new_content = template_text.replace("{{ Title }}", title)
        new_content = new_content.replace("{{ Content }}", HTML_content)
        new_content = new_content.replace("href= '/", file_path)
        new_content = new_content.replace("src= '/", file_path)

        file_name = f"{os.path.basename(file_path).split(".")[0]}.{os.path.basename(temp).split(".")[1]}"


        # Create a new file
        with open(file_path, "w") as file:
            file.write(new_content)

        # Rename the file
        os.rename(file_path, os.path.join(path_string, file_name))

        # Verify the rename
        if os.path.exists(os.path.join(path_string, file_name)):
            print("File renamed successfully!")
        else:
            print("File rename failed.")

    else:
        return



def md_to_HTML(des, temp):

    def update_file(sub_path = ""):

        path_string = os.path.join(des, sub_path)
        items = os.listdir(path_string)

        for item in items:
            if os.path.isdir(os.path.join(path_string, item)):

                new_string = sub_path + f"{item}/"
                update_file(new_string)

            else:

                generate_pages_recursive(item, temp, path_string)



    return update_file()


def generate_page(from_path, template_path, dest_path):
    print("Generating page from from_path to dest_path using template_path")

    copy_tree(from_path, dest_path)

    md_to_HTML(dest_path, template_path)








def static_to_docs():
    docs_rel = "docs"
    static_rel = "static"
    template_rel = "template.html"
    content_rel = "content"

    #local repo use
    # basepath = os.path.abspath(".")

    #github hosting use
    basepath = sys.argv[0]

    shutil.rmtree(os.path.join(basepath, docs_rel), True)
    os.mkdir(os.path.join(basepath, docs_rel))

    docs_path = os.path.join(basepath, docs_rel)
    static_path = os.path.join(basepath, static_rel)
    content_rel_path = os.path.join(basepath, content_rel)
    template_path = os.path.join(basepath, template_rel)


    copy_tree(static_path, docs_path)
    generate_page(content_rel, template_path, docs_path)






def main():

    static_to_docs()


    # print(TextNode("This is some anchor text", "link", "https://www.boot.dev"))

    # print("hello world")

if __name__ == "__main__":
    main()
