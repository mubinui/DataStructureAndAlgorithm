class Stack:
    def __init__(self):
        self.s = []
        self.length = 0


    def size(self):
        return self.length


    def isEmpty(self):
        flag = False
        if self.length == 0:
            flag = True
        return flag


    def push(self,element):
        if self.length == 0:
            (self.s).append(element)

        else:
            temp = self.s[self.length]
            (self.s).append(element)
            self.s[self.length] = temp

        self.length = self.length + 1

    def pop(self):
        if not self.length == 0:
            


