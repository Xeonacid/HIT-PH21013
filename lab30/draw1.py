#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('太阳能电池的暗伏安特性测量')
plt.xlabel('电压(V)')
plt.ylabel('电流(mA)')

x = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0])
y = np.array([0, 0.029,0.099,0.254,0.574,1.239,2.5,4.9,9.6,23.3,86.4])
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth, label = '单晶硅',linestyle='-')
plt.plot(x, y, 'o')

x = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0])
y = np.array([0,0.006,0.017,0.037,0.081,0.184,0.436,1.2,3.5,15.2,68.5])
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth, label = '多晶硅',linestyle='--')
plt.plot(x, y, 'o')

x = np.array([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.2, 4.5])
y = np.array([0, 0.117,0.241,0.370,0.507,0.676,0.942,1.3,1.9,2.5,3.5,5.4,9.4,14.8,21.7,29.6])
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth, label = '非晶硅',linestyle='-.')
plt.plot(x, y, 'o')

plt.legend()
plt.show()
