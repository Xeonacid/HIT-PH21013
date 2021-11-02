#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('两种太阳能电池开路电压随光强变化曲线')
plt.xlabel('光强I(W/m^2)')
plt.ylabel('开路电压Voc(V)')
x = np.array([700,365,215,144,104,79,63,51])[::-1]
y = np.array([2.72,2.60,2.50,2.41,2.32,2.23,2.14,2.05])[::-1]
x_smooth = np.linspace(x.min(), x.max(), 300)
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth, label = '单晶硅',linestyle='-')
plt.plot(x, y, 'o')
y = np.array([3.01,2.78,2.46,2.16,1.91,1.70,1.51,1.34])[::-1]
y_smooth = make_interp_spline(x, y)(x_smooth)
plt.plot(x_smooth, y_smooth, label = '非晶硅',linestyle='--')
plt.plot(x, y, 'o')
plt.legend()
plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('两种太阳能电池短路电流随光强变化曲线')
plt.xlabel('光强I(W/m^2)')
plt.ylabel('短路电流Isc(mA)')
x = np.array([700,365,215,144,104,79,63,51])
y = np.array([73.1,39.9,23.0,16.2,11.7,9.0,7.1,5.8])
plt.plot(x, y, label = '单晶硅',linestyle='-')
plt.plot(x, y, 'o')
y = np.array([7.9,4.3,2.6,1.7,1.3,1.0,0.8,0.6])
plt.plot(x, y, label = '非晶硅',linestyle='--')
plt.plot(x, y, 'o')
plt.legend()
plt.show()
