class Node:
    def __init__(self,value,next = None) -> None:
        self.value = value
        self.next = next

class CSLinkedList:
    def __init__(self,head: Node) -> None:
        self.head = self.tail = head
        self.head.next = self.head

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next 
            if node == self.head:
                break

    def insert(self,value,location=-1):
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif location == -1:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail = newNode
        else:
            node = self.head
            loc = 1
            while node.next!=self.head and loc != location :
                node = node.next
                loc+=1
            nextNode = node.next
            node.next = newNode
            newNode.next = nextNode

    def search(self,value):
        node = self.head
        index = 0
        while node.value!=value:
            node = node.next
            index+=1
            if node.next == self.head:
                break
        else:
            return f"The value {value} is at index {index}"
        return f"The value {value} does not exists"
    
    def delete(self,value):
        node = self.head
        prev = self.tail
        while node.value!= value:
            node = node.next
            prev = prev.next
            if node == self.head:
                break
        else:
            if node == self.head:
                self.tail.next = node.next
                self.head = node.next
                del node
            elif node == self.tail:
                prev.next = self.head
                self.tail = prev
                del node
            else:
                prev.next = node.next
                del node
            return "deleted Succeccfully"
        return "Value cannot be found"
    
    def delete_list(self):
        self.head = None
        self.tail = None
        self.tail.next=None

cl = CSLinkedList(Node(1))

cl.insert(2)
cl.insert(3,0)
cl.insert(4)
cl.insert(5,3)
cl.insert(6)

print([node for node in cl])

print(cl.search(7))

print(cl.delete(3))

print([node for node in cl])

cl.delete_list()

print([node for node in cl])