import sys
from helper import Stack, RuleSetConfigs, CheckType, JumpStatement, TypeError, MissingArgumentError

# types: int, str, bool, list
# comment: ??
# #JL for commands
# #JL@ for other commands 
# #JL@SS size<int>
# use that for stack size
# --not in bytes, in length of the stack<list>--
#default is 256 

debug = False
Ruleset = RuleSetConfigs(256, False)
filen = "./src/test.jail"
if len(sys.argv) >= 2:
    filen = sys.argv[1]

programL = []
with open(filen, "r") as file:
    programL = [line.strip() for line in file.readlines()]

program = []
tc = 0
lt = {}
for line in programL:
    args = line.split(" ")
    opcode = args[0].lower()

    if opcode == "":
        continue
    if opcode.endswith(":"):
        lt[opcode[:-1]] = tc+1
        continue
    if opcode.startswith("??"):
        #this is a comment ^
        continue
    # deal with #JL,  #JL@ for commands
    if opcode.startswith("#jl"):
        if debug:
            print("--Lexer: startswith #JL")
        permutator = opcode[3]
        cmd = opcode[4:]
        if permutator == "@": 
            if debug:
                print("--Lexer: " + cmd.lower())
            match cmd.lower():
                case "ss":         
                    Ruleset.setVal("ss", int(args[1]))
                case "ivs":
                    Ruleset.setVal("vs", True)
                case "evs":
                    Ruleset.setVal("vs", False)
        elif permutator == "!":
            match cmd.lower():
                case "db":
                    print("Debug Active")
                    debug = True
        
        continue

    program.append(opcode)
    tc += 1
    if opcode == "push":
        #should give variable for now its only numbers(int)
        type_ = args[1]
        var = args[2]
        match type_.lower():
            case "int":
                program.append(int(var))
            case "str":
                program.append(str(var))
            case "bool":
                if var.lower() == "true":
                    program.append(True)
                else:
                    program.append(False)
            case "list":
                var = var.split(",")
                for i in var:
                    var[i] = var[i].strip()
                program.append(var)
            case "var":
                program.append("_var_")
                program.append(str(var))
        tc += 1
    if opcode == "print":
        if args[1].lower() == "__top__":
            stringL = "__top__"
        elif args[1].lower() == "__stack__":
            stringL = "__stack__"
        elif args[1].lower() == "__var_stack__":
            stringL = "__var_stack__"
        else:
            stringL = " ".join(args[1:])[1:-1]
        program.append(stringL)
        tc += 1
    if opcode.startswith("jump"):
        label = args[1].lower()
        program.append(label)
        tc += 1
    if opcode == "var":
        type_ = args[1]
        var = args[3]
        varName = args[2]
        program.append(varName)
        tc += 1
        match type_.lower():
            case "int":
                program.append(int(var))
            case "str":
                program.append(str(var))
            case "bool":
                if var.lower() == "true":
                    program.append(True)
                else:
                    program.append(False)
            case "list":
                var = var.split(",")
                for i in var:
                    var[i] = var[i].strip()
                program.append(var)
        tc += 1
    

if debug:
    print("--Std Printer: ", program)
    print("--Std Printer: ", lt)
    
pc = 0
stack = Stack(Ruleset.getVal("ss"), Ruleset.getVal("vs"))

while program[pc] != "halt":
    opcode = program[pc]
    if debug:
        print("--Runner: " + opcode)
    pc += 1
    if opcode == "push":
        if program[pc] == "_var_":
            pc += 1
            stack.push(stack.getVar(program[pc]))
            pc += 1
        else:
            stack.push(program[pc])
            pc += 1
    elif opcode == "pop":
        #will NOT save the value
        stack.pop()
    elif opcode == "read":
        num = int(input(""))
        stack.push(num)
    elif opcode == "print":
        if program[pc] == "__top__":
            strL = "TOP: " + str(stack.top())
        elif program[pc] == "__stack__":
            strL = "STACK: " + str(stack.buf) + " : " + str(stack.pt)
        elif program[pc] == "__var_stack__":
            strL = f"Var Stack: {str(stack.vars)}"
        else:
            strL = program[pc]
        print(strL)
        pc += 1
    elif opcode == "add":
        a = stack.pop()
        b = stack.pop()
        if CheckType(a, b, int, int):
            stack.push(a + b)
        else:
            raise TypeError("Top 2 variables in the stack are both not Type int")
    elif opcode.startswith("jump"):
        theTop = stack.top()
        if debug:
            print("--Runner 'jump' opcode: ", type(stack.top()))
        if JumpStatement(opcode, theTop):
            pc = lt[program[pc]]
        else:
            pc += 1
    elif opcode == "var":
        stack.pushVar(program[pc], program[pc + 1])
        pc += 2
    else:
        print(opcode + "not implemented yet or not a possible opcode!")
        pc += 1