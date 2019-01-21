#! /usr/bin/env python
# coding:utf-8

def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (first+last)//2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False

def binary_search1(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        elif item < alist[midpoint]:
            return binary_search1(alist[:midpoint], item)
        else:
            return binary_search1(alist[midpoint+1:], item)

if __name__ == '__main__':
    li = [1,2,3,4,5,6,7,8,9]
    print(binary_search1(li, 2))