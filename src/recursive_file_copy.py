import os
import shutil

def copy_dir_tree(target, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for f in os.listdir(target):
        from_ = os.path.join(target, f)
        to_ = os.path.join(destination, f)
        print(f" * {from_} -> {to_}")
        if os.path.isfile(from_):
            shutil.copy(from_, to_)
        else:
            copy_dir_tree(from_, to_)