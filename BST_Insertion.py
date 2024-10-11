#https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem?isFullScreen=true
#code:
class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self, current_node, val):
        if val < current_node.info:
            if current_node.left is None:
                current_node.left = Node(val)
            else:
                self._insert(current_node.left, val)
        else:
            if current_node.right is None:
                current_node.right = Node(val)
            else:
                self._insert(current_node.right, val)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
