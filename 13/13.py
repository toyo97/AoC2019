import numpy as np
import sys
from time import sleep

np.set_printoptions(threshold=sys.maxsize)


def choose_dir(table, old_xball):
    nptable = np.array(table)
    yball, xball = tuple(np.argwhere(nptable == '.')[0, :])
    ypaddle, xpaddle = tuple(np.argwhere(nptable == '_')[0, :])

    if old_xball > xball:
        bdir = -1
    else:
        bdir = 1
    xfuture = xball + bdir
    if xfuture == xpaddle or (abs(xfuture-xpaddle) == 1 and ypaddle - yball == 1):
        dir = 0
    elif xfuture < xpaddle:
        dir = -1
    else:
        dir = 1
    print(f'ball {xball, yball} paddle {xpaddle, ypaddle} xfuture {xfuture}')
    return dir, xball

def print_table(table):
    for i in range(len(table)):
        print("".join(table[i]) + '\n')

def norm(v):
    return abs(v[0]) + abs(v[1])

def plot(table, colored):
    # top-left corner and bottom-right corner
    img = np.array(table)

    tl = min(colored, key=norm)
    br = max(colored, key=norm)

    img = img[br[1]+10:tl[1]-10:-1, tl[0]-10:br[0]+10]
    plt.imshow(img)
    plt.show()

prog = list(map(int, open('13.in').read().strip().split(',')))
prog.extend([0]*100000)

table = [[' '] * 45 for _ in range(20)]

oldx = 0

M = [' ', '|', '#', '_', '.']
J = {'a': -1, 's': 0, 'd': 1}

# play for free
prog[0] = 2

out = []
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
            print_table(table)
            prog[idx], oldx = choose_dir(table, oldx)
            sleep(0.01)
#            inp = ''
#            while inp not in J.keys():
#                inp = input('')
#
#            prog[idx] = int(J[inp])
#            inp = ''
#            print(f'color: {prog[idx]}')

        elif opcode == '04':
            out.append(prog[idx])
            if len(out) == 3:
#                print(f'out: {out}')
                c = out.pop(0)
                r = out.pop(0)
                s = out.pop(0)
                if c == -1 and r == 0:
                    print(s)
                else:
                    table[r][c] = M[s]

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


