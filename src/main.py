from textnode import *
import shutil
import os
from copystatic import *
from gencontent import *
import sys


def main():
    if len(sys.argv) >= 2: 
        basepath = sys.argv[1]
    else: 
        basepath = "/"
    docs_dir = "./docs"
    static_dir = "./static"
    if os.path.exists(docs_dir):
        shutil.rmtree(docs_dir)
    copy_static(static_dir, docs_dir)
    generate_pages_recursive("./content", "./template.html", "./docs", basepath)

if __name__ == "__main__":
    main()