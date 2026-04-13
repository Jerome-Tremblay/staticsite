from markd_to_html import *
from htmlnode import *
import os
from pathlib import Path

def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            title = line[2:]
            return title.strip()
    else:
        raise Exception("No title found")
    
def generate_page(from_path, template_path, dest_path, basepath):
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
    templ_content = templ_content.replace('href="/', f'href="{basepath}')
    templ_content = templ_content.replace('src="/', f'src="{basepath}')

    
    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)
    file = open(dest_path, "w")
    file.write(templ_content)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            dest_path = Path(os.path.join(dest_dir_path, entry)).with_suffix(".html")
            generate_page(os.path.join(dir_path_content, entry), template_path, dest_path, basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry), basepath)
