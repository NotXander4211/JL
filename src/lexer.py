import constants

filen = "./src/test.jail"

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
    
    program.append(opcode)
    tc += 1
    if opcode == "push":
        #should give variable for now its only numbers(int)
        num = int(args[1])
        program.append(num)
        tc += 1
    if opcode == "print":
        stringL = " ".join(args[1:])
        program.append(stringL)
        tc += 1
    if opcode == "jump.eq.0":
        label = args[1].lower()
        program.append(label)
        tc += 1
        
print(program)
print(lt)

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
    
pc = 0
stack = Stack(256)

while program[pc] != "halt":
    opcode = program[pc]
    pc += 1
    if opcode == "push":
        print("printp")
        stack.push(program[pc])
        pc += 1
    elif opcode == "read":
        num = int(input(""))
        stack.push(num)
    elif opcode == "print":
        print("print")
        strL = program[pc]
        print(strL)
        pc += 1
    elif opcode == "add":
        a = stack.pop()
        b = stack.pop()
        stack.push(a + b)
    elif opcode == "jump.eq.0":
        print("prinwet")
        num = stack.top()
        print(stack.top())
        if num == 0:
            pc = lt[program[pc]]
        else:
            pc += 1