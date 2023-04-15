class treeNode:
    def __init__(self, value, right = None, left = None) -> None:
        self.value = value
        self.right = right
        self.left = left

class binarySearchTree:
    def __init__(self, Node = None) -> None:
        self.root = Node

    def insert(self, value):
        if not self.root:
            self.root = treeNode(value)
        else:
            node = self.root
            while node:
                if node.value >= value:
                    if node.left == None:
                        node.left = treeNode(value)
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = treeNode(value)
                        break
                    else:
                        node = node.right

    def search(self,value):
        def findValue(node):
            if node == None:
                return False
            if node.value == value:
                return True
            if not findValue(node.left):
                return findValue(node.right)
            else: return True

        return findValue(self.root)

    def printTree(self):
        def preOrderTraversal(node,value):
            if node == None:
                return
            print(node.value,value)
            preOrderTraversal(node.left,value+1)
            preOrderTraversal(node.right,value+1)


        preOrderTraversal(self.root,0)


def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    else:
        if value < rootNode.value:
            rootNode.left = deleteNode(rootNode.left,value)
        elif value > rootNode.value:
            rootNode.right = deleteNode(rootNode.right,value)
        else:
            if rootNode.left is None:
                temp = rootNode.right
                rootNode = None
                print("delete successful")
                return temp
            elif rootNode.right is None:
                temp = rootNode.left
                rootNode = None
                return temp
            
            minNode = minValueNode(rootNode.right)
            rootNode.value = minNode.value
            rootNode.right = deleteNode(rootNode.right,minNode.value)
    return rootNode                

bst = binarySearchTree(treeNode(70))
nodes = [50,90,30,60,20,40,80,100,85,86,83]
for i in nodes:
    bst.insert(i)
# bst.printTree()

# print(bst.search(50))
# print(bst.search(110))

print(deleteNode(bst.root, 70))
bst.printTree()