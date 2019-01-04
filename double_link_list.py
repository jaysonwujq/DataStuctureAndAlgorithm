#!/usr/bin/env python
# coding:utf-8

class Node(object):
    '''单链表节点'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class DLinkList(object):
    '''双向链表'''
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
            print(cur.item, end=' ')
            cur = cur.next
        print('')

    def add(self, item):
        '''头部添加元素'''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        '''尾部添加元素'''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            cur.prev = cur

    def insert(self, pos, item):
        '''指定位置添加元素'''
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = node(item)
            count = 0
            cur = self._head
            while count < (pos - 1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next = node

    def remove(self,item):
        '''删除节点'''
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                #第一个就是删除节点
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    if cur.next:
                        cur.next.prev = cur.prev
                    break
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
    ll = DLinkList()
    ll.add(1)
    ll.insert(1, 2)
    ll.append(2)
    ll.remove(1)
    ll.travel()
