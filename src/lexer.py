from helper import Stack, CheckType, JumpStatement, TypeError, MissingArgumentError

debug = False
filen = "./src/test2.jail"

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
        lt[opcode[:-1]] = tc
        continue
    if opcode.startswith("??"):
        #this is a comment ^
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

if not debug:
    print(program)
    print(lt)
    
pc = 0
stack = Stack(256)

while program[pc] != "halt":
    opcode = program[pc]
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
            strL = "STACK: " + str(stack.buf) + " : " + str(stack.vars) + " : " + str(stack.pt)
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
        #print(stack.top())
        if JumpStatement(opcode, theTop):
            pc = lt[program[pc]]
        else:
            pc += 1
    elif opcode == "var":
        stack.pushVar(program[pc], program[pc + 1])
        pc += 2
    else:
        print(opcode + "not implemented yet or not a possible opcode")
        pc += 1