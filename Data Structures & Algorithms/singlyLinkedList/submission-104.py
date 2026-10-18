class Node:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head
    
    def get(self, index: int) -> int:
        
        count = 0
        cur = self.head.next

        while cur:
            if count == index:
                return cur.val
            cur = cur.next
            count += 1
        
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head == self.tail:
            self.tail.next = newNode
            self.tail = newNode
        else:
            tmp = self.head.next
            self.head.next = newNode
            newNode.next = tmp

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:

        count = 0

        cur = self.head

        while cur and count < index:
            cur = cur.next
            count += 1
        
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        res = []

        cur = self.head.next

        while cur:
            res.append(cur.val)
            cur = cur.next
        
        return res
