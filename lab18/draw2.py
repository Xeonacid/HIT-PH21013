#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('接收信号幅度与距离的关系')
plt.xlabel('线圈距离(cm)')
plt.ylabel('幅度(V)')
x = [26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
y = [5.0, 6.4, 7.2, 7.4, 7.6, 7.4, 7.0, 6.6, 6.1, 5.5]
plt.plot(x, y)
plt.plot(x, y, 'o')
plt.show()
