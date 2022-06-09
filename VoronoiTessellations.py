import matplotlib.pyplot as plt
import random
import numpy as np
import math

def GenerateVoroniTesselations(num_kernels, size):
    
    def GenerateKernels(k, size):
        kernels = []
        for i in range(k):
            kernels.append([[random.randint(0, size), random.randint(0, size)], random.randint(0, 255)])
        return kernels

    def Distance(a, b):
        return math.sqrt(math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2))

    kernels = GenerateKernels(num_kernels, size)

    img = np.full((size, size), 255, dtype=np.uint8)
    
    for kernel in kernels:
        x, y = kernel[0][0], kernel[0][1]
        img[x, y] = np.array([180])

    min_distance = []
    for x in range(size):
        for y in range(size):
            distances = []
            for kernel in kernels:
                distances.append(Distance(kernel[0], [x, y]))
            min_distance.append([min(distances), distances.index((min(distances)))])
            
    count = 0
    for x in range(size):
        for y in range(size):
                img[x, y] = kernels[min_distance[count][1]][1]
                count += 1
    

    for kernel in kernels:
        img[kernel[0][0], kernel[0][1]] = 0

    fig = plt.figure(figsize=(10,10))
    plt.imshow(img)
    plt.show()

GenerateVoroniTesselations(24, 1000)