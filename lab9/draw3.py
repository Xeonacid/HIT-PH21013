#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.title('PN结正向压降随温度变化曲线')
plt.xlabel('温度/℃')
plt.ylabel('电压/V')

x = [40.0, 45.0, 50.0, 55.0, 60.0, 65.0, 70.0, 75.0, 80.0, 85.0]
y = [0.4055, 0.3900, 0.3775, 0.3642, 0.3511, 0.3380, 0.3243, 0.3098, 0.2947, 0.2802]
plt.plot(x, y)
plt.plot(x, y, 'o')

plt.show()
