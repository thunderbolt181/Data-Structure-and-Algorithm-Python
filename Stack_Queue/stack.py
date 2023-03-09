class Stack:
    def __init__(self) -> None:
        self.stack=[]

    def __str__(self) -> str:
        return str(self.stack)

    def push(self,value) -> None:
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop() if not self.isEmpty() else "Stack is empty"

    def isEmpty(self) -> bool:
        return True if len(self.stack)==0 else False
    
    def peek(self):
        return self.stack[-1] if not self.isEmpty() else "Stack is empty"
    
    def empty(self):
        self.stack = []
    

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)
print(s.pop())
print(s)
print(s.isEmpty())
print(s.peek())
s.empty()
print(s)