class Node(object):

    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


class Binarysearchtree(object):

    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if data < node.data:
            if node.leftchild:
                self.insertNode(data, node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data, node.rightchild)
            else:
                node.rightchild = Node(data)
    

    def getminvalue(self):
        if self.root:
            return self.getmin(self.root)
    
    def getmin(self ,node):
        if node.leftchild:
            return self.getmin(node.leftchild)
        
        return node.data
    
    def getmaxvalue(self):
        if self.root:
            return self.getmax(self.root)
    
    def getmax(self, node):
        if node.rightchild:
            return self.getmax(node.rightchild)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseinorder(self.root)
            self.traversepreorder(self.root)
            self.traversepostorder(self.root)

    def traverseinorder(self, node):
        if node.leftchild:
            self.traverseinorder(node.leftchild)
        
        print(node.data)

        if node.rightchild:
            self.traverseinorder(node.rightchild)



    def traversepreorder(self, node):
        print node.data

        if node.leftchild:
            self.traversepreorder(node.leftchild)

        if node.rightchild:
            self.traversepreorder(node.rightchild)    



    def traversepostorder(self, node):
        if node.leftchild:
            self.traversepostorder(node.leftchild)
        
        if node.rightchild:
            self.traversepostorder(node.rightchild)

        print node.data





    def remove(self,data):
        if self.root:
            self.root = self.removenode(data, self.root)

    def removenode(self, data, node):

        if not node:
            return node
        
        if data < node.data:
            node.leftchild = self.removenode(data, node.leftchild)
        elif data > node.data:
            node.rightchild = self.removenode(data, node.rightchild)
        
        else:

            if not node.leftchild and not node.rightchild:
                print("removing a leaf node..")
                del node
                return None

            if not node.leftchild:
                print("removing a node with single/only right child..")
                tempNode = node.rightchild
                del node
                return tempNode

            elif not node.rightchild:
                print("removing a node with single left child..")
                tempNode = node.leftchild
                del node
                return tempNode
            

            print("removing node with two children..")
            tempNode = self.getpredecessor(node.leftchild)
            node.data = tempNode.data
            node.leftchild = self.removenode(tempNode.data, node.leftchild)

        return node
    
    def getpredecessor(self, node):
        if node.rightchild:
            return self.getpredecessor(node.rightchild)

        return node







bst = Binarysearchtree()

bst.insert(10)
bst.insert(4)
bst.insert(5)
bst.insert(15)
bst.insert(12)
bst.insert(20)
#bst.remove(4)
print("min value is ",bst.getminvalue())
print("max value is ",bst.getmaxvalue())

bst.traverse()

