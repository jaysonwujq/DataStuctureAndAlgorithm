#!/usr/bin/env python
# coding:utf-8

class SingleNode(object):
    '''单链表循环节点'''
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleCycleLinkList(object):
    '''循环单链表'''
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''判断是否为空'''
        return self._head == None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return
        cur = self._head
        #print(cur.item, end=' ')
        while cur.next != self._head:
            print(cur.item, end=' ')
            cur = cur.next
        print(cur.item, end=' ')
        print('')
    def add(self, item):
        '''头部添加元素'''
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            node.next = self._head
            #移到链表尾部，使尾部节点的next指向node
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            self._head = node

    def append(self, item):
        '''尾部添加元素'''
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node
            node.next = self._head

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
        if self.is_empty():
            return
        cur = self._head
        pre = None
        #若头节点的元素就是要找的item
        if cur.item == item:
            #若链表不止一个节点
            if cur.next != self._head:
                while cur.next != self._head:
                    cur = cur.next
                cur.next = self._head.next
                self._head = self._head.next
            else:
                self.head = None
        else:
            pre = self._head
            while cur != self._head:
                if cur.item == item:
                    pre.next = cur.next
                    return
                else:
                    pre = cur
                    cur = cur.next
            #尾节点
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        '''判断节点是否存在'''
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

if __name__ == '__main__':
    ll = SingleCycleLinkList()
    ll.add(1)
    ll.travel()
    ll.append(2)
    print(ll.length())
    ll.remove(1)
    ll.insert(1,3)
    ll.travel()
