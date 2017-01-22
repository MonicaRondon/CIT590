import unittest
from cities import *
from earth_distance import *

class TestCities(unittest.TestCase):

    def test_read_cities(self):
        file_name = "city-data.txt" 
        self.assertEqual(len(read_cities(file_name)), (50))
        self.assertEqual(read_cities(file_name)[0][0], ("Alabama"))
        self.assertEqual(read_cities(file_name)[1][1], ("Juneau"))
        self.assertEqual(read_cities(file_name)[49][2], (41.145548))
        self.assertEqual(read_cities(file_name)[49][3], (-104.802042))   
    
    def test_print_cities(self):
        """this is a personal test, not intended for the assignment"""
        #print_cities(read_cities("city-data.txt"))
        pass
    
    def test_distance_between(self):
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5)]
        distance_calc = (distance(0,0,5,5))
        self.assertAlmostEqual(distance_between(road_map[0], road_map[1]), distance_calc, 2)

    def test_print_map(self):
        """this is a personal test, not intended for the assignment"""
        #print_map(read_cities("city-data.txt"))
        pass

    def test_compute_total_distance(self):
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5)]
        # because compute_total_distance is a cycle (returns to start)
        # for a two position calculation mutliply by two for total 
        distance_calc = (distance(0, 0, 5, 5)) * 2
        self.assertAlmostEqual(compute_total_distance(road_map), distance_calc, 2)

    def test_swap_cities(self):
        #test for TWO cities
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5)]
        # because compute_total_distance is a cycle (returns to start)
        # for a two position calculation mutliply by two for total 
        distance_calc = (distance(0, 0, 5, 5)) * 2
        swap_result = swap_cities(road_map, 0, 1)
        #need to evaluate a tuple (new_road_map, new_total_distance)
        self.assertEqual(swap_result[0], [ 
            ("fake state", "fake city 2", 5, 5),
            ("fake state", "fake city 1", 0, 0)])
        self.assertAlmostEqual(swap_result[1], distance_calc, 2)
        #test for NO swap
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5)]
        # because compute_total_distance is a cycle (returns to start)
        # for a two position calculation mutliply by two for total 
        distance_calc = (distance(0, 0, 5, 5)) * 2
        swap_result = swap_cities(road_map, 0, 0)
        self.assertEqual(swap_result[0], [ 
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5)])
        self.assertAlmostEqual(swap_result[1], distance_calc, 2)
        #test for FOUR cities
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5),
            ("fake state", "fake city 3", 10, 10),
            ("fake state", "fake city 4", 25, 25)]
        swap_result = swap_cities(road_map, 0, 2)
        distance_calc_1 = distance(10, 10, 5, 5)
        distance_calc_2 = distance(5, 5, 0, 0)
        distance_calc_3 = distance(0, 0, 25, 25)
        distance_calc_4 = distance(25, 25, 10, 10)
        dclc = distance_calc_1 + distance_calc_2 + distance_calc_3 + distance_calc_4
        self.assertEqual(swap_result[0], [ 
            ("fake state", "fake city 3", 10, 10),
            ("fake state", "fake city 2", 5, 5),
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 4", 25, 25)])
        self.assertAlmostEqual(swap_result[1], dclc, 2)

    def test_swap_adjacent_cities(self):
        #test for FOUR cities
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 5, 5),
            ("fake state", "fake city 3", 10, 10),
            ("fake state", "fake city 4", 25, 25)]
        swap_adj_result = swap_adjacent_cities(road_map, 0)
        distance_calc_1 = distance(5, 5, 0, 0)
        distance_calc_2 = distance(0, 0, 10, 10)
        distance_calc_3 = distance(10, 10, 25, 25)
        distance_calc_4 = distance(25, 25, 5, 5)
        dclc = distance_calc_1 + distance_calc_2 + distance_calc_3 + distance_calc_4
        self.assertEqual(swap_adj_result[0], [ 
            ("fake state", "fake city 2", 5, 5),
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 3", 10, 10),
            ("fake state", "fake city 4", 25, 25)])
        self.assertAlmostEqual(swap_adj_result[1], dclc, 2)

    def test_find_best_cycle(self):
        road_map = [ # fake road map
            ("fake state", "fake city 1", 0, 0),
            ("fake state", "fake city 2", 25, 25),
            ("fake state", "fake city 3", 10, 10),
            ("fake state", "fake city 4", 5, 5)]
        distance_calc_1 = distance(0, 0, 5, 5)
        distance_calc_2 = distance(5, 5, 10, 10)
        distance_calc_3 = distance(10, 10, 25, 25)
        distance_calc_4 = distance(25, 25, 0, 0)
        shortest_distance = distance_calc_1 + distance_calc_2 + distance_calc_3 + distance_calc_4
        best_cycle = find_best_cycle(road_map)
        best_distance = compute_total_distance(best_cycle)
        self.assertAlmostEqual(best_distance, shortest_distance, 2)
        file_name = "city-data.txt"
        road_map = read_cities(file_name)
        original_total_distance = compute_total_distance(road_map)
        best_cycle = find_best_cycle(road_map)
        best_distance = compute_total_distance(best_cycle)
        self.assertLessEqual(best_distance, original_total_distance)
    


unittest.main()
    
 
