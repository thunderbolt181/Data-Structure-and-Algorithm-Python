class Node:
    def __init__(self, value, prev = None, n = None) -> None:
        self.value = value
        self.prev = prev
        self.next = n

class DLinkedList:
    def __init__(self,node) -> None:
        self.head = self.tail = node

    def p(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def rev(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def insert(self,value,pos=-1) -> None:
        node = self.head
        if self.head is None:
            self.head = self.tail = Node(value)
        elif pos == 0:
            temp = Node(value, n = self.head)
            self.head.prev = temp
            self.head = temp
        elif pos == -1:
            temp = Node(value, prev= self.tail)
            self.tail.next = temp
            self.tail = temp
        else:
            temp = Node(value)
            loc = 1
            while node.next and loc != pos:
                node = node.next
                loc+=1
            node.next.prev = temp
            temp.next = node.next
            node.next = temp
            temp.prev = node

    def delete(self,value):
        node = self.head
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev.none
                self.tail = self.head
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            while node.value!=value:
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev
            del node
        

d = DLinkedList(Node(1))

d.insert(2,0)
d.insert(3)
d.insert(4)
d.insert(5,1)

d.delete(3)

d.p()
print("---")
d.rev()