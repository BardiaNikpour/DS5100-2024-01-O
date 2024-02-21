### Exercise 5 ###

import random
import matplotlib.pyplot as plt
import numpy as np


# Generate a 2x3 matrix of random normals
matrix = np.random.randn(2, 3)

#Excercise 5.7
# Multiply the matrix by 2 (scale the matrix)
matrix = matrix * 2

#Exercise 5.8
# Add the scaled matrix to itself
matrix = matrix + matrix

# Print the matrix
print(matrix)
 