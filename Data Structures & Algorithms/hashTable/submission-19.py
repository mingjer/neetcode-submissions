class Node:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * capacity

    def hash_function(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.table[index]

        if head is None:
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
        index = self.hash_function(key)
        head = self.table[index]

        while head:
            if head.key == key:
                return head.val
            head = head.next
        
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        head = self.table[index]

        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                else:
                    self.table[index] = head.next
                self.size -= 1
                return True
            prev, head = head, head.next
        
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
                if newTable[index] == None:
                    newTable[index] = Node(node.key, node.val)
                else:
                    head = newTable[index]
                    while head.next:
                        head = head.next
                    head.next = Node(node.key, node.val)
                node = node.next
        
        self.table = newTable


