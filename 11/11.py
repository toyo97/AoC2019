import numpy as np
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, start_panel=0):
        self.dir = (0,1)
        self.table = [[0 for i in range(1000)] for j in range(1000)]
        self.pos = (499, 499)
        self.table[self.pos[1]][self.pos[0]] = start_panel
        self.colored = set()

    def get_color(self):
        return self.table[self.pos[1]][self.pos[0]]

    def acquire_out(self, out):
#        print(f'pos: {self.pos}')
        color = out.pop(0)
        turn = out.pop(0)
        if self.table[self.pos[1]][self.pos[0]] != color:
            self.colored.add(self.pos)
#            print(self.colored)
            self.table[self.pos[1]][self.pos[0]] = color

        self.dir = RIGHT[self.dir] if turn == 1 else LEFT[self.dir]
        self.pos = self.pos[0] + self.dir[0], self.pos[1] + self.dir[1]

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


RIGHT = {(0,1): (1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1)}
LEFT = {(0,1): (-1,0), (-1,0): (0,-1), (0,-1): (1,0), (1,0): (0,1)}

prog = list(map(int, open('11.in').read().strip().split(',')))
prog.extend([0]*100000)

robot = Robot(start_panel=1)

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
            prog[idx] = robot.get_color()
#            print(f'color: {prog[idx]}')

        elif opcode == '04':
            out.append(prog[idx])
            if len(out) == 2:
#                print(f'out: {out}')
                robot.acquire_out(out)

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


print(len(robot.colored))

plot(robot.table, robot.colored)
