#!/usr/bin/env python
# coding:utf-8

class SingleNode(object):
    '''单链表节点'''
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleLinkList(object):
    '''单链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判断是否为空'''
        return self._head == None

    def length(self):
        '''链表长度'''
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        cur = self._head
        while cur != None:
            print(cur.item, sep=' ')
            cur = cur.next

    def add(self, item):
        '''头部添加元素'''
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        '''尾部添加元素'''
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self,item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.item == item:
                #第一个就是删除节点
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        '''判断节点是否存在'''
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

if __name__ == '__main__':
    ll = SingleLinkList()
    ll.add(1)
    ll.append(2)
    ll.add(0)
    ll.travel()
    ll.insert(0,4)
    ll.travel()
    ll.search(4)
    ll.remove(4)
    ll.search(4)
