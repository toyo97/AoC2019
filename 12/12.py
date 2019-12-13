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


def key_hash(x):
    y = x * 3 - 2
    k = np.zeros((1,3))
    for i in range(3):
        k[0,i] = y[:,[i,i+3]].sum()
    return k


key = np.array(key_hash(moons))
end = [False, False, False]

periods = np.zeros((3,2))
it = 0

while not all(end):

    moons[:,vel] += compute_gravity(moons)
    moons[:,pos] += moons[:,vel]
    new_key = key_hash(moons)

    ran = np.argwhere([not x for x in end]).flatten().tolist()
#    print(visited[:,:,0])
    for k in ran:
        eq_k = new_key[:,k] == key[:,k]
        if np.any(eq_k):
            for idx in np.argwhere(eq_k).flatten().tolist():
#        print(moons[:,[k,k+3]])
#        print(visited[:,[k,k+3],0].transpose((2,0,1)))
                eq = np.array_equal(moons[:,[k,k+3]], visited[:,[k,k+3],idx])
    #        print(eq.size)
                if np.any(eq):
                    i = np.argwhere(eq)
                    periods[k,:] = np.array([i, it+1])
                    end[k] = True

    visited = np.append(visited, moons[:,:,np.newaxis].copy(), axis=-1)
    key = np.append(key, new_key, axis=0)

#    if it == 0:
#        print(visited)
#        print(visited[:,[0,3],:].transpose((2,0,1)))
#        print(np.all(visited[:,[0,3],:].transpose((2,0,1)) == moons[:,[0,3]], axis=(1,2)))
    it += 1
    if it % 100 == 0:
        print(it)

print(f'final it: {it}')
print(periods)

print(mcm(periods[:,1] - periods[:,0], periods[:,0]))
