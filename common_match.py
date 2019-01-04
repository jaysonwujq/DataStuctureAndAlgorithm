#!/usr/bin/env python
# coding:utf-8
s = 'ababebabwasabcawabca'
m = 'abc'

len_s = len(s)
len_m = len(m)
i, j = 0, 0
while i < len_m and j < len_s:
    if m[i] == s[j]:
        i += 1
        j += 1
    else:
        i = 0
        j = j - i + 1
if i == len_m:
    print(j-i)
else:
    print('no match')