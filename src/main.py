from textnode import *
import shutil
import os
from copystatic import *
from gencontent import *


def main():
    public_dir = "./public"
    static_dir = "./static"
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    copy_static(static_dir, public_dir)
    generate_pages_recursive("./content", "./template.html", "./public")

if __name__ == "__main__":
    main()