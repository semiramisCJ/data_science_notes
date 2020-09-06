from random import randint
from math import sqrt
import numpy as np

# TO DO: Generalize the algorithm
# For the moment, each pair of elements is clustered with
# another one that is its closest instead of performing
# the expected clustering
# We need to accept also uneven sized lists or coordinates

def euclidean_distance(coords_1, coords_2):
    x1, y1 = coords_1
    x2, y2 = coords_2
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def calculate_distances_all_vs_all(list_of_coords):
    n = len(list_of_coords)
    distances = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            coords_1 = list_of_coords[i]
            coords_2 = list_of_coords[j]
            if coords_1 == coords_2:
                distances[i, j] = np.nan
            else:
                distances[i, j] = round(euclidean_distance(coords_1, coords_2), 2)
    return distances

def find_minimal_pairs(distances):
    for i in range(len(distances)):
        np.nanmin(distances)
        i, j = np.where(distances == np.nanmin(distances))[0]
    return i, j

def hierarchical_clustering(list_of_coords):
    clustered_list = []
    while(not np.all(np.isnan(list_of_coords))):
        distances = calculate_distances_all_vs_all(list_of_coords)
        i, j = find_minimal_pairs(distances)
        distances[i, j] = distances[j, i] = np.nan
        clustered_list.append([list_of_coords[i], list_of_coords[j]])
        list_of_coords[i] = list_of_coords[j] = (np.nan, np.nan)
        print(clustered_list)
    return clustered_list

if __name__ == "__main__":
    size = 6
    #x = [randint(0,50) for i in range(size)]
    #y = [randint(0,50) for i in range(size)]
    #list_of_coords = list(zip(x, y))
    list_of_coords = [(42, 39), (1, 19), (26, 24), (13, 13), (39, 22), (26, 29)]
    print(list_of_coords)
    distances = calculate_distances_all_vs_all(list_of_coords)
    print(distances)
    hierarchical_clustering(list_of_coords)
