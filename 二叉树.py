# -*- encoding: utf8 -*-
class Node(object):
    def __init__(self, element=-1, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right

class Tree(object):
    def __init__(self):
        self.root = Node()

    def insert_left(self, element):
        node = Node(element)
        if self.root.element == -1:  # 假设树是空的。则对根节点赋值
            self.root = node

        self.root.left = node

    def insert_right(self, element):
        node = Node(element)
        if self.root.element == -1:  # 假设树是空的。则对根节点赋值
            self.root = node

        self.root.right = node

    def preorder(self, treenode):
        '前序（pre-order，NLR）遍历'
        if treenode is 0:
            return
        print treenode.data
        self.preorder(treenode.left)
        self.preorder(treenode.right)

a = Tree()
for i in range(100):
    a.insert_left(i)

for i in range(100, 200):
    a.insert_right(i)

a.insert_left(1000)


