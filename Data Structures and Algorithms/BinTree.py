# -*- coding: utf-8 -*-
class BinaryTree(object):
    def __init__(self, root_value):
        self.root = root_value
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            left_subtree = BinaryTree(node)
            left_subtree.leftChild = self.leftChild
            self.leftChild = left_subtree

    def insertRight(self, node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            right_subtree = BinaryTree(node)
            right_subtree.rightChild = self.rightChild
            self.rightChild = right_subtree

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, root_value):
        self.root = root_value

    def getRootVal(self):
        return self.root

    # 树的前序遍历
    def preorder(self):
        print self.root
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

