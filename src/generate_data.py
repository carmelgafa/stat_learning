import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10.5, 0.5)


print(x)

y = -(np.square(x) - (10*x))

print(y)

plt.plot(x,y)
plt.show()