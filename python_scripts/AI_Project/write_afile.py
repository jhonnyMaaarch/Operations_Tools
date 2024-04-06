#####
# user provides a file name
# and writes to it and the content of the file is displayed
import sys
import subprocess

filename = sys.argv[1]


fileReader = open(filename, 'a')
content = input("Enter your input here: ")
fileReader.writelines(content)


#open the file in read mode

fileWriter = open(filename, 'r')

#store the content in a list
#lines = fileWriter.readlines()


#print the content
#for line in lines:
#    print(line)



#import subprocess

# I want to read the entire content

subprocess.call('cat '+ filename, shell=True)



