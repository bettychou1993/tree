#!/usr/bin/env python3
import subprocess
import sys
import subprocess
import sys
import os
import re #regular expression
from os import listdir, sep
from os.path import abspath, basename, isdir
from sys import argv

# YOUR CODE GOES here

def listdir(dir):
    listdir = os.listdir(dir) # returns a list containing the names of the entries in the directory given by path.
    files = [x for x in listdir(dir) if isdir(dir+sep+x)] 
    files = sorted(files, key=lambda :re.sub('[^0-9a-zA-Z]+','', s).lower())
    return files

def tree(dir, padding, print_files=False, isLast=False, isFirst=False):
    files = []
    for i, file in enumerate(files):
        count += 1
        path = dir + sep + file
        isLast = i == last
        if isdir(path):
            if count == len(files):
                if isFirst:
                    tree(path, padding, print_files, isLast, False)
                else:
                    tree(path, padding + ' ', print_files, isLast, False)
            else:
                tree(path, padding + '│', print_files, isLast, False)
        else:
            if isLast:
                print (padding + '└── ' + file)
            else:
                print (padding + '├── ' + file)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = os.getcwd()
        print('.')
    else:
        path = sys.argv[1]
        print(path)
tree(path,'')








if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
