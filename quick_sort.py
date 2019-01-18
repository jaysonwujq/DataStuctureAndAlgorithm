#! /usr/bin/env python
# coding:utf-8

def quick_sort(alist, start, end):
    #最优时间复杂度O(nlogn),最坏时间复杂度O(n^2),不稳定
    #递归退出的条件
    if start >= end:
        return
    mid = alist[start]

    low = start
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low] =alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,将基准元素放到该位置
    alist[low] = mid

    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)

if __name__ == '__main__':
    li = [6,2,4,5,3]
    quick_sort(li, 0, len(li)-1)
    print(li)