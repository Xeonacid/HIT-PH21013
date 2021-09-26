#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def sin_wave(start, end, period, ratio, xlabel = '', ylabel = ''):
    x = np.arange(start, end, 0.001)
    y = ratio * np.sin(x * 2 * np.pi / period)

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def triangle_wave(start, end, period, ratio, xlabel = '', ylabel = ''):
    x = []
    y = []

    i = start
    isup = True
    while i < end:
        curend = i + period / 2
        if curend > end:
            curend = end
        curx = np.arange(i, curend, 0.001)
        cury = np.array([ratio * (-1 + (t - i) / (period / 2) * 2) if isup else ratio * (1 - (t - i) / (period / 2) * 2) for t in curx])
        x = np.append(x, curx)
        y = np.append(y, cury)

        i += period / 2
        isup = not isup

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def square_wave(start, end, period, ratio, xlabel = '', ylabel = ''):
    x = []
    y = []

    i = start
    ispositive = True
    while i < end:
        curend = i + period / 2
        if curend > end:
            curend = end
        curx = np.arange(i, curend, 0.001)
        cury = np.array([ratio if ispositive else -ratio for t in curx])
        x = np.append(x, curx)
        y = np.append(y, cury)

        i += period / 2
        ispositive = not ispositive

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def half_wave_rectification(start, end, period, ratio, xlabel = '', ylabel = ''):
    x = []
    y = []

    i = start
    issin = True
    while i < end:
        curend = i + period / 2
        if curend > end:
            curend = end
        curx = np.arange(i, curend, 0.001)
        print(curx.shape)
        cury = ratio * np.sin((curx - i) * 2 * np.pi / period) if issin else np.zeros(curx.shape[0])
        x = np.append(x, curx)
        y = np.append(y, cury)

        i += period / 2
        issin = not issin

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def full_wave_rectification(start, end, period, ratio, xlabel = '', ylabel = ''):
    x = []
    y = []

    i = start
    while i < end:
        curend = i + period
        if curend > end:
            curend = end
        curx = np.arange(i, curend, 0.001)
        print(curx.shape)
        cury = ratio * np.sin((curx - i) * np.pi / period)
        x = np.append(x, curx)
        y = np.append(y, cury)

        i += period

    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

sin_wave(-0.3, 0.3, 0.238, 4.4, 'x / ms', 'y / V')
triangle_wave(-0.3, 0.3, 0.238, 4.4, 'x / ms', 'y / V')
square_wave(-0.3, 0.3, 0.238, 4.4, 'x / ms', 'y / V')
half_wave_rectification(-0.3, 0.3, 0.238, 2, 'x / ms', 'y / V')
full_wave_rectification(-0.2, 0.2, 0.119, 2.3, 'x / ms', 'y / V')
