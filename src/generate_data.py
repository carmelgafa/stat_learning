from operator import ne
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_data(func, max_random_points=20, min_point=0, max_point=10, resolution=0.05, error_threshold=2):

    print("Generating data...")

    points = pd.DataFrame(columns=['x', 'y'])

    function = pd.DataFrame(columns=['x', 'y'])

    for x in np.arange(min_point,max_point+resolution, resolution):

        # get a random number between 1 and max_random_points
        number_of_y_points = np.random.randint(1, max_random_points)

        y = func(x)

        function = function.append({'x': x, 'y': y}, ignore_index=True)

        for _ in np.arange(0, number_of_y_points):

            error = np.random.uniform(-error_threshold, error_threshold)

            points = points.append({'x': x, 'y': y+error}, ignore_index=True)

    # save function in csv
    function.to_csv('function.csv', index=False)

    # save points in csv
    points.to_csv('points.csv', index=False)

    return function, points

def extract_points(min_point=0, max_point=10, resolution=0.05):
    points = pd.read_csv('points.csv')

    filtered_points = pd.DataFrame(columns=['x', 'y'])

    for x in np.arange(min_point,max_point+resolution, resolution):
        y_points = points[points['x'] == x]
        
        filtered_points = filtered_points.append(y_points, ignore_index=True)

    return filtered_points

def average_estimate(points):

    average_estimate = pd.DataFrame(columns=['x', 'y'])

    for x in points['x']:
        y_points = points[points['x'] == x]

        y_average = np.mean(y_points['y'])

        average_estimate = average_estimate.append({'x': x, 'y': y_average}, ignore_index=True)

    return average_estimate


def neighborhood_estimate(points, window):

    neighborhood_estimate = pd.DataFrame(columns=['x', 'y'])

    for x in points['x']:

        y_points = points[(points['x'] > x - window) & (points['x'] < x + window)]

        y_neighborhood_average = np.mean(y_points['y'])
        
        neighborhood_estimate = neighborhood_estimate.append({'x': x, 'y': y_neighborhood_average}, ignore_index=True)
      
    return neighborhood_estimate


if __name__=='__main__':

    # func = lambda x: -(np.square(x) - (10*x))

    # func = lambda x:  (10*x)

    func = lambda x:  (x**2) + 10
    max_random_points=5
    min_point=0
    max_point=10
    resolution=0.05
    error_threshold=5

    function, points = generate_data(func, max_random_points, min_point, max_point, resolution, error_threshold)

    resolution = resolution*20

    filtered_points = extract_points(min_point, max_point, resolution)

    average_estimate = average_estimate(filtered_points)

    window = resolution*5
    
    neighborhood_estimate = neighborhood_estimate(filtered_points, window)

    
    fig,ax = plt.subplots(1,1)

    function.plot(x='x', y='y', ax=ax, kind='line', color='blue', label='function')

    filtered_points.plot(x='x', y='y', kind='scatter', ax=ax, color='gainsboro', label='points')

    average_estimate.plot(x='x', y='y', kind='line', ax=ax, color='red', label='estimate')
    
    neighborhood_estimate.plot(x='x', y='y', kind='line', ax=ax, color='orange', label='estimate')
    plt.show()
