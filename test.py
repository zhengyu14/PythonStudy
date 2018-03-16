# Path (Mac): /Users/Zhengyu/Documents/Git/PythonStudy/test.py
# Path (Win): C:\Users\i323429\Documents\GitHub\PythonStudy\test.py

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y = 2*x + 1

plt.figure()
plt.plot(x, y)
plt.show()
