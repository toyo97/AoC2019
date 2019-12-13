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

visited = moons.copy()[:,:,np.newaxis]
print(visited[:,:,0])
end = [False, False, False]

periods = np.zeros((3,2))
it = 0

while not all(end):

    moons[:,vel] += compute_gravity(moons)
    moons[:,pos] += moons[:,vel]

    for k in range(3):
#        print(moons[:,[k,k+3]])
#        print(visited)
#        print(visited[:,[k,k+3],0].transpose((2,0,1)))
        eq = np.all(moons[:,[k,k+3]] == visited[:,[k,k+3],:].transpose((2,0,1)), axis=(1,2))
#        print(eq.size)
        if not end[k] and np.any(eq):
            i = np.argwhere(eq)
            periods[k,:] = np.array([i, it+1])
            end[k] = True

    visited = np.append(visited, moons[:,:,np.newaxis].copy(), axis=-1)
    if it == 0:
        print(visited)
        print(visited[:,[0,3],:].transpose((2,0,1)))
        print(np.all(visited[:,[0,3],:].transpose((2,0,1)) == moons[:,[0,3]], axis=(1,2)))
    it += 1
    if it % 100 == 0:
        print(it)

print(f'final it: {it}')
print(periods)

print(mcm(periods[:,1] - periods[:,0], periods[:,0]))
