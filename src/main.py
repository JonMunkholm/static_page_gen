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


def generate_pages_recursive(file, temp, path_string, base):

    if file.endswith(".md"):

        file_path = os.path.join(path_string, file)
        file_text = open(file_path).read()

        HTML_content = markdown_to_html_node(file_text).to_html()
        title = extract_title(file_text)

        template_text = open(temp).read()

        new_content = template_text.replace("{{ Title }}", title)
        new_content = new_content.replace("{{ Content }}", HTML_content)
        new_content = new_content.replace("href= '/", 'href= "' + base)
        new_content = new_content.replace("src= '/", 'src= "' + base)

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

    copy_tree(content_dir, docs_dir)

    md_to_HTML(docs_dir, template_dir)





#directory and root path
docs_dir = "./docs"
static_dir = "./static"
template_dir = "./template.html"
content_dir = "./content"
default_basepath = "/"

def static_to_docs():


    #github hosting use
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print(f"help me: {basepath}")

    shutil.rmtree(docs_dir, True)
    if not os.path.exists(docs_dir):
        os.mkdir(docs_dir)


    copy_tree(static_dir, docs_dir)
    generate_page(content_dir, template_dir, docs_dir, basepath)






def main():

    static_to_docs()


    # print(TextNode("This is some anchor text", "link", "https://www.boot.dev"))

    # print("hello world")

if __name__ == "__main__":
    main()
