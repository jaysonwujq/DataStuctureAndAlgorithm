#! /usr/bin/env python
# coding:utf-8

def bubble_sort(alist):
    #最优时间复杂度O(n);最坏时间复杂度O(n^2),稳定
    for i in range(len(alist)-1):
        swap = 0
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                swap += 1
        if not swap:
            break

def bubble_sort1(alist):
    for j in range(len(alist)-1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        swap = 0
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swap += 1
        if not swap:
            break

if __name__ == '__main__':
    li = [6,2,4,5,3]
    bubble_sort(li)
    print(li)