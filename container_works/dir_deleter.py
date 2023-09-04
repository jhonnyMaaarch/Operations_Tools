#! /usr/bin/python3
import subprocess
import os
import shutil
os.system('ls -la')
dir_name = input("Enter the name of the directory: ")
os.system('rm -rf '+ dir_name)
os.system('ls -la ')


