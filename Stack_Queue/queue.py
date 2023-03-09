class Queue:
    def __init__(self) -> None:
        self.queue=[]

    def __str__(self) -> str:
        return str(self.queue)

    def push(self,value) -> None:
        self.queue.append(value)
    
    def pop(self):
        a = self.queue[0]
        if len(self.queue)>1:
            self.queue = self.queue[1:]
            return a
        elif len(self.queue)==1:
            self.queue = []
            return a
        else:
            return "Queue is Empty"

    def isEmpty(self) -> bool:
        return True if len(self.queue)==0 else False
    
    def peek(self):
        return self.queue[0] if not self.isEmpty() else "Stack is empty"
    
    def empty(self):
        self.stack = []
    

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print(q)
print(q.pop())
print(q)