prog = list(map(int, open('9.in').read().strip().split(',')))
prog.extend([0]*100000)

i = 0
base = 0
end = False
while not end:
    instr = str(prog[i]).rjust(5, '0')
    opcode = instr[-2:]
# One-parameter opcodes
    if opcode in ['03', '04', '09', '99']:

# Mode extraction
        mode = instr[-3]
        if mode == '0':
            idx = prog[i+1]
        elif mode == '1':
            idx = i+1
        elif mode == '2':
            idx = base + prog[i+1]

# Opcode matching
        if opcode == '03':
            prog[idx] = int(input('Type input: '))

        elif opcode == '04':
            out = prog[idx]
            print(out)

        elif opcode == '09':
            base += prog[idx]

        elif opcode == '99':
            end = True

        i += 2

# Three-parameters opcodes
    else:

# Mode extraction
        modes = [instr[-3], instr[-4], instr[-5]]
        idxs = []
        j = 1
        for mode in modes:
            if mode == '0':
                idxs.append(prog[i+j])
            elif mode == '1':
                idxs.append(i+j)
            elif mode == '2':
                idxs.append(base + prog[i+j])
            j += 1

        a = prog[idxs[0]]
        b = prog[idxs[1]]

# Opcode matching
        if opcode == '01':
            prog[idxs[2]] = a + b
            i += 4

        elif opcode == '02':
            prog[idxs[2]] = a * b
            i += 4

        elif opcode == '05':
            i = b if a else i+3

        elif opcode == '06':
            i = b if not a else i+3

        elif opcode == '07':
            prog[idxs[2]] = 1 if a < b else 0
            i += 4

        elif opcode == '08':
            prog[idxs[2]] = 1 if a == b else 0
            i += 4

        else:
            print(f'Unknown opcode {opcode}')
