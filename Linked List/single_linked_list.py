class Node:
    def __init__(self,value,next=None) -> None:
        self.value = value
        self.next = next

class SlinkedList:
    def __init__(self, head) -> None:
        self.head = head

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def insert(self,value,location=-1):
        if self.head == None:self.head = Node(value)
        node = self.head
        if location==0:
            self.head = Node(value,self.head)
        else:
            loc = 1
            while node.next and loc!=location:
                node = node.next
                loc+=1
            node.next = Node(value,node.next)

    def delete(self,value):
        node = self.head
        prev = None
        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.head = self.head.next
                del node
                return "Delete Successful"
            prev = node
            node = node.next
        else:
            return "Value not found"

    def search(self, value):
        node = self.head
        pos = 1
        while node:
            if node.value == value:
                return f"The value {value} is at {pos} position"
            pos+=1
            node = node.next
        else:
            return "The value does not exists."
        
    def del_list(self):
        del self.head # Garbase collector will delete all the the non referenced nodes.


node1 = Node(1)
s = SlinkedList(node1)
s.insert(5)
s.insert(51)
s.insert(25)
s.insert(2,2)

print([node for node in s])

print(s.search(51))

print(s.delete(1))

s.insert(15,1)

print([node for node in s])

s.del_list()

print([node for node in s])

    