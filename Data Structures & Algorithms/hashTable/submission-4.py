class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.table = [None] * capacity
        self.size = 0

    def hashFunction(self, key):
        return key % self.capacity
    
    def insert(self, key: int, value: int) -> None:
        index = self.hashFunction(key)
        head = self.table[index]

        if not head:
            self.table[index] = Node(key, value)
        else:
            prev = None
            while head:
                if head.key == key:
                    head.val = value
                    return
                prev, head = head, head.next
            prev.next = Node(key, value)
        self.size += 1
        if self.size / self.capacity >= 0.5:
            self.resize()
        
    def get(self, key: int) -> int:
        index = self.hashFunction(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.val
            node = node.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hashFunction(key)
        node = self.table[index]

        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[index] = node.next
                self.size -=1
                return True
            prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        newTable = [None] * self.capacity

        for node in self.table:
            while node:
                index = node.key % self.capacity
                if newTable[index] is None:
                    newTable[index] = Node(node.key, node.val)
                else:
                    newNode = newTable[index]
                    while newNode.next:
                        newNode = newNode.next
                    newNode.next = Node(node.key, node.val)
                node = node.next
        
        self.table = newTable

