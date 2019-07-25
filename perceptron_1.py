# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:53:53 2019

@author: gonzaga.g
"""
import numpy as np

x = np.array([[-1, -1], [1, 0], [-1, 10.0]])
y = [1, -1, 1]
t = 15
n_mistakes = 0


def perceptron(x, y, t, n_mistakes):
    tits = []
    theta = np.array([0.0, 0.0])
    for j in range(1, t+1):
        print(j)
        for i in range(len(x)):
            print("x=", x[i])
            if y[i]*np.matmul(theta, x[i]) <= 0:
                theta += y[i]*x[i]
                print("\u03B8=", theta)
                n_mistakes += 1
                tits.append(theta.copy())
    return tits, n_mistakes


tits, nm = perceptron(x, y, t, n_mistakes)
[list(i) for i in tits]
