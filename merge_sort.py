#! /usr/bin/env python
# coding:utf-8

def merge_sort(alist):
    #最优时间复杂度：O(nlogn),最坏时间复杂度：O(nlogn),稳定
    n = len(alist)
    if n <= 1:
        return alist
    mid = n//2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]
    return result

if __name__ == '__main__':
    li = [6,2,3,4,5]
    a = merge_sort(li)
    print(a)