#!/usr/bin/python3
# This script improvement upon the earlier file_actions.py version seeks to dynamically enable write operation on a specified user file

import subprocess
import os
import sys


created_file = sys.argv[1]


def write_to_file(created_file):


    added_writes = []
    CreateFile = open(created_file, 'w+')
    CreateFile.writelines('This is the beginning content.')
    action_question = input("would you like to write to file: (Y or N): ")
    if action_question == 'Y':
        new_content = input('')
        added_writes.append(new_content)
        File_additions = open(created_file, 'a')
        File_additions.writelines(added_writes)
        
        #check_content = subprocess.check_output('cat %s'% created_file, shell=True)
        #print("Current file content: \n", check_content)
        #CreateFile.close()
        #w
    else:
        CreateFile.close()
        os.system('ls -la')

if __name__ == "__main__":
    write_to_file(created_file)






