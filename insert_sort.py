#! /usr/bin/env python
# coding:utf-8

def insert_sort(alist):
    #最优时间复杂度O(n),最坏时间复杂度O(n^2),稳定
    #从第二个位置开始向前插入
    for i in range(1, len(alist)):
        swap = 0
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
                swap += 1
        if not swap:
            break

if __name__ == '__main__':
    li = [6,2,3,4,5]
    insert_sort(li)
    print(li)