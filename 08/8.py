import numpy as np
import matplotlib.pyplot as plt

# LAYER DIMENSIONS
m = 6
n = 25

# Input reading
nums = list(map(int, open('8.in').read().strip()))

# Check if the dimensions fit the input
assert len(nums) % m*n == 0

# ... and then find the number of layers
nlayers = len(nums) // (m*n)


# ************ PART 1 ***************

# Create 3D tensors
A = np.array(nums).reshape((nlayers, m, n))

# Find layer with fewest 0 occurrences
layX = (np.sum(A == 0, axis=(1,2))).argmin()

print(f'Part 1 solution: {np.sum(A[layX,:,:] == 1) * np.sum(A[layX,:,:] == 2)}')


# ************ PART 2 ***************

# Solution image initialization
B = np.zeros((m,n))

# Find foremost visible pixels in tensor and store them in the sol. image
for i in range(A.shape[1]):
    for j in range(A.shape[2]):
        k = 0
        while A[k,i,j] == 2:
            k += 1
        B[i,j] = A[k,i,j]

# Plot the image
plt.imshow(B)
plt.show()
