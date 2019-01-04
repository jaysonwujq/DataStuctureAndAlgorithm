#! /usr/bin/env python
# coding:utf-8

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue('hello')
    q.enqueue('world')
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
