#! /usr/bin/env python
# coding:utf-8

def select_sort(alist):
    #最优时间复杂度O(n^2),最坏时间复杂度O(n^2),不稳定（选最大情况）
    n = len(alist)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if alist[j] < alist[min_idx]:
                min_idx = j
        if min_idx != i:
            alist[i], alist[min_idx] = alist[min_idx], alist[i]

if __name__ == '__main__':
    li = [6,2,4,5,3]
    select_sort(li)
    print(li)