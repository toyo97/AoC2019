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

def mcm(nums, offset):
    v = offset + nums
    while not np.all(v == v[0]):
        i = np.argmin(v)
        v[i] += nums[i]

    return v[0]


lines = open('12.in').read().strip().split('\n')

pos = [0,1,2]
vel = [3,4,5]

moons = np.zeros((len(lines), 6))

for i,line in enumerate(lines):
    coords = line.split(', ')
    for j in range(len(coords)):
        coords[j] = int(coords[j].strip('xyz<>='))
    moons[i, pos] = np.array(coords)

visited = moons[:,:,np.newaxis].copy()
end = [False, False, False]

periods = np.zeros((3,2))
it = 0

while not all(end):

    moons[:,vel] += compute_gravity(moons)
    moons[:,pos] += moons[:,vel]

    for i in range(visited.shape[2]):
        for k in range(3):
            if not end[k] and np.array_equal(moons[:,[k,k+3]], visited[:,:,i].reshape(moons.shape)[:,[k, k+3]]):

                periods[k,:] = np.array([i, it+1])
                end[k] = True

    visited = np.append(visited, moons[:,:,np.newaxis].copy(), axis=2)
    it += 1
    if it % 100 == 0:
        print(it, visited.shape[2])

print(f'final it: {it}')
print(periods)

print(mcm(periods[:,1] - periods[:,0], periods[:,0]))




