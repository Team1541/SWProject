import os
import matplotlib
os.environ['DISPLAY'] = 'localhost:1.0'
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(100))
plt.show()

