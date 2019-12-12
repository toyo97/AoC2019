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

energies = compute_energy(moons[:,pos], moons[:,vel])
visited = moons[:,:,np.newaxis].copy()
end = False

it = 0
while not end:

    moons[:,vel] += compute_gravity(moons)
    moons[:,pos] += moons[:,vel]

    new_en = compute_energy(moons[:,pos], moons[:,vel])
    same_en_idx = np.argwhere(energies == new_en)
    if  same_en_idx.size > 0:
#        print(len(visited), same_en_idx.size)
        for i in range(same_en_idx.size):
            end = np.array_equal(moons, visited[:,:,same_en_idx[i]].reshape(moons.shape))
            if end:
                break
    visited = np.append(visited, moons[:,:,np.newaxis].copy(), axis=2)
    energies = np.append(energies, new_en)
    it += 1
#    if it == 2772:
#        print(moons)
#        print(visited[:,:,0])
#        print(compute_energy(moons[:,pos], moons[:,vel]))
#        print(energies[-1])
#        print(np.array_equal(moons, visited[:,:,0]))
#        print(end)
#        end = True
    if it % 10000 == 0:
        print(it)

print(f'final it: {it}')
