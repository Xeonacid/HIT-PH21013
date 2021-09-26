#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

ts = np.linspace(-50, 50, 1000)

def lissajous(A1 = 5, A2 = 8, w1 = 1.2, w2 = 1.2, theta1 = np.pi, theta2 = 0.6 * np.pi, title = ''):

    x, y = [], []
    for t in ts:
        x.append(A1 * np.cos(w1 * t + theta1))
        y.append(A2 * np.cos(w2 * t + theta2))

    plt.plot(x, y)
    plt.title(title)
    plt.show()

lissajous(title = 'f_x = 4.198kHz')
lissajous(w1 = 2, w2 = 1, theta2 = 0.75 * np.pi, title = 'f_x = 8.394kHz')
lissajous(w1 = 3, w2 = 1, theta2 = 0.8 * np.pi, title = 'f_x = 12.59kHz')
