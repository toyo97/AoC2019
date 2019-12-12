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

lines = open('12.in').read().strip().split('\n')

pos = [0,1,2]
vel = [3,4,5]

moons = np.zeros((len(lines), 6))

for i,line in enumerate(lines):
    coords = line.split(', ')
    for j in range(len(coords)):
        coords[j] = int(coords[j].strip('xyz<>='))
    moons[i, pos] = np.array(coords)

for _ in range(1000):
    moons[:,vel] += compute_gravity(moons)
    moons[:,pos] += moons[:,vel]

print(compute_energy(moons[:,pos], moons[:,vel]))
