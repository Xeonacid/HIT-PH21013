#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

fig = plt.figure()
ax1 = fig.add_subplot()
plt.rcParams['font.sans-serif'] = ['SimHei']
ax1.set_title('单晶硅输出特性 I=215W/m^2')
ax1.set_xlabel('输出电压(V)')
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5])
x_smooth = np.linspace(x.min(), x.max(), 300)
ax1.set_ylabel('输出电流I(mA)')
y1 = np.array([22.9,23.0,22.9,23.4,23.3,22.9,22.2,22.0,21.2,19.8,17.6,16.2,13.8,11.0,6.7,0.2])
y1_smooth = make_interp_spline(x, y1)(x_smooth)
ax1.plot(x_smooth, y1_smooth, label = '输出电流I(mA)',linestyle='-')
ax1.plot(x, y1, 'o')
ax2 = ax1.twinx()
ax2.set_ylabel('输出功率P(mW)')
y2 = [x * y for x, y in zip(x, y1)]
y2_smooth = make_interp_spline(x, y2)(x_smooth)
ax2.plot(x_smooth, y2_smooth, 'g', label = '输出功率P(mW)',linestyle='--')
ax2.plot(x, y2, 'o')
Vm, Pm = 1.8, 35.64
ax2.annotate(f'Pm={Pm}W', xy = (Vm, Pm), xytext = (-20, 10), textcoords = 'offset points')
fig.legend(loc = 1, bbox_to_anchor = (1, 1), bbox_transform = ax1.transAxes)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot()
plt.rcParams['font.sans-serif'] = ['SimHei']
ax1.set_title('非晶硅输出特性 I=700W/m^2')
ax1.set_xlabel('输出电压(V)')
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6,2.7])
x_smooth = np.linspace(x.min(), x.max(), 300)
ax1.set_ylabel('输出电流I(mA)')
y1 = np.array([7.9,7.8,7.5,7.4,7.3,7.1,6.9,6.7,6.4,6.1,5.6,5.4,4.9,4.4,3.9,3.1,2.2,1.0])
y1_smooth = make_interp_spline(x, y1)(x_smooth)
ax1.plot(x_smooth, y1_smooth, label = '输出电流I(mA)',linestyle='-')
ax1.plot(x, y1, 'o')
ax2 = ax1.twinx()
ax2.set_ylabel('输出功率P(mW)')
y2 = [x * y for x, y in zip(x, y1)]
y2_smooth = make_interp_spline(x, y2)(x_smooth)
ax2.plot(x_smooth, y2_smooth, 'g', label = '输出功率P(mW)',linestyle='--')
ax2.plot(x, y2, 'o')
Vm, Pm = 2.1, 11.34
ax2.annotate(f'Pm={Pm}W', xy = (Vm, Pm), xytext = (-20, 10), textcoords = 'offset points')
fig.legend(loc = 1, bbox_to_anchor = (1, 1), bbox_transform = ax1.transAxes)
plt.show()
