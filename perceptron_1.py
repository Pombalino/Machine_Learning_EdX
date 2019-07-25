# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 08:53:53 2019

@author: gonzaga.g
"""
import numpy as np

x = np.array([[-4, 2], [-2, 1], [-1, -1], [2, 2], [1, -2]])
y = [1, 1, -1, -1, -1]
t = 2
n_mistakes = 0


def perceptron(x, y, t, n_mistakes, offset=False):
    tits = []
    theta = np.array([0.0, 0.0])
    tet0 = 0
    for j in range(1, t+1):
        print(j)
        for i in range(len(x)):
            print("x=", x[i])
            if offset:
                if y[i]*(np.matmul(theta, x[i])+tet0) <= 0:
                    theta += y[i]*x[i]
                    tet0 += y[i]
                    print("\u03B8=", theta)
                    print("\u03B8_0=", tet0)
                    n_mistakes += 1
            else:
                if y[i]*np.matmul(theta, x[i]) <= 0:
                    theta += y[i]*x[i]
                    print("\u03B8=", theta)
                    n_mistakes += 1
                    tits.append(theta.copy())
    return tits, tet0, n_mistakes


tits, tet, nm = perceptron(x, y, t, n_mistakes, offset=True)
[list(i) for i in tits]
