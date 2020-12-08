with open("input_day8.txt") as f:
    boot_code = f.readlines()

def do_acc(value):
    global acc, instruction
    acc += value
    instruction += 1

def do_jmp(value):
    global instruction
    instruction += value

def do_nop(value):
    global instruction
    instruction += 1

# Part one
acc = 0
instruction = 0
commands = {'acc': do_acc, 'jmp': do_jmp, 'nop': do_nop}
hashInstruction = set()

while(True):
    if(instruction in hashInstruction):
        break
    hashInstruction.add(instruction)
    operation, argument = boot_code[instruction].strip().split(" ")
    commands[operation](int(argument))

print(acc)

# Part two
acc = 0
instruction = 0
commands = {'acc': do_acc, 'jmp': do_jmp, 'nop': do_nop}
hashInstruction = set()
hashInstructionChanged = set()
cahngeOperation = True

while(True):
    if instruction >= len(boot_code):
        print("Boot finished")
        break
    if instruction in hashInstruction:
        acc = 0
        instruction = 0
        hashInstruction = set()
        cahngeOperation = True
    hashInstruction.add(instruction)
    operation, argument = boot_code[instruction].strip().split(" ")
    if cahngeOperation and operation != 'acc':
        if instruction not in hashInstructionChanged:
            hashInstructionChanged.add(instruction)
            if operation == 'jmp':
                operation = 'nop'
            else:
                operation = 'jmp'
            cahngeOperation = False

    commands[operation](int(argument))

print(acc)