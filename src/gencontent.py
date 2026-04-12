from markd_to_html import *
from htmlnode import *
import os

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            title = line[2:]
            return title.strip()
    else:
        raise Exception("No title found")
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path, "r")
    from_content = file.read()
    file.close()
    file = open(template_path, "r")
    templ_content = file.read()
    file.close()

    node = markdown_to_html_node(from_content)
    html_string = node.to_html()
    title = extract_title(from_content)
    templ_content = templ_content.replace("{{ Title }}", title)
    templ_content = templ_content.replace("{{ Content }}", html_string)

    
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    file = open(dest_path, "w")
    file.write(templ_content)
    file.close()