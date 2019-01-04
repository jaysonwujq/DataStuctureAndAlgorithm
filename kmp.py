#! /usr/bin/env python
# coding=utf-8

def KMP_algorithm(string, pattern):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    pnext = gen_pnext(pattern)
    print(pnext)
    n = len(string)
    m = len(pattern)
    i, j = 0, 0
    while (i < n) and (j < m):
        print('i:',i)
        print('j:',j)
        if (string[i] == pattern[j]):
            i += 1
            j += 1
        elif (j != 0):
            j = pnext[j - 1]
        else:
            i += 1
    if (j == m):
        return i - j
    else:
        return -1


def gen_pnext(pattern):
    """
    构造临时数组pnext
    """
    index, m = 0, len(pattern)
    pnext = [0] * m
    i = 1
    while i < m:
        if (pattern[i] == pattern[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index != 0):
            index = pnext[index - 1]
        else:
            pnext[i] = 0
            i += 1
    return pnext


if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    pattern = 'abcdabcy'
    [0, 0, 0, 0, 1, 2, 3, 0]
    out = KMP_algorithm(string, pattern)
    print('res:',out)

