####################################
## The user will write and 
##display the content of a file
##
import subprocess
import sys

filename = sys.argv[1]

fileWriter = open(filename, 'a')
content = input("Enter <press space bar>: \n")
fileWriter.writelines(content)

subprocess.call('cat '+filename, shell=True)


