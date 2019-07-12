# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 14:25:23 2019

@author: gonzaga.g

Primeiras aulas com código do curso da EdX
"""

import numpy as np

x = [1, 5]
x = np.array(x)
x + 1
x + 2
x - 4
x*5

y = np.array([5, 6])
x+y
x*y
x/y

np.zeros([4, 5])  # retorna uma matrix x, y de zeros
np.ones([4, 6])  # retorna uma matrix x, y de 1s

np.random.random([3, 2])  # retorna uma matrix aleatória x, y
######################
#         Ex.1       #
######################


def randomization(n):
    """
    Arg:
      n - an integer
    Returns:
      A - a randomly-generated nx1 Numpy array.
    """
    # Your code here
    return np.random.random([n, 1])


randomization(5)

x.shape
y = np.array([[3, 5, 1], [1, 3, 9]])
y.shape
y.transpose()

z = y+3
z*y  # element-wise multiplication!!
np.matmul(x, z)  # algebraic matrix multiplication
np.exp(x)  # e to the power of each element in x
np.sin(x)  # works as exp, element-wise
np.tanh(x)

x = np.array([4, 2, 9, -6, 5, 11, 3])
np.max(x)
x.max()
np.min(x)

np.random.random([2, 6])
np.random.random()  # single random element

np.linalg.norm(x)  # L2 norm of x matrix

######################
#        Proj 0      #
######################


def neural_network(inputs, weights):
    """
     Takes an input vector and runs it through a 1-layer neural network
     with a given weight matrix and returns the output.

     Arg:
       inputs - 2 x 1 NumPy array
       weights - 2 x 1 NumPy array
     Returns (in this order):
       out - a 1 x 1 NumPy array, representing the output of the neural network
    """
    # Your code here
    return np.tanh(np.matmul(weights.transpose(), inputs))


neural_network(np.random.random([2, 1]), np.random.random([2, 1]))
