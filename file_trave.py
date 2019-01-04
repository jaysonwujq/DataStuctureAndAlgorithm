#! /usr/bin/env python
# coding:utf-8

import os
from os import listdir

def stretch(mydir):
    '''广度优先'''
    dirs = [os.path.abspath(mydir)]
    while dirs:
        current = dirs.pop(0)
        for subPath in listdir(current):
            path = os.path.join(current, subPath)
            if os.path.isdir(path):
                dirs.append(path)
            print(path)

def depth(mydir):
    '''深度优先'''
    mydir = os.path.abspath(mydir)
    for subPath in listdir(mydir):
        path = os.path.join(mydir, subPath)
        if os.path.isdir(path):
            depth(path)
        print(path)

if __name__ == '__main__':
    stretch(os.getcwd())
    depth(os.getcwd())