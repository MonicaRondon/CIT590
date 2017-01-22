"""Traveling Salesman by Monica Rondon
This is a program the calculates the circuit a travling salesman may take 
between the 50 state capitals of the United States of America. The program
calculates the distance between all cities and compares circuites in order
to minimize the distance traveled."""

import random
from earth_distance import *
from math import *

def main():
    """Reads in and prints out the city data, then creates the "best" cycle and 
    prints it out."""
    file_name = "city-data.txt" 
    road_map = read_cities(file_name)
    print_cities(road_map)
    road_map = find_best_cycle(road_map)
    print_map(road_map)

def read_cities(file_name):
    """Reads in the cities from the given file_name, and returns them as a list 
    of four-tuples: [(state, city, latitude, longitude), ...]. """
    road_map = []
    with open(file_name) as inputfile:
        for line in inputfile:
            (state, city, lat, long) = line.strip().split("\t")
            road_map.append((state, city, float(lat), float(long)))
    return road_map
    
def print_cities(road_map):
    """Prints a list of cities, along with their locations. Prints only one or
    two digits after the decimal point."""
    for city in road_map:
        print("City is: {0},".format(city[1]), \
        "Latitude is: {0:.2f},".format(city[2]),\
        "Longitude is: {0:.2f}".format(city[3]))

def distance_between(city_1, city_2):
    """Calls distance function imported from earth_distance to calculate the 
    distance between two cities"""
    distance_btwn = distance(city_1[2], city_1[3], city_2[2], city_2[3])
    return distance_btwn

def compute_total_distance(road_map):
    """Returns, as a floating point number, the sum of the distances of all the 
    connections in the road_map as a cyclying, with the last city connecting to
    the first."""
    total_distance = 0
    for index in range(0, len(road_map)):
        city_1 = road_map[index]
        if index == len(road_map) - 1:
            city_2 = road_map[0] 
        else:
            city_2 = road_map[index + 1]
        distance_btwn = distance_between(city_1, city_2)
        total_distance = total_distance + distance_btwn
    return total_distance

def swap_adjacent_cities(road_map, index):
    """Takes the city at a location index in the road_map, and the city at 
    a location index+1 (or at 0, if index refers to the last element in the 
    list), swaps their positions in the road_map, computes the new total 
    distance, and returns the tuple (new_road_map, new_total_distance)."""
    index2 = index + 1
    if index2 == len(road_map):
        index2 = 0
    return swap_cities(road_map, index, index2)

def swap_cities(road_map, index1, index2):
    """Takes the city at a location index in the road_map, and the city at 
    a location index2, swaps their positions in the road_map, computes the 
    new total distance, and returns the tuple (new_road_map, 
    new_total_distance)."""
    new_road_map = road_map[:]
    if index1 != index2:
        new_road_map[index2] = road_map[index1]
        new_road_map[index1] = road_map[index2]
    new_total_distance = compute_total_distance(new_road_map)
    return (new_road_map, new_total_distance)

def find_best_cycle(road_map):
    """Uses the functions swap_cities and swap_adjacent_cities, tries 10000 
    swaps, and each time keeps the best cycle found so far."""
    new_road_map = road_map[:]
    total_distance = compute_total_distance(new_road_map)
    for index in range(0, 5000):
        max_index = len(new_road_map) - 1
        (swapped_road_map, swapped_total_distance) = swap_adjacent_cities(new_road_map, index % max_index)
        if swapped_total_distance < total_distance:
            new_road_map = swapped_road_map
            total_distance = swapped_total_distance
        index1 = random.randint(0, max_index)
        index2 = random.randint(0, max_index)
        (swapped_road_map, swapped_total_distance) = swap_cities(new_road_map, index1, index2)
        if swapped_total_distance < total_distance:
            new_road_map = swapped_road_map
            total_distance = swapped_total_distance
    return new_road_map

def print_map(road_map):
    """Prints, in an easily understandable format, the cities and their 
    connections, along with the cost for each connection and the total cost."""
    total_distance = 0
    for index in range(0, len(road_map)):
        city_1 = road_map[index]
        if index == len(road_map) - 1:
            city_2 = road_map[0] 
        else:
            city_2 = road_map[index + 1]
        distance_btwn = distance_between(city_1, city_2)
        total_distance = total_distance + distance_btwn
        print("From city: {0},".format(city_1[1]), \
        "To city: {0},".format(city_2[1]),\
        "Distance is: {0:.2f},".format(distance_btwn),\
        "Cost is: ${0:.2f}.".format(distance_btwn))
    print ("Total cost is: ${0:.2f}.".format(total_distance))

if __name__ == '__main__': 
    main()
