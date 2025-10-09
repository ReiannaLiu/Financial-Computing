from fc_utils import Tree

class BinaryTree:
    def __init__(self, val, left=None, right=None):
        self._value = val
        self._left = left
        self._right = right
        
    def __str__(self):
        return str(self._convertToTree())
    
    def __repr__(self):
        if self.isLeaf():
            return f'Tree({self.getValue()}, {self.getLeft()}, {self.getRight()})'
        else:
            leftRepr = repr(self.getLeft())
            rightRepr = repr(self.getRight())
            return f'Tree({self.getValue()}, {leftRepr}, {rightRepr})'
    
    def __eq__(self, other):
        if not isinstance(other, BinaryTree):
            return False
        return ((self.getValue() == other.getValue()) and 
                (self.getLeft() == other.getLeft()) and
                (self.getRight() == other.getRight()))
        
    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getValue(self):
        return self._value
    
    def isLeaf(self):
        return (self.getRight() is None) and (self.getLeft() is None)
    
    def _convertToTree(self):
        if self.isLeaf():
            return Tree(self.getValue())
        else:
            leftTree = self.getLeft()
            rightTree = self.getRight()
            children = []
            if leftTree is not None:
                children.append(leftTree._convertToTree())
            if rightTree is not None:
                children.append(rightTree._convertToTree())
            return Tree(self.getValue(), *children)
    
class BST(BinaryTree):
    def __init__(self, value):
        super().__init__(value)
    
    def insert(self, value):
        if value < self.getValue():
            leftTree = self.getLeft()
            if leftTree is None:
                self._left = BST(value)
            else:
                leftTree.insert(value)
        else:
            rightTree = self.getRight()
            if rightTree is None:
                self._right = BST(value)
            else:
                rightTree.insert(value)
        
    
def testBinaryTree():
    t1 = BinaryTree(5)
    t1._left = BinaryTree(3)
    t1._right = BinaryTree(1)
    
    t2 = BinaryTree(5, BinaryTree(3), BinaryTree(1))
    
    assert(t1 == t2)
    assert(t1 != BinaryTree(5))
    assert(t1 != BinaryTree(5, BinaryTree(3)))

def testBST():
    t1 = BST(5)
    t1.insert(3)
    t1.insert(1)
    t1.insert(7)

testBinaryTree()
testBST()