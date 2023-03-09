class Node:
    def __init__(self,value,n=None) -> None:
        self.value = value
        self.next = n

class Queue:
    def __init__(self,node = None) -> None:
        self.head = self.tail = node

    def __str__(self) -> str:
        a = []
        node = self.head
        while node:
            a.append(node.value)
            node = node.next
        return str(a)

    def push(self,value):
        if self.tail:
            node = Node(value)
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = Node(value)

    def pop(self):
        if self.head:
            v=self.head.value
            self.head = self.head.next
            return v
        else:
            return "Stack is Empty"
        
    def peek(self):
        if self.head:
            return self.head.value
        else:
            return "Stack is Empty"
        
    def isEmpty(self):
        return False if self.head else True
    
    def empty(self):
        self.head = self.tail = None


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q)
print(q.pop())
print(q)
print(q.peek())
print(q.isEmpty())