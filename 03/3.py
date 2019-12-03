from operator import add

def d(v):
    return abs(v[0]) + abs(v[1])

def add_steps(path, steps, inters):
    for i,p in enumerate(path):
        if p in inters:
            steps[p] += i


l1, l2 = open('3.in', 'r').read().strip().split('\n')
w1, w2 = l1.split(','), l2.split(',')

M = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }

path1 = [(0,0)]
path2 = [(0,0)]

for dir1, dir2 in zip(w1, w2):
    m1, m2 = M[dir1[0]], M[dir2[0]]

    for _ in range(int(dir1[1:])):
        new_point = tuple(map(add, m1, path1[-1]))
        path1.append(new_point)

    for _ in range(int(dir2[1:])):
        new_point = tuple(map(add, m2, path2[-1]))
        path2.append(new_point)

#print(path1)

p1 = set(path1)
p2 = set(path2)

inters = p1.intersection(p2)
inters.remove((0,0))

#print(inters)

md = list(map(d, inters))

print(min(md))

steps = {key: 0 for key in inters}

add_steps(path1, steps, inters)
add_steps(path2, steps, inters)

print(min(steps.values()))
