#!/usr/bin/python3
import subprocess
import os
import sys
#import 

created_file = sys.argv[1] 


def write_to_file(created_file):

    if len(sys.argv) !=2:
        print("Usage: python file_work.py <file_to_work> ")
        sys.exit(1)

    CreateFile = open(created_file, 'w+')
    CreateFile.writelines("Files are meant to be written to and read from.\n")
    CreateFile.close()

    os.system('ls -la')

if __name__ == "__main__":
    write_to_file(created_file)


