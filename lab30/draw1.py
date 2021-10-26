#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('太阳能电池的暗伏安特性测量')
plt.xlabel('电压(V)')
plt.ylabel('电流(mA)')

x = [0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0]
y = [0, 0.005, 0.017, 0.040, 0.093, 0.229, 0.564, 1.361, 4.2, 18.1, 86.0]
plt.plot(x, y, label = '单晶硅')
plt.plot(x, y, 'o')

plt.legend()
plt.show()
