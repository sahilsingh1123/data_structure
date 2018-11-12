class Node(object):

    def __init__(self, data):
        self.data = data 
        self.height = 0
        self.leftchild = None
        self.rightchild = None

    
class AVL(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertnode(data, self.root)



    def insertnode(self, data, node):

        if not node:
            return Node(data)
        
        if data < node.data:
            node.leftchild = self.insertnode(data, node.leftchild)
        
        else:
            node.rightchild = self.insertnode(data, node.rightchild)

        node.height = max(self.calheight(node.leftchild), self.calheight(node.rightchild)) + 1

        return self.settleviolation(data, node)


    def settleviolation(self, data, node):

        balance = self.calcbalance(node)

        # case 1 -> left left heavy situation--right rotation

        if balance > 1 and data < node.leftchild.data:
            print("left left heavy situation..") 
            return self.rotateright(node)


        # case 2 --> right right heavy--> left rotate

        if balance < -1 and data > node.rightchild.data:
            print("right right havy situattion..")
            return self.rotateleft(node)


        # case 3... left and right heavy.. both roataion need to perform

        if balance > 1 and data > node.leftchild.data:
            print("left-right heavy situation")
            node.leftchild = self.rotateleft(node.leftchild)
            return self.rotateright(node)

        # case 4 right-left heavy situation...

        if balance < -1 and data < node.rightchild.data:
            print("right-left situation...")
            node.rightchild = self.rotateright(node.rightchild)
            return self.rotateleft(node)

        return node

    def traverse(self):
        if self.root:
            self.traverseinorder(self.root)

    def traverseinorder(self, node):

        if node.leftchild:
            self.traverseinorder(node.leftchild)

        print(node.data)

        if node.rightchild:
            self.traverseinorder(node.rightchild)





    def calheight(self, node):

        if not node:
            return -1

        return node.height

    #if returns > 1 means left heavy tree
    #-----------< -1 -----right heavy tree- left rotation

    def calcbalance(self, node):

        if not node:
            return 0

        return self.calheight(node.leftchild) - self.calheight(node.rightchild)

    def rotateright(self, node):

        print("rotating to right...", node.data)

        templeftchild = node.leftchild
        t = templeftchild.rightchild

        templeftchild.rightchild = node
        node.leftchild = t

        node.height = max(self.calheight(node.leftchild), self.calheight(node.rightchild)) + 1
        templeftchild.height = max(self.calheight(templeftchild.leftchild), self.calheight(templeftchild.rightchild)) + 1

        return templeftchild


    def rotateleft(self, node):

        print("rotating to left...", node.data)

        temprightchild = node.rightchild
        t = temprightchild.leftchild

        temprightchild.leftchild = node
        node.rightchild = t

        node.height = max(self.calheight(node.leftchild), self.calheight(node.rightchild)) + 1
        temprightchild.height = max(self.calheight(temprightchild.leftchild), self.calheight(temprightchild.rightchild)) + 1

        return temprightchild



avl = AVL()

avl.insert(10)
avl.insert(4)
avl.insert(5)
avl.insert(15)
avl.insert(12)
avl.insert(20)

avl.traverse()