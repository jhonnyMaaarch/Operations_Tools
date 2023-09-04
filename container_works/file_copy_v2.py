#!/usr/bin/python
import os
import shutil
import subprocess
import sys

file_to_move = sys.argv[1]
dest_dir = sys.argv[2]
def file_move(file_to_move, dest_dir):
    # first validate the number of input is correct
    if len(sys.argv) != 3:
        print("Usage: ./file_copy.py <file_to_move> <destination_dir> ")
        sys.exit(1)
#    file_to_move = sys.argv[1]
#    dest_dir = sys.argv[2]

    if os.path.isfile(file_to_move) & os.path.isdir(dest_dir):
        shutil.copy(file_to_move, dest_dir)
        print(f"file '{file_to_move}' successfully moved to '{dest_dir}' directory.")
        os.chdir(dest_dir)
        os.getcwd()
        os.system('ls -la')
    else:
        try:
            os.path.isfile(file_to_move)
        except OSError as f:
            print(f"Error: {f}")
        try:
            os.path.isdir(dest_dir)
        except OSError as d:
            print(f"Error: {d}")

if __name__ == "__main__":
    file_move(file_to_move, dest_dir)



