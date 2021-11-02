import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func1(x, a, b):
    return a * np.exp(b * x)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('电压V(V)')
plt.ylabel('电流I(mA)')
x = np.array([1.7498,1.7783,1.7981,1.8363,1.8787,1.9054,1.9259,1.9451,1.9607,1.9768,1.9893])
y = np.array([0.3090,0.6084,0.9388,1.9959,4.023,5.950,7.935,10.173,12.368,15.213,18.073])
x_smooth = np.linspace(x.min(), x.max(), 300)
popt1, _ = curve_fit(func1, x, y)
y_smooth = [func1(i, popt1[0],popt1[1]) for i in x_smooth]
plt.plot(x_smooth,y_smooth,linestyle='-')
plt.plot(x, y, 'o')
plt.title(f'LED伏安特性曲线   ({popt1[0]:.4e})*e^(({popt1[1]:.4e})*x)')
plt.legend()
plt.show()

def func2(x, a, b):
    return a*x + b

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xlabel('电压V(V)')
plt.ylabel('电流I(mA)')
x = np.array([0.25,0.50,0.65,0.81,0.92,1.14,1.30,1.62,1.94,2.26,2.60,2.88])
y = np.array([0.1551,0.3083,0.3998,0.4997,0.5998,0.7023,0.7996,1.0016,1.2020,1.3999,1.6060,1.7906])
x_smooth = np.linspace(x.min(), x.max(), 300)
popt2, _ = curve_fit(func2, x, y)
y_smooth = [func2(i, popt2[0],popt2[1]) for i in x_smooth]
plt.plot(x_smooth,y_smooth,linestyle='-')
plt.plot(x, y, 'o')
plt.title(f'电阻伏安特性曲线   ({popt2[0]:.4e})*x+({popt2[1]:.4e})')
plt.annotate(f'Rx+RA={1000/popt2[0]:.0f}Ω', xy = (2.0, 0.4), xytext = (0, 0), textcoords = 'offset points')
plt.legend()
plt.show()