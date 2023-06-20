class BinaryTree(object):
    def __init__(self, rootObj) -> None:
        self.key = rootObj
        self.leftNode = None
        self.rightNode = None
    
    def insertLeft(self, newObj):
        if self.leftNode == None:
            self.leftNode = BinaryTree(newObj)
        else:
            t = BinaryTree(newObj)
            t.leftNode = self.leftNode
            self.leftNode = t
    
    def insertRight(self, newObj):
        if self.rightNode == None:
            self.rightNode = BinaryTree(newObj)
        else:
            t = BinaryTree(newObj)
            t.rightNode = self.rightNode
            self.rightNode = t
    
    def getRootVal(self):
        return self.key
    
    def setRootVal(self,newRootVal):
        self.key = newRootVal

    def getLeftNode(self):
        return self.leftNode
    
    def setLeftNode(self, newLeftNode):
        self.leftNode = newLeftNode

    def getRightNode(self):
        return self.rightNode
    
    def setRightNode(self, newRightNode):
        self.rightNode = newRightNode

def preOrder(tree):
    if tree:
        print(tree.getRootVal())
        preOrder(tree.getLeftNode())
        preOrder(tree.getRightNode())

def inOrder(tree):
    if tree:
        inOrder(tree.getLeftNode())
        print(tree.getRootVal())
        inOrder(tree.getRightNode())

def postOrder(tree):
    if tree:
        postOrder(tree.getLeftNode())
        postOrder(tree.getRightNode())
        print(tree.getRootVal())

b = BinaryTree('a')
b.insertLeft('b')
b.insertRight('c')

preOrder(b)
print()
inOrder(b)
print()
postOrder(b)
