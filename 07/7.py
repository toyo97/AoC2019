"""
Curious comment: this program works on the input string but not on the test.\
Or at least it does not give the same result as those given in the\
problem description
"""

from itertools import permutations

I = list(map(int, open('7.in').read().strip().split(',')))

sequences = permutations([5,6,7,8,9])

res = []

for perm in sequences:
#    print(f'perm: {perm}')

    out = 0
    end = False
    idx = [0] * 5
    PROG = [I[:]] * 5
    amp = 0
    first_cycle = 5
    while not end:
#        print(f'amp: {amp}')

        if first_cycle > 0:
#            print(f'inputs: {perm[amp]}, {out}')
            inputs = [perm[amp], out]
            first_cycle -= 1
        else:
#            print(f'inputs: {out}')
            inputs = [out]

        go_next = False

        while (not go_next) and (not end):
            instr = str(PROG[amp][idx[amp]]).rjust(5, '0')
            opcode = instr[-2:]

#            print(f'opcode: {opcode}')

        # No-input opcodes
            if opcode in ['03', '04', '99']:

                if opcode == '03':
                    PROG[amp][PROG[amp][idx[amp]+1]] = inputs.pop(0)
                    idx[amp] += 2

                elif opcode == '04':
                    out = PROG[amp][PROG[amp][idx[amp]+1]]
#                    inputs.append(out)
                    idx[amp] += 2
                    go_next = True
#                    print(f'amp {amp} outputs: {out}')

                elif opcode == '99':
                    end = True

        # Three-inputs opcodes
            else:
                a = PROG[amp][idx[amp]+1] if int(instr[-3]) else PROG[amp][PROG[amp][idx[amp]+1]]
                b = PROG[amp][idx[amp]+2] if int(instr[-4]) else PROG[amp][PROG[amp][idx[amp]+2]]

                if opcode == '01':
                    PROG[amp][PROG[amp][idx[amp]+3]] = a + b
                    idx[amp] += 4

                elif opcode == '02':
                    PROG[amp][PROG[amp][idx[amp]+3]] = a * b
                    idx[amp] += 4

                elif opcode == '05':
                    idx[amp] = b if a else idx[amp]+3

                elif opcode == '06':
                    idx[amp] = b if not a else idx[amp]+3

                elif opcode == '07':
                    PROG[amp][PROG[amp][idx[amp]+3]] = 1 if a < b else 0
                    idx[amp] += 4

                elif opcode == '08':
                    PROG[amp][PROG[amp][idx[amp]+3]] = 1 if a == b else 0
                    idx[amp] += 4

                else:
                    print(f'Unknown opcode {opcode}')

#        output produced, go to go_next amp
        amp = (amp + 1) % 5

    res.append(out)

print(max(res))
