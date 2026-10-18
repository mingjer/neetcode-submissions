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
            curr = curr.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.head == self.tail:
            self.head.next = newNode
            self.tail = newNode
        else:
            tmp = self.head.next
            self.head.next = newNode
            newNode.next = tmp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        count = 0
        curr = self.head

        while curr and count < index:
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
