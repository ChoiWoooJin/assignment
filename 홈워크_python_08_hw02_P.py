class Stack:
    
    def __init__(self):
        self.lis = []
        
    def empty(self):
        if len(self.lis) == 0:
            return True
        else:
            return False
    
    def top(self):
        return self.lis[-1]
    
    def pop(self):
        if len(self.lis) != 0:
            return self.lis.pop(-1)
        else:
            return False

    def push(self,data):
        self.lis = self.lis.append(data)
    
    def __repr__(self):
        return str(self.lis)


    
        