:#!/usr/bin/env python3
import subprocess
import sys
import os
import re
from os import listdir, sep
from os.path import abspath, basename, isdir
from sys import argv

# YOUR CODE GOES here


def listdir(path):
    dirs = os.listdir(path)
    files = [x for x in dirs if x[0] != ('.')]
    files = sorted(files, key=lambda s: re.sub('[^0-9a-zA-Z]+', '', s).lower())
    return files


def tree(path, padding, print_files=False, isLast=False, isFirst=False):
    count = 0
    dirs = listdir(path)
    for i, file in enumerate(dirs):
        count += 1
        path = path + sep + file
        isLast = (i == len(dirs))
        if isdir(path):
            if count == len(file):
                if isFirst:
                    tree(path, padding, print_files, isLast, False)
                else:
                    tree(path, padding + ' ', print_files, isLast, False)
            else:
                tree(path, padding + '│', print_files, isLast, False)
        else:
            if isLast:
                print(padding + '└── ' + file)
            else:
                print(padding + '├── ' + file)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        path = os.getcwd()
    else:
        path = sys.argv[1]
    tree(path, '')
