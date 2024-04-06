##########
## User will write to a file
## and the module will display
## the content of the file
##

import sys


FileName = sys.argv[1]

FileWriter = open(FileName, 'a')
FileContent = input("Write<start your writing by hitting space bar>: ")
FileWriter.writelines(FileContent)

with open(FileName, 'r') as RealFile:
    lines = RealFile.readlines()


for line in lines:
    print(line.strip())




