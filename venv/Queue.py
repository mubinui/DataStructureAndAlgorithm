class Queue:
    def __init__(self):
        self.x = []
        self.front = -1
        self.rear = -1
        self.Size = 0
       


    def isEmpty(self):
        flag = False
        if self.Size == 0 :
            flag = True

        return flag


    def enqueue(self,elem):
        if  self.Size == 0:
            (self.x).append(elem)
            self.front = 0
            self.rear = 0

        else:
            (self.x).append(elem)
            self.rear = self.rear + 1

        self.Size = self.Size + 1

        
    
    def dequeue(self):
        if not self.Size == 0:
            removedElem = self.x[self.front]
            self.x[self.front] = None
            self.Size = self.Size - 1
            self.front = self.front + 1
            return removedElem


    def size(self):
        return self.Size



    def peek (self):
        return self.Size


    def printList(self):
        for i in self.x:
            if not i == None :
                print(i,end='->')
