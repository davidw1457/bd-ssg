import shutil
import os

def copy_files_recursive(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir(dest)
    contents = os.listdir(src)
    if len(contents) == 0:
        return
    subdirectories = []
    for c in contents:
        full_src = os.path.join(src, c)
        if os.path.isfile(full_src):
            full_dest = os.path.join(dest, c)
            shutil.copy(full_src, full_dest)
            continue
        subdirectories.append(c)
    for sd in subdirectories:
        full_src = os.path.join(src, sd)
        full_dest = os.path.join(dest, sd)
        copy_files_recursive(full_src, full_dest)
