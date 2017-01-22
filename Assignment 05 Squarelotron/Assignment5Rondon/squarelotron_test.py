import unittest
from squarelotron import *

class TestSquarelotron(unittest.TestCase):

    def test_make_squarelotron(self):
        list = []
        for i in range(1, 26):
            list.append(i)
        self.assertEqual((1), make_squarelotron(list)[0][0])
        self.assertEqual((25), make_squarelotron(list)[4][4])
        self.assertEqual((13), make_squarelotron(list)[2][2])

    def test_make_list(self):
        squarelotron = ([[ 1,  2,  3,  4,  5],
                         [ 6,  7,  8,  9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18, 19, 20],
                         [21, 22, 23, 24, 25]])
        self.assertEqual((1), make_list(squarelotron)[0])
        self.assertEqual ((25), make_list(squarelotron)[24])
        self.assertEqual((12), make_list(squarelotron)[11])

    def test_swap(self):
        list = [1, 2, 3, 4]
        new_list = [1, 4, 3, 2]
        swap(list, 1, 2)
        self.assertEqual(new_list, list)

    def test_upside_down_flip(self):
        squarelotron = ([[ 1,  2,  3,  4,  5],
                         [ 6,  7,  8,  9, 10],
                         [11, 12, 13, 14, 15],
                         [16, 17, 18, 19, 20],
                         [21, 22, 23, 24, 25]])

        ring = "inner"
        u_d_inner_squarelotron =  ([[ 1,  2,  3,  4,  5],
                                    [ 6, 17, 18, 19, 10],
                                    [11, 12, 13, 14, 15],
                                    [16,  7,  8,  9, 20],
                                    [21, 22, 23, 24, 25]])
        self.assertEqual(u_d_inner_squarelotron, upside_down_flip(squarelotron, ring))

        ring = "outer"
        u_d_outer_squarelotron =  ([[21, 22, 23, 24, 25],
                                    [16,  7,  8,  9, 20],
                                    [11, 12, 13, 14, 15],
                                    [ 6, 17, 18, 19, 10],
                                    [ 1,  2,  3,  4,  5]])
        self.assertEqual(u_d_outer_squarelotron, upside_down_flip(squarelotron, ring))

    def test_left_right_flip(self):
        squarelotron = ([[ 1,  2,  3,  4,  5],
                          [ 6,  7,  8,  9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]])
        ring = "inner"
        l_r_inner_squarelotron =  ([[ 1,  2,  3,  4,  5],
                                    [ 6,  9,  8,  7, 10],
                                    [11, 14, 13, 12, 15],
                                    [16, 19, 18, 17, 20],
                                    [21, 22, 23, 24, 25]])
        self.assertEqual(l_r_inner_squarelotron, left_right_flip(squarelotron, ring))
        
        ring = "outer"
        l_r_outer_squarelotron =  ([[ 5,  4,  3,  2,  1],
                                    [10,  7,  8,  9,  6],
                                    [15, 12, 13, 14, 11],
                                    [20, 17, 18, 19, 16],
                                    [25, 24, 23, 22, 21]])
        self.assertEqual(l_r_outer_squarelotron, left_right_flip(squarelotron, ring))


    def test_inverse_diagonal_flip(self):
        squarelotron =  ([[ 1,  2,  3,  4,  5],
                          [ 6,  7,  8,  9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]])
       
        ring = "inner"
        i_d_inner_squarelotron =  ([[ 1,  2,  3,  4,  5],
                                    [ 6, 19, 14,  9, 10],
                                    [11, 18, 13,  8, 15],
                                    [16, 17, 12,  7, 20],
                                    [21, 22, 23, 24, 25]])
        self.assertEqual(i_d_inner_squarelotron, inverse_diagonal_flip(squarelotron, ring))

        ring = "outer"
        i_d_outer_squarelotron =  ([[25, 20, 15, 10, 5],
                                    [24,  7,  8,  9, 4],
                                    [23, 12, 13, 14, 3],
                                    [22, 17, 18, 19, 2],
                                    [21, 16, 11,  6, 1]])
        self.assertEqual(i_d_outer_squarelotron, inverse_diagonal_flip(squarelotron, ring))

    def test_main_diagonal_flip(self):
        squarelotron =  ([[ 1,  2,  3,  4,  5],
                          [ 6,  7,  8,  9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]])

        ring = "inner"
        m_d_inner_squarelotron =  ([[ 1,  2,  3,  4,  5],
                                    [ 6,  7, 12, 17, 10],
                                    [11,  8, 13, 18, 15],
                                    [16,  9, 14, 19, 20],
                                    [21, 22, 23, 24, 25]])
        self.assertEqual(m_d_inner_squarelotron, main_diagonal_flip(squarelotron, ring))
        ring = "outer"
        m_d_outer_squarelotron =  ([[ 1,  6, 11, 16, 21],
                                    [ 2,  7,  8,  9, 22],
                                    [ 3, 12, 13, 14, 23],
                                    [ 4, 17, 18, 19, 24],
                                    [ 5, 10, 15, 20, 25]])
        self.assertEqual(m_d_outer_squarelotron, main_diagonal_flip(squarelotron, ring))

    def test_print_squarelotron(self):
        """this is a personal test"""
        squarelotron =  ([[ 1,  2,  3,  4,  5],
                          [ 6,  7,  8,  9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]])
        print_squarelotron(squarelotron)

unittest.main()
