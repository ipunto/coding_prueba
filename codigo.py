import numpy as np

x = np.linspace(0,1,100)
y = np.sin(x)

print(x)

import matplotlib.pyplot as plt

plt.plot(x,y)

z = np.cos(x)**2 + y**2

print(np.mean(z))