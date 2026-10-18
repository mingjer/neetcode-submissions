class Node:
    def __init__(self, val = 0, next = None):
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
            count += 1
            cur = cur.next
        
        return -1

    def insertHead(self, val: int) -> None:
        if self.head == self.tail:
            self.head.next = Node(val)
            self.tail = self.head.next
        else:
            tmp = self.head.next
            newNode = Node(val)
            self.head.next = newNode
            newNode.next = tmp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        count = 0

        cur = self.head

        while count < index and cur:
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
