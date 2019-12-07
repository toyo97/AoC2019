from itertools import permutations

I = list(map(int, open('7.in').read().strip().split(',')))

sequences = permutations([0,1,2,3,4])

res = []

for perm in sequences:
    out = 0
    print(f'perm: {perm}')

    for amp in perm:
        print(f'amp: {amp}')
        I_copy = I[:]
        inputs = [amp, out]
        i = 0
        print(f'inputs: {inputs}')

        end = False
        while not end:
            instr = str(I_copy[i]).rjust(5, '0')
            opcode = instr[-2:]
            print(f'opcode: {opcode}')
        # No-input opcodes
            if opcode in ['03', '04', '99']:

                if opcode == '03':
                    I_copy[I_copy[i+1]] = inputs.pop(0)
                    i += 2

                elif opcode == '04':
                    out = I_copy[I_copy[i+1]]
                    i += 2
                    print(f'out: {out}')

                elif opcode == '99':
                    end = True

        # Three-inputs opcodes
            else:
                a = I_copy[i+1] if int(instr[-3]) else I_copy[I_copy[i+1]]
                b = I_copy[i+2] if int(instr[-4]) else I_copy[I_copy[i+2]]

                if opcode == '01':
                    I_copy[I_copy[i+3]] = a + b
                    i += 4

                elif opcode == '02':
                    I_copy[I_copy[i+3]] = a * b
                    i += 4

                elif opcode == '05':
                    i = b if a else i+3

                elif opcode == '06':
                    i = b if not a else i+3

                elif opcode == '07':
                    I_copy[I_copy[i+3]] = 1 if a < b else 0
                    i += 4

                elif opcode == '08':
                    I_copy[I_copy[i+3]] = 1 if a == b else 0
                    i += 4

                else:
                    print(f'Unknown opcode {opcode}')

    res.append(out)


print(max(res))
