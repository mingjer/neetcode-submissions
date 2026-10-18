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
        curr = self.head.next

        while curr:
            if count == index:
                return curr.val
            count += 1
            curr = curr.next
        
        return -1

    def insertHead(self, val: int) -> None:
        newHead = Node(val)
        newHead.next = self.head.next
        self.head.next = newHead

        if newHead.next == None:
            self.tail = newHead

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        count = 0

        while count < index and curr:
            count += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        
        res = []
        curr = self.head.next

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
