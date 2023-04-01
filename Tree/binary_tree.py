from do_not_delete import Queue

class TreeNode:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, node) -> None:
        self.root = node

    # Pre, In, Post order traversal comes under Depth first search (DFS)
    def preOrderTraversal(self,rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.left)
        self.preOrderTraversal(rootNode.right)

    def inOrderTraversal(self,rootNode):
        if not rootNode:
            return
        self.inOrderTraversal(rootNode.left)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.right)

    def postOrderTraversal(self,rootNode):
        if not rootNode:
            return
        self.postOrderTraversal(rootNode.left)
        self.postOrderTraversal(rootNode.right)
        print(rootNode.data)

    # level order traversal comes in Breath First Search (BFS)

    def levelOrderTraversal(self,rootNode):
        if not rootNode:
            return
        else:
            customQueue = Queue()
            customQueue.push(rootNode)
            while not(customQueue.isEmpty()):
                root = customQueue.pop()
                print(root.data)
                if (root.left is not None):
                    customQueue.push(root.left)
                if (root.right is not None):
                    customQueue.push(root.right)

    # Searching in Binary Tree
    def searchBT(self,value,root):
        if root == None:
            return False
        elif root.data == value:
            return True
        return True if self.searchBT(value,root.left) or self.searchBT(value,root.right) else False

    def insert(self,newNode,rootNode):# using level order traversing
        if not rootNode:
            rootNode = newNode
        else:
            customQueue = Queue()
            customQueue.push(rootNode)
            while not (customQueue.isEmpty()):
                root = customQueue.pop()
                if root.left is None:
                    root.left = newNode
                    return "Successful"
                else:
                    customQueue.push(root.left)
                if root.right is None:
                    root.right = newNode
                    return "Successful"
                else:
                    customQueue.push(root.right)

    def getDeepestNode(self, rootNode):
        if not rootNode:
            return
        else:
            customQueue = Queue()
            customQueue.push(rootNode)
            while not(customQueue.isEmpty()):
                root = customQueue.pop()
                if (root.left is not None):
                    customQueue.push(root.left)
                if (root.right is not None):
                    customQueue.push(root.right)
            return root

    def deleteTree(self):
        if self.root:
            self.root.right = None
            self.root.left = None
            self.root = None


drinks = TreeNode("Drinks")
tree = BinaryTree(drinks)
cold = TreeNode("Cold")
hot = TreeNode("Hot")
drinks.left = cold
drinks.right = hot
tee = TreeNode('tee')
coffee = TreeNode('Coffee')
cola = TreeNode('Cola')
fanta = TreeNode('Fanta')
cold.left=cola
cold.right=fanta
hot.left=tee
hot.right=coffee

print(tree.searchBT('hot',tree.root))
print(tree.insert(TreeNode("something"),tree.root))

# tree.preOrderTraversal(tree.root)
# tree.levelOrderTraversal(tree.root)
# tree.inOrderTraversal(tree.root)
# tree.postOrderTraversal(tree.root)