class Node:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next

class LinkedList:   
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.dummy = Node()
        self.dummy.next = self.head
        self.count = 0
    def get(self, index: int):
        if self.count == 0 or index not in range(self.count):
            return -1
        else:
            tmp = self.head
            count = 0
            while tmp:
                # print(count)
                if count == index:
                    print("get the value of index", index, "and the value is ", tmp.val)
                    return tmp.val
                tmp = tmp.next  
                count += 1          
    def insertHead(self, val: int):
        if self.count == 0:
            self.head.val = val
        else:
            self.dummy.next = Node(val)
            self.dummy.next.next = self.head
            self.head = self.dummy.next
        # print("insert from the head and the value of head is ", self.head.val)
        self.count += 1
    def insertTail(self, val: int):
        if self.count == 0:
            self.head.val = val
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        # print("insert from the tail and the value of tail is ", self.tail.val)
        self.count += 1
    def remove(self, index: int):
        if self.count == 0 or index not in range(self.count):    
            return False
        else:
            if index == 0:
                self.head = self.head.next
                self.dummy.next = self.head
            else:
                cur = self.dummy
                self.dummy.next = cur.next
                count = 0
                while count < index and cur:
                    count += 1
                    cur = cur.next
                print(cur.val, cur.next.val)
                if cur and cur.next:
                    if cur.next == self.tail:
                        self.tail = cur
                    cur.next = cur.next.next
                self.head = self.dummy.next
            self.count -= 1
            print(self.getValues())
            return True
    def getValues(self):
        if self.count == 0:
            return []
        else:
            tmp = self.head
            res = []
            while tmp:
                res.append(tmp.val)
                tmp = tmp.next
            
            return res
