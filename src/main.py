from textnode import *
import os
import shutil
from recursive_file_copy import *
from generate_pages import *

from_dir = 'static'
to_dir = 'public'

def main():
    if os.path.exists(to_dir):
        shutil.rmtree(to_dir)
    copy_dir_tree(from_dir, to_dir)
    recursive_generator('content', 'template.html', 'public')


main()