class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if not self.root:
            self.root = Node(key, val)
        else:
            cur = self.root
            while True:
                if cur.key < key:
                    if cur.right == None:
                        cur.right = Node(key, val)
                        return
                    cur = cur.right
                elif cur.key > key:
                    if cur.left == None:
                        cur.left = Node(key, val)
                        return
                    cur = cur.left
                else:
                    cur.val = val
                    return

    def get(self, key):

        cur = self.root

        while cur:
            if cur.key < key:
                cur = cur.right
            elif cur.key > key:
                cur = cur.left
            else:
                return cur.val
        
        return -1
        
    def getMin(self):
        if not self.root:
            return -1

        cur = self.root
        
        while True:
            if cur.left == None:
                return cur.val
            cur = cur.left

    def getMax(self):
        if not self.root:
            return -1

        cur = self.root
        
        while True:
            if cur.right == None:
                return cur.val
            cur = cur.right

    def remove(self, key):

        def findMin(node):
            cur = node

            while cur and cur.left:
                cur = cur.left
            
            return cur

        def removeHelper(curr, key):
            if curr == None:
                return None

            if key > curr.key:
                curr.right = removeHelper(curr.right, key)
            elif key < curr.key:
                curr.left = removeHelper(curr.left, key)
            else:
                if curr.left == None:
                    # Replace curr with right child
                    return curr.right
                elif curr.right == None:
                    # Replace curr with left child
                    return curr.left
                else:
                    # Swap curr with inorder successor
                    minNode = findMin(curr.right)
                    curr.key = minNode.key
                    curr.val = minNode.val
                    curr.right = removeHelper(curr.right, minNode.key)
            return curr

        self.root = removeHelper(self.root, key)

    def getInorderKeys(self):
        res = []

        def inorder(node, res):
            if not node:
                return 
            
            inorder(node.left, res)
            res.append(node.key)
            inorder(node.right, res)
        
        inorder(self.root, res)

        return res 