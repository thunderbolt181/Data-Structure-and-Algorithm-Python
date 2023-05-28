class Heap:
    def __init__(self, size):
        self.customList = (size+1)*[None]
        self.heapSize = 0
        self.maxSize = size + 1

def peakOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrdedTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])

def heapifyInsertion(rootNode,index,heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            rootNode.customList[index],rootNode.customList[parentIndex] = rootNode.customList[parentIndex],rootNode.customList[index]
        heapifyInsertion(rootNode, parentIndex, heapType)
    elif heapType == "Max":
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            rootNode.customList[index],rootNode.customList[parentIndex] = rootNode.customList[parentIndex],rootNode.customList[index]
        heapifyInsertion(rootNode, parentIndex, heapType)

def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize+1] = nodeValue
    rootNode.heapSize += 1
    heapifyInsertion(rootNode, rootNode.heapSize, heapType)
    return "The Value has been successfully inserted."

heap = Heap(5)
insertNode(heap,4,"Max")
insertNode(heap,5,"Max")
insertNode(heap,2,"Max")
insertNode(heap,1,"Max")
# insertNode(heap,4,"Max")
levelOrdedTraversal(heap)