#!/usr/bin/python3
# trying out sys.argv
import os
import sys
import subprocess

os.system('ls -la')
if len(sys.argv) != 2:
    print("Usage: python dir_deleter_v2.py <directory to delete>")
    sys.exit(1)

dir_deleted = sys.argv[1]
try:
    os.rmdir(dir_deleted)
    print("directory " + dir_deleted + " successfully deleted!")
    os.system('ls -la')
except OSError as e:
    print(f"Error: {e}")
    print(f"Directory '{dir_deleted}' could not be deleted. ")

#if __name__ == "__main__":
#    main()
