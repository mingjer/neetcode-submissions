class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = None
        self.right = None

class Deque:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def append(self, value: int) -> None:
        newNode = Node(value)
        self.tail.right = newNode
        newNode.left = self.tail
        self.tail = newNode

        self.size += 1

    def appendleft(self, value: int) -> None:
        
        newNode = Node(value)
        if self.size == 0:
            self.head.right = newNode
            newNode.left = self.head
            self.tail = newNode
        else:
            tmp = self.head.right
            self.head.right = newNode
            newNode.left = self.head
            newNode.right = tmp
            tmp.left = newNode
        
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        prev = self.tail.left
        tmp = self.tail
        prev.right = None
        self.tail = prev

        self.size -= 1
        return tmp.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        tmp = self.head.right
        if tmp == self.tail:
            self.head.right = None
            self.tail = self.head
        else:
            self.head.right = tmp.right
            tmp.right.left = self.head
            

        self.size -= 1
        return tmp.val
