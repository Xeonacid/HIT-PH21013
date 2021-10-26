#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('两种太阳能电池开路电压随光强变化曲线')
plt.xlabel('光强I(W/m^2)')
plt.ylabel('开路电压Voc(V)')
x = [740, 397, 239, 158.4, 114.0, 86.4, 67.7, 55.7]
y = [2.82, 2.70, 2.62, 2.55, 2.50, 2.46, 2.42, 2.38]
plt.plot(x, y, label = '单晶硅')
plt.plot(x, y, 'o')
y = [3.06, 2.99, 2.92, 2.87, 2.81, 2.77, 2.73, 2.69]
plt.plot(x, y, label = '非晶硅')
plt.plot(x, y, 'o')
plt.legend()
plt.show()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('两种太阳能电池短路电流随光强变化曲线')
plt.xlabel('光强I(W/m^2)')
plt.ylabel('短路电流Isc(mA)')
x = [740, 397, 239, 158.4, 114.0, 86.4, 67.7, 55.7]
y = [77.6, 42.0, 26.2, 17.7, 13.0, 9.9, 7.7, 6.3]
plt.plot(x, y, label = '单晶硅')
plt.plot(x, y, 'o')
y = [8.9, 4.8, 3.0, 2.0, 1.501, 1.149, 0.902, 0.726]
plt.plot(x, y, label = '非晶硅')
plt.plot(x, y, 'o')
plt.legend()
plt.show()
