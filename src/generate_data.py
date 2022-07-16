from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

error_threshold = 2

points = pd.DataFrame(columns=['x', 'y'])
function = pd.DataFrame(columns=['x', 'y'])

fig,ax = plt.subplots(1,1)

number_of_random_points = 20

resolution = 0.05

for x in np.arange(0,10+resolution, resolution):

    # get a random number between 1 and 5
    number_of_y_points = np.random.randint(1, number_of_random_points)

    y = -(np.square(x) - (10*x))
    
    function = function.append({'x': x, 'y': y}, ignore_index=True)

    for y_point in np.arange(0, number_of_y_points):
        
       
        error = np.random.uniform(-error_threshold, error_threshold)

        points = points.append({'x': x, 'y': y+error}, ignore_index=True)



function.plot(x='x', y='y', ax=ax, kind='line', color='blue', label='function')

points.plot(x='x', y='y', kind='scatter', ax=ax, color='gainsboro', label='points')


estimate = pd.DataFrame(columns=['x', 'y'])

for x in np.arange(0,10+resolution, resolution):
    # get y points for x
    y_points = points[points['x'] == x]

    y_average = np.mean(y_points['y'])

    estimate = estimate.append({'x': x, 'y': y_average}, ignore_index=True)

# estimate.plot(x='x', y='y', kind='line', ax=ax, color='red', label='estimate')

# estimate mean squared error

estimate_error_squared = (estimate['y'] - function['y'])**2
estimate_mse = np.mean(estimate_error_squared)
print('Estimate MSE: ', estimate_mse)



neighborhood_estimate = pd.DataFrame(columns=['x', 'y'])

for x in np.arange(0,10+resolution, resolution):
    
    window = 10*resolution
    
    y_points = points[(points['x'] > x - window) & (points['x'] < x + window)]

    y_neighborhood_average = np.mean(y_points['y'])
    
    neighborhood_estimate = neighborhood_estimate.append({'x': x, 'y': y_neighborhood_average}, ignore_index=True)
    
# neighborhood_estimate.plot(x='x', y='y', kind='line', ax=ax, color='green', label='neighborhood estimate')

neighborhood_error_squared = (neighborhood_estimate['y'] - function['y'])**2
neighborhood_mse = np.mean(neighborhood_error_squared)
print('Neighborhood MSE: ', neighborhood_mse)


plt.show()
