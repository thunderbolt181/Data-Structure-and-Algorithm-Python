class binaryTree:
    def __init__(self,size) -> None:
        self.tree = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insert(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The Binary Tree is full."
        self.tree[self.lastUsedIndex+1] = value
        self.lastUsedIndex+=1

    def search(self,value):
        for i in range(1,self.maxSize):
            if i == value:
                return "Value found at index" + str(i)
        else:
            return "Value does not exists"
        
    def preOrderTraversal(self, index=1):
        if index>=self.maxSize or self.tree[index]==None:
            return 
        else:
            print(self.tree[index])
            self.preOrderTraversal(index=2*index)
            self.preOrderTraversal(index=((index*2)+1))

    def inOrderTraversal(self,index = 1):
        if index>=self.maxSize or self.tree[index]==None:
            return
        else:
            self.inOrderTraversal(index=2*index)
            print(self.tree[index])
            self.inOrderTraversal(index=((index*2)+1))

    def postOrderTraversal(self,index=1):
        if index>=self.maxSize or self.tree[index]==None:
            return
        else:
            self.postOrderTraversal(index=2*index)
            self.postOrderTraversal(index=((index*2)+1))
            print(self.tree[index])

bt = binaryTree(8)
bt.insert("Drinks")
bt.insert("Hot")
bt.insert("Cold")
bt.insert("Tee")
bt.insert("Coffee")
bt.insert("Cola")
bt.insert("Fanta")

print(bt.tree)
bt.postOrderTraversal()
