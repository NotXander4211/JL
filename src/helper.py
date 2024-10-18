class TypeError(Exception):
    pass

class MissingArgumentError(Exception):
    pass

class RestrictedUse(Exception):
    pass

class OpcodeException(Exception):
    pass

EXCEPTIONS = {"TE":TypeError, "MAE":MissingArgumentError, "RU":RestrictedUse, "OE":OpcodeException}

class RuleSetConfigs:
    def __init__(self, ss: int, vs: bool, db: bool):
        self.rules = {}
        self.rules["ss"] = ss
        self.rules["vs"] = vs
        self.rules["db"] = db
    def getVal(self, val):
        return self.rules.get(val, None)
    def setVal(self, key, val):
        self.rules[key] = val

class Stack:
    def __init__(self, size, vars):
        self.varUse = False
        if vars:
            self.vars = {}
            self.varUse = True
        self.buf = [0 for _ in range(size)]
        self.pt = -1
    def push(self, value: int):
        self.pt += 1
        self.buf[self.pt] = value
    def pop(self):
        #print(self.buf[self.pt])
        val = self.buf[self.pt]
        self.pt -= 1
        return val
    def top(self):
        return self.buf[self.pt]
    def pushVar(self, var, value):
        if self.varUse:
            self.vars[var] = value
        else:
            raise RestrictedUse("VS was not set to True, variable stack was not created")
    def getVar(self, var):
        if self.varUse:
            return self.vars[var]
        raise RestrictedUse("VS was not set to True, variable stack was not created")

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
            case _:
                raise MissingArgumentError("Missing argument for jump statement")
    return res

def sendDebug(msg, rs: RuleSetConfigs): # rs = rule set
    if rs.getVal("db"):
        print(msg)