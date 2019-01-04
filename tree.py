#! /usr/bin/env python
# coding:utf-8

class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = [self.root]
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self, node):
        '''递归实现先序遍历'''
        if node == None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        '''递归实现中序遍历'''
        if node == None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        '''递归实现后序遍历'''
        if node == None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')

    def stretch(self, node):
        '''队列实现层次遍历'''
        if node == None:
            return
        queue = [node]
        while queue:
            cur = queue.pop(0)
            print(cur.elem, end=' ')
            if cur.lchild != None:
                queue.append(cur.lchild)
            if cur.rchild != None:
                queue.append(cur.rchild)

if __name__ == '__main__':
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(5)
    tree.add(10)
    tree.preorder(tree.root)
    print('')
    tree.inorder(tree.root)
    print('')
    tree.postorder(tree.root)
    print('')
    tree.stretch(tree.root)
    print('')




