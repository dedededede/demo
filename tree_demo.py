# -*- encoding: utf8 -*-
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.father = None

class Tree(object):
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, node):
        father = None
        cur = self.root
        while cur:
            if cur.value == node.value:
                return
            father = cur
            if node.value < cur.value:
                cur = cur.left
            else:
                cur = cur.right

        node.father = father
        if father is None:
            self.root = node
        elif node.value < father.value:
            father.left = node
        else:
            father.right = node

    def search(self, value):
        """
        Search function will search a node into tree.
        """
        cur = self.root
        while cur:
            if cur.value == value:
                return cur
            elif cur.value < value:
                cur = cur.right
            else:
                cur = cur.left
        return

    def deleteNode(self, node):
        """
        Delete function will delete a node into tree.
        Not complete , may need some more scenarion that we can handle
        Now it is handling only leaf.
        """

        # Check if tree is empty.
        cur = self.root
        while cur:
            if cur.value < node.value:
                cur = cur.right
            elif cur.value > node.value:
                cur = cur.left
            elif cur.value == node.value:
                if cur.left is None and cur.right is None:  # 说明是叶子节点
                    if cur.father is None:  # 说明是根节点, 直接把树赋值为空
                        self.root = None
                    else:
                        if cur.father.left.value == node.value:
                            cur.father.left = None
                        elif cur.father.right.value == node.value:
                            cur.father.right = None

                elif cur.left is not None and cur.right is None:
                    cur.father.left = cur.left
                    cur.left.father = cur.father

                elif cur.left is None and cur.right is not None:
                    cur.father.right = cur.right
                    cur.right.father = cur.father

                elif cur.left is not Node and cur.right is not None:
                    cur.father.left = cur.left
                    cur.right.father = cur.left
                    cur.left.right = cur.right
                    cur.left.father = cur.father

                return

    def preOrder(self, root):
        if root is not None:
            print root.value
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print root.value
            self.inOrder(root.right)

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print root.value

    def levelOrder(self, root):
        node_list = []
        node_list.append(root)

        while 1:
            new_node_list = []
            if len(node_list) == 0:
                break
            for index in range(len(node_list)):
                item = node_list[index]
                print item.value
                if item.left:
                    new_node_list.append(item.left)
                if item.right:
                    new_node_list.append(item.right)
            node_list = new_node_list

tree = Tree()
tree.insert(Node(10))
tree.insert(Node(5))
tree.insert(Node(15))
tree.insert(Node(1))
tree.insert(Node(9))
tree.insert(Node(16))
#tree.deleteNode(Node(5))
print "前序遍历"
tree.preOrder(tree.root)
print "中序遍历"
tree.inOrder(tree.root)
print "后序遍历"
tree.postOrder(tree.root)

print "层遍历"
tree.levelOrder(tree.root)



