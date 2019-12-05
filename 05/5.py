I = list(map(int, open('5.in').read().strip().split(',')))

end = False

i = 0
while not end:
    instr = str(I[i]).rjust(5, '0')
    opcode = instr[-2:]

    if opcode == '01':
        a = I[i+1] if int(instr[-3]) else I[I[i+1]]
        b = I[i+2] if int(instr[-4]) else I[I[i+2]]

        I[I[i+3]] = a + b
        i += 4

    elif opcode == '02':
        a = I[i+1] if int(instr[-3]) else I[I[i+1]]
        b = I[i+2] if int(instr[-4]) else I[I[i+2]]

        I[I[i+3]] = a * b
        i += 4

    elif opcode == '03':
# Part 1 ID=1
#        I[I[i+1]] = 1
# Part 2 ID=5
        I[I[i+1]] = 5
        i += 2

    elif opcode == '04':
        print(I[I[i+1]])
        i += 2

    elif opcode == '05':
        a = I[i+1] if int(instr[-3]) else I[I[i+1]]
        b = I[i+2] if int(instr[-4]) else I[I[i+2]]

        i = b if a else i+3

    elif opcode == '06':
        a = I[i+1] if int(instr[-3]) else I[I[i+1]]
        b = I[i+2] if int(instr[-4]) else I[I[i+2]]

        i = b if not a else i+3

    elif opcode == '07':
        a = I[i+1] if int(instr[-3]) else I[I[i+1]]
        b = I[i+2] if int(instr[-4]) else I[I[i+2]]

        I[I[i+3]] = 1 if a < b else 0
        i += 4

    elif opcode == '08':
        a = I[i+1] if int(instr[-3]) else I[I[i+1]]
        b = I[i+2] if int(instr[-4]) else I[I[i+2]]

        I[I[i+3]] = 1 if a == b else 0
        i += 4

    elif opcode == '99':
        end = True
