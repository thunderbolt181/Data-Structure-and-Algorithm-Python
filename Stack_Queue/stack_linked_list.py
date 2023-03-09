class Node:
    def __init__(self,value,n=None) -> None:
        self.value = value
        self.next = n

class Stack:
    def __init__(self,node = None) -> None:
        self.head = node

    def __str__(self) -> str:
        a = []
        node = self.head
        while node:
            a.append(node.value)
            node = node.next
        return str(a)

    def push(self,value):
        if self.head:
            node = Node(value,self.head)
            self.head = node
        else:
            self.head = Node(value)

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
        self.head = None


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)
print(s.pop())
print(s)
print(s.peek())
print(s.isEmpty())