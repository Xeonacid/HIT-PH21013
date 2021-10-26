#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax1 = fig.add_subplot()
plt.rcParams['font.sans-serif'] = ['SimHei']
ax1.set_title('单晶硅输出特性 I=740W/m^2')
ax1.set_xlabel('输出电压(V)')
x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4]
ax1.set_ylabel('输出电流I(A)')
y1 = [0.0778, 0.0782, 0.0790, 0.0776, 0.0781, 0.0777, 0.0771, 0.0763, 0.0764, 0.0753, 0.0722, 0.0618, 0.0341]
ax1.plot(x, y1, label = '输出电流I(A)')
ax1.plot(x, y1, 'o')
ax2 = ax1.twinx()
ax2.set_ylabel('输出功率P(W)')
y2 = [x * y for x, y in zip(x, y1)]
ax2.plot(x, y2, 'g', label = '输出功率P(W)')
ax2.plot(x, y2, 'o')
Vm, Pm = 2.0, 0.1444
ax2.annotate(f'Pm={Pm}W', xy = (Vm, Pm), xytext = (-20, 10), textcoords = 'offset points')
fig.legend(loc = 1, bbox_to_anchor = (1, 1), bbox_transform = ax1.transAxes)
plt.show()

fig = plt.figure()
ax1 = fig.add_subplot()
plt.rcParams['font.sans-serif'] = ['SimHei']
ax1.set_title('非晶硅输出特性 I=239W/m^2')
ax1.set_xlabel('输出电压(V)')
x = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8]
ax1.set_ylabel('输出电流I(A)')
y1 = [0.0037, 0.0037, 0.0037, 0.0036, 0.0036, 0.0036, 0.0036, 0.0035, 0.0034, 0.0033, 0.0032, 0.0029, 0.0026, 0.0020, 0.0010]
ax1.plot(x, y1, label = '输出电流I(A)')
ax1.plot(x, y1, 'o')
ax2 = ax1.twinx()
ax2.set_ylabel('输出功率P(W)')
y2 = [x * y for x, y in zip(x, y1)]
ax2.plot(x, y2, 'g', label = '输出功率P(W)')
ax2.plot(x, y2, 'o')
Vm, Pm = 2.0, 0.0064
ax2.annotate(f'Pm={Pm}W', xy = (Vm, Pm), xytext = (-20, 10), textcoords = 'offset points')
fig.legend(loc = 1, bbox_to_anchor = (1, 1), bbox_transform = ax1.transAxes)
plt.show()
