import numpy as np
import matplotlib.pyplot as plt

m = 6
n = 25

nums = list(map(int, open('8.in').read().strip()))

#print(f'Array length: {len(nums)}')
assert len(nums) % m*n == 0

nlayers = len(nums) // (m*n)

A = np.array(nums).reshape((nlayers, m, n))

occ0 = np.sum(A == 0, axis=(1,2))
#print(occ0)
layX = occ0.argmin() # layer with fewest 0 occurrences

print(np.sum(A[layX,:,:] == 1) * np.sum(A[layX,:,:] == 2))

B = np.zeros((m,n))

for i in range(A.shape[1]):
    for j in range(A.shape[2]):
        k = 0
        while A[k,i,j] == 2:
            k += 1
        B[i,j] = A[k,i,j]

plt.imshow(B, interpolation='nearest')
plt.show()
