import sys
from helper import EXCEPTIONS
from helper import sendDebug
from helper import Stack, RuleSetConfigs, CheckType, JumpStatement

# types: int, str, bool, list
# comment: ??
# #OL for commands
# #OL@ for other commands 
# #OL@SS size<int>
# use that for stack size
# --not in bytes, in length of the stack<list>--
#default is 256 
#All commands are run during the lexing

Ruleset = RuleSetConfigs(ss=256, vs=False)
filen = "./src/prog/test.ol"
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
    sendDebug(opcode, Ruleset)

    if opcode == "":
        sendDebug("blank line cont", Ruleset)
        continue
    if opcode.endswith(":"):
        lt[opcode[:-1]] = tc+1
        sendDebug("label':' cont", Ruleset)
        continue
    if opcode.startswith("??"):
        #this is a comment ^
        print("??comp")
        continue
    # deal with #OL,  #OL@ for commands
    if opcode.startswith("#ol"):
        sendDebug("--Lexer: startswith #ol", Ruleset)
        permutator = opcode[3]
        cmd = opcode[4:]
        if permutator == "@": 
            sendDebug("--Lexer: " + cmd.lower(), Ruleset)
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
                    Ruleset.setVal("db", True)
        
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
    

sendDebug(f"--Std Printer: {program}", Ruleset)
sendDebug(f"--Std Printer: {lt}", Ruleset)
    
pc = 0
stack = Stack(Ruleset.getVal("ss"), Ruleset.getVal("vs"))

while program[pc] != "halt":
    opcode = program[pc]
    sendDebug(f"--Runner: {opcode}", Ruleset)
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
            raise EXCEPTIONS["TE"]("Top 2 variables in the stack are both not Type int")
    elif opcode.startswith("jump"):
        theTop = stack.top()
        sendDebug(f"--Runner 'jump' opcode: {type(stack.top())}", Ruleset)
        if JumpStatement(opcode, theTop):
            pc = lt[program[pc]]
        else:
            pc += 1
    elif opcode == "var":
        stack.pushVar(program[pc], program[pc + 1])
        pc += 2
    else:
        pc += 1
        raise EXCEPTIONS["OE"](opcode + "not implemented yet or not a possible opcode!")