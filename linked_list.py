#! /usr/bin/env python

class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class linkedlist(object):

    def __init__(self):
        self.head = None
        self.size = 0



    def insertatstart(self, data):
        self.size = self.size + 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode



    def remove(self,data):
        if self.head is None:
            return

        self.size = self.size - 1

        currentNode = self.head
        previousNode = None


        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode



        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode





    def size(self):
        return self.size


    def insertatend(self,data):

        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head


        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode


        actualNode.nextNode = newNode


    def traverselist(self):


        actualNode = self.head


        while actualNode is not None:
            print ("%d" % actualNode.data)

            actualNode = actualNode.nextNode










linklist = linkedlist()


linklist.insertatstart(12)
linklist.insertatstart(16)
linklist.insertatstart(198)
linklist.insertatstart(198)
linklist.insertatstart(198)
linklist.insertatstart(198)
linklist.insertatstart(198)
linklist.insertatstart(198)
linklist.insertatstart(198)
linklist.insertatend(1)
linklist.insertatend(1)
linklist.insertatend(1)
linklist.insertatend(1)


linklist.remove(12)


linklist.traverselist()
