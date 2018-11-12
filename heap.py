class Heap(object):

    HEAP_SIZE = 10

    def __init__(self):
        self.heap = [0]*Heap.HEAP_SIZE
        self.currentposition = -1
    
    def insert(self, item):
        if self.isFull():
            print("heap is full..")
            return

        self.currentposition = self.currentposition + 1
        self.heap[self.currentposition] = item
        self.fixup(self.currentposition)

    def fixup(self, index):

        parentindex = int((index-1)/2)

        while parentindex >= 0 and self.heap[parentindex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentindex]
            self.heap[parentindex] = temp
            parentindex = int((index -1)/2)

    def heapsort(self):

        for i in range(0, self.currentposition+1):
            temp = self.heap[0]
            print(temp)

            self.heap[0] = self.heap[self.currentposition-i]
            self.heap[self.currentposition-i] = temp
            self.fixdown(0, self.currentposition-i-1)

    def fixdown(self, index, upto):
        while index <= upto:

            leftchild = 2*index+1
            rightchild = 2*index+2

            if leftchild < upto:
                childtoswap = None

                if rightchild > upto:
                    childtoswap = leftchild
                else:
                    if self.heap[leftchild] > self.heap[rightchild]:
                        childtoswap = leftchild
                    else:
                        childtoswap = rightchild

                if self.heap[index] < self.heap[childtoswap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[childtoswap]
                    self.heap[childtoswap] = temp

                else:
                    break

                index = childtoswap
            else:
                break

    def isFull(self):
        if self.currentposition == Heap.HEAP_SIZE:
            return True
        else:
            return False


if __name__ == "__main__":

    HEap = Heap()

    HEap.insert(10)
    HEap.insert(-23)
    HEap.insert(15)
    HEap.insert(1)
    HEap.insert(-90)

    HEap.heapsort()