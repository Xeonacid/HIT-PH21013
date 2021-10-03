#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('不同温度下PN结正向伏安特性曲线')
plt.xlabel('电压/V')
plt.ylabel('电流/μA')

x = [0.300, 0.320, 0.340, 0.360, 0.380, 0.400, 0.420, 0.440]
y = [1.0, 1.6, 2.7, 4.5, 7.7, 12.9, 21.8, 36.4]
plt.plot(x, y, label = 'T=t0')
plt.plot(x, y, 'o')

x = [0.300, 0.320, 0.340, 0.360, 0.380, 0.400, 0.420, 0.440]
y = [3.6, 6.0, 9.8, 16.2, 26.7, 43.0, 68.4, 106.6]
plt.plot(x, y, label = 'T=40.0℃')
plt.plot(x, y, 'o')

plt.legend()
plt.show()
