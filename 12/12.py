import numpy as np

def compute_gravity(arr):
    acc = np.zeros((arr.shape[0],3))

    for i in range(arr.shape[0]):
        for j in range(3):
            acc[i,j] += np.sum(arr[:,j] > arr[i,j])
            acc[i,j] -= np.sum(arr[:,j] < arr[i,j])

    return acc

def compute_energy(P, V):
    pot = np.sum(np.abs(P), axis=1)
    kin = np.sum(np.abs(V), axis=1)
    return np.sum(pot*kin)

lines = open('test12_2.in').read().strip().split('\n')

pos = [0,1,2]
vel = [3,4,5]

moons = np.zeros((len(lines), 6))

for i,line in enumerate(lines):
    coords = line.split(', ')
    for j in range(len(coords)):
        coords[j] = int(coords[j].strip('xyz<>='))
    moons[i, pos] = np.array(coords)

visited = moons[:,:,np.newaxis].copy()
end = False

repeat = [(0,0) for _ in range(3)]

it = 0

coords = [0,1,2]
V = [[],[],[]]

while not end:

    moons[:,vel] += compute_gravity(moons)
    moons[:,pos] += moons[:,vel]

    for c in coords:
        c_tup = tuple(moons[:,c])
        if c_tup in V[c]:
            repeat[c] = (V[c].index(c_tup),it)
            coords.remove(c)

        else:
            V[c].append(c_tup)

    end = len(coords) == 0

    it += 1
    if it == 14:
        print(moons)
        print(visited[:,:,0])
        print(repeat)

    if it % 1000 == 0:
        print(it)

print(f'final it: {it}')
print(f'repeats: {repeat}')
