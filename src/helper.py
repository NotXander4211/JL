class TypeError(Exception):
    pass

class MissingArgumentError(Exception):
    pass

class Stack:
    def __init__(self, size):
        self.buf = [0 for _ in range(size)]
        self.pt = -1
    def push(self, value: int):
        self.pt += 1
        self.buf[self.pt] = value
    def pop(self):
        #print(self.buf[self.pt])
        number = int(self.buf[self.pt])
        self.pt -= 1
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

def JumpStatement(statement, top):
    res = False
    args = statement.split(".")
    args[1] = args[1].lower()
    # this is fine bc we only need args[2] for ints for now
    if len(args) >= 3:
        args[2] = int(args[2])
    match args[1]:
            case "eq":
                if top == args[2]:
                    res = True
            case "gt":
                if top >= args[2]:
                    res = True
            case "lt":
                if top <= args[2]:
                    res = True
            case "tr":
                #looks worse but needed bc will always evaluate to true if there is value, same for case "fa"
                if top == True:
                    res = True
            case "fa":
                if top == False:
                    res = True
            case default:
                raise MissingArgumentError("Missing argument for jump statement")
    return res
