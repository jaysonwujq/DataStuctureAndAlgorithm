#! /usr/bin/env python
# coding:utf-8

def shell_sort(alist):
    #最优时间复杂度：根据步长序列的不同而不同,最坏时间复杂度：O(n^2),不稳定
    n = len(alist)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        gap = gap //2

if __name__ == '__main__':
    li = [6,2,4,5,3,1,0]
    shell_sort(li)
    print(li)