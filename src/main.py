from textnode import *
import os
import shutil
from recursive_file_copy import *
from generate_pages import *
import sys

basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

from_dir = 'static'
to_dir = 'docs'

def main():
    if os.path.exists(to_dir):
        shutil.rmtree(to_dir)
    copy_dir_tree(from_dir, to_dir)
    recursive_generator('content', 'template.html', 'docs', basepath)


main()