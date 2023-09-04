#!/usr/bin/python3
# The purpose of this app is to create new directory that never existed
import os
import subprocess
import sys

if len(sys.argv) != 2:
    print("Usage: python create_dir.py <dir_to_make>")
    sys.exit(1)

os.system('ls -la')
dir_to_make = sys.argv[1]
try:
    os.mkdir(dir_to_make)
    print(f"directory '{dir_to_make}' successfully created!")
    os.system('ls -la')
except OSError as e:
    print(f"Error '{e}'")
    print(f"directory '{dir_to_make}' cannot be created!")
    os.system('ls -la')




