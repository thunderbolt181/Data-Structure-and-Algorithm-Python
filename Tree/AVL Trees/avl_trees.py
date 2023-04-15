
class AvlTreeNode:
    def __init__(self, value):
        self.value  = value
        self.left = None
        self.right = None
        self.height = 1

def printHelper(currPtr, indent, last):
    import sys
    if currPtr != None:
        sys.stdout.write(indent)
        if last:
            sys.stdout.write("R----")
            indent += "     "
        else:
            sys.stdout.write("L----")
            indent += "|    "
        print(currPtr.value)
        printHelper(currPtr.left, indent, False)
        printHelper(currPtr.right, indent, True)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraversal(rootNode.left)
    preOrderTraversal(rootNode.right)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.left)
    print(rootNode.value)
    inOrderTraversal(rootNode.right)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.left)
    postOrderTraversal(rootNode.right)
    print(rootNode.value)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = []
        customQueue.append(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.pop(0)
            print(root.value)
            if (root.left is not None):
                customQueue.append(root.left)
            if (root.right is not None):
                customQueue.append(root.right)

def searchNode(node, value):
    if node.value == value:
        return True
    elif value < node.value:
        if node.left is None:
            return False
        else:
            return searchNode(node.left,value)
    else:
        if node.right is None:
            return False
        else:
            return searchNode(node.right, value)
        
def getHeight(node):
    if not node:
        return 0
    return node.height

def rightRotate(node):
    newRoot = node.left
    node.left = newRoot.right
    newRoot.right = node
    node.height = 1+max(getHeight(node.left),getHeight(node.right))
    newRoot.height = 1+max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot

def leftRotate(node):
    newRoot = node.right
    node.right = newRoot.left
    newRoot.left = node
    node.height = 1+max(getHeight(node.left),getHeight(node.right))
    newRoot.height = 1+max(getHeight(newRoot.left),getHeight(newRoot.right))
    return newRoot

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def insert(node,value):
    if not node:
        return AvlTreeNode(value)
    elif value > node.value:
        node.right = insert(node.right,value)
    else:
        node.left = insert(node.left, value)

    node.height = 1+max(getHeight(node.left),getHeight(node.right))

    balance = getBalance(node)
    if balance > 1:
        if value < node.left.value:
            return rightRotate(node)
        else:
            node.left = leftRotate(node.left)
            return rightRotate(node)
    if balance < -1:
        if value > node.right.value:
            return leftRotate(node)
        else:
            node.right = rightRotate(node.right)
            return leftRotate(node)
    return node

def minimunValue(node):
    current = node.right
    while current.left:
        current = current.left
    return current

def deleteNode(root, value):
    if not root:
        return root
    elif value < root.value:
        root.left = deleteNode(root.left, value)
    elif value > root.value:
        root.right = deleteNode(root.right, value)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        if root.right is None:
            temp = root.left
            root = None
            return temp

        minValueNode = minimunValue(root)
        root.value = minValueNode.value
        root.right = deleteNode(root.right, minValueNode.value)

    balance = getBalance(root)
    if balance > 1:
        if value < node.left.value:
            return rightRotate(node)
        else:
            node.left = leftRotate(node.left)
            return rightRotate(node)
    if balance < -1:
        if value > node.right.value:
            return leftRotate(node)
        else:
            node.right = rightRotate(node.right)
            return leftRotate(node)
    return root

    

values = [30,25,35,20,10,15,5,50,60,70,65]
avl = None
for i in values:
    avl = insert(avl,i)
printHelper(avl, "",True)
deleteNode(avl, 65)
deleteNode(avl, 50)
printHelper(avl, "",True)