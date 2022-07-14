import numpy as np
import matplotlib.pyplot as plt

error_threshold = 2

x_points = []
y_points = []

for x in np.arange(0,10.2, 0.2):

    # get a random number between 1 and 5
    number_of_y_points = np.random.randint(1, 5)

    for y_point in np.arange(0, number_of_y_points):
        
        # get a random number between 0 and 0.2
        error = np.random.uniform(-error_threshold, error_threshold)
        y = -(np.square(x) - (10*x)) + error

        x_points.append(x)
        y_points.append(y)

plt.scatter(x_points, y_points)
plt.show()