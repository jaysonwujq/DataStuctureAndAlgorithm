#! /usr/bin/env python
# coding:utf-8

def meiju(li, n1, n2):
    '''枚举法计算数组中两个字符串的最小距离，这是方法1，时间复杂度 O(n^2)
    '''
    if n1 not in li or n2 not in li:
        return -1
    if n1 == n2:
        return 0
    min = len(li)
    for i in range(0, len(li)):
        if n1 == li[i]:
            pos1 = i
            for j in range(0, len(li)):
                if n2 == li[j]:
                    pos2 = j
                    distance = abs(i - j)
                    if distance < min:
                        min = distance
    return min

def create_hash(li):
    '''生成哈希列表'''
    set_li = list(set(li))
    li_hash = {}
    for i in range(0, len(set_li)):
        temp = {}
        for j in range(0, len(set_li)):
            if set_li[i] != set_li[j]:
                temp[set_li[j]] = meiju(li, set_li[i], set_li[j])
        li_hash[set_li[i]] = temp
    return li_hash


def hash_way(li_hash, n1, n2):
    '''从哈希列表获取值'''
    if n1 not in li_hash or n2 not in li_hash:
        return -1
    if n1 == n2:
        return 0
    return li_hash[n1][n2]

if __name__ == '__main__':
    li = [1, 3, 5, 2, 1, 6, 3, 6, 1, 2, 2, 5, 3]
    n1 = 1
    n2 = 5
    set_li = list(set(li))
    li_hash = create_hash(li)
    print(meiju(li, n1, n2))
    print(hash_way(li_hash, n1, n2))