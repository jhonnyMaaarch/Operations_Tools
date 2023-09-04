#! /usr/bin/python3
import os
import sys
import subprocess

def delete_dir(dir_to_delete):
    try:
        os.rmdir(dir_to_delete)
        print(f"directory '{dir_to_delete}' successfully deleted")
        os.system('ls -la')
    except OSError as e:
        print(f"Error '{e}'")
        print(f"Directory '{dir_to_delete}' could not be deleted")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dir_deleter_v3.py <dir_to_be_deleted>")
        sys.exit(1)

    dir_to_delete = sys.argv[1]

    delete_dir(dir_to_delete)

