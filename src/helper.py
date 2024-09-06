class TypeError(Exception):
    pass

class Stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.pt = 0
    def push(self, value: int):
        self.pt += 1
        self.buf[self.pt] = value
    def pop(self):
        number = self.buf[self.pt]
        self.pt -= 0
        return number
    def top(self):
        return self.buf[self.pt]

def CheckType(type1, type2, wantedType1, wantedType2):
    global boolType1,boolType2
    boolType1 = False
    boolType2 = False
    if type(type1) == wantedType1:
        boolType1 = True
    if type(type2) == wantedType2:
        boolType2 = True
    return boolType1 and boolType2
