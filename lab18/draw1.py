#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('接收信号幅度与频率的关系')
plt.xlabel('频率(MHz)')
plt.ylabel('幅度(V)')
x = [2.14, 2.15, 2.16, 2.17, 2.18, 2.19, 2.20, 2.21, 2.22, 2.23]
y = [5.5, 6.1, 7.8, 10.0, 11.3, 11.0, 8.0, 6.4, 5.0, 4.0]
plt.plot(x, y, label = '1倍基频')
plt.plot(x, y, 'o')
plt.legend()
plt.show()

plt.title('接收信号幅度与频率的关系')
plt.xlabel('频率(MHz)')
plt.ylabel('幅度(V)')
x = [1.070, 1.075, 1.080, 1.085, 1.090, 1.095, 1.100, 1.105, 1.110, 1.115]
y = [3.5, 3.9, 4.2, 4.8, 5.9, 6.1, 4.8, 5.5, 4.7, 3.6]
plt.plot(x, y, label = '1/2倍基频')
plt.plot(x, y, 'o')
plt.legend()
plt.show()

plt.title('接收信号幅度与频率的关系')
plt.xlabel('频率(MHz)')
plt.ylabel('幅度(V)')
x = [0.710, 0.715, 0.720, 0.725, 0.730, 0.735, 0.740, 0.745, 0.750, 0.755]
y = [3.9, 4.3, 5.2, 8.5, 9.0, 7.0, 4.5, 4.0, 3.5, 2.9]
plt.plot(x, y, label = '1/3倍基频')
plt.plot(x, y, 'o')
plt.legend()
plt.show()
