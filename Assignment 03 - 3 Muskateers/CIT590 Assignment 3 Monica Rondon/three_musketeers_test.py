import unittest
from three_musketeers import *

left = "left"
right = "right"
up = "up"
down = "down"
M = "M"
R = "R"
_ = "-"

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), "R")
        self.assertEqual(at((0, 4)), "M")

    def test_set_board(self):
        self.assertEqual(at((0, 0)), "-")
        self.assertEqual(at((1, 2)), "R")
        self.assertEqual(at((1, 3)), "M")

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((0, 4), string_to_location("A5"))
        self.assertEqual((4, 0), string_to_location("E1"))
        self.assertNotEqual ((1, 3), string_to_location("A3"))

    def test_location_to_string(self):
        self.assertEqual(("A5"), location_to_string((0, 4)))
        self.assertNotEqual(("C1"), location_to_string((3, 0)))

    def test_at(self):
        self.assertEqual(("-"), at((0,0)))
        self.assertNotEqual((M), at((4,1)))
            
    def test_all_locations(self):
        self.assertEqual((25), len(all_locations()))
        self.assertEqual((0,0), all_locations()[0])
        self.assertEqual((4,4), all_locations()[24])
        self.assertEqual((2,3), all_locations()[13])            
        
    def test_adjacent_location(self):
        self.assertEqual((0, 1), adjacent_location((0, 0), right))
        self.assertEqual((4, 2), adjacent_location((4, 3), left)) 
        self.assertEqual((3, 0), adjacent_location((4,0), up))
        self.assertEqual((1, 4), adjacent_location((0,4), down)) 

    def test_is_within_board(self):
        self.assertTrue(is_within_board((0,0), right), "this should be true because it is within the board")
        self.assertFalse(is_within_board((0,0), left), "this should be false because it off the board")
        self.assertTrue(is_within_board((4,4), up),"this should be true because it is within the board")
        self.assertFalse(is_within_board((4,0), down), "this should be false because it is off the board")

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((0,0)), "should be true")
        self.assertTrue(is_legal_location((4,4)), "should be true")
        self.assertTrue(is_legal_location((0,4)), "should be true")
        self.assertTrue(is_legal_location((4,0)), "should be true")
        self.assertFalse(is_legal_location((0,5)), "should be false")
        self.assertFalse(is_legal_location((-1, 0)), "should be false")
        self.assertFalse(is_legal_location((4, -1)), "should be false")
        self.assertFalse(is_legal_location((4,5)), "should be false")

    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((1,3), down), "should be true")
        self.assertTrue(is_legal_move_by_musketeer((2,2), left), "should be true")
        self.assertFalse(is_legal_move_by_musketeer((0,3), left), "should be false")
        self.assertFalse(is_legal_move_by_musketeer((0,3), up), "should be false")        
        
    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((1,2), left), "should be true")
        self.assertTrue(is_legal_move_by_enemy((2,1), up), "should be true")
        self.assertFalse(is_legal_move_by_enemy((4,3), down), "should be false")
        self.assertFalse(is_legal_move_by_enemy((3,1), up), "should be false")  
  
    def test_is_legal_move(self):
        self.assertTrue(is_legal_move((2,2), up), "should be true")
        self.assertTrue(is_legal_move((2,3), right), "should be true")
        self.assertFalse(is_legal_move((0,3), right), "should be false")
        self.assertFalse(is_legal_move((0,3), down), "should be false")
        self.assertFalse(is_legal_move((0,3), up), "should be false")
        self.assertFalse(is_legal_move((3,1), up), "should be false")
        self.assertFalse(is_legal_move((2,1), right), "should be false")
        self.assertFalse(is_legal_move((4,3), down), "should be false")
  
    def test_can_move_piece_at(self):
        self.assertTrue(can_move_piece_at((1,3)), "should be true")
        self.assertTrue(can_move_piece_at((4,3)), "should be true")
        self.assertFalse(can_move_piece_at((0,3)), "should be false")
        create_board()
        self.assertFalse(can_move_piece_at((4,4)), "should be false")
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((0,3)), "should be true")
        self.assertTrue(can_move_piece_at((2,2)), "should be true")
        self.assertFalse(can_move_piece_at((0,4)), "should be false")
        

    def test_possible_moves_from(self):
        self.assertEqual(possible_moves_from((0,0)), [])
        self.assertEqual(possible_moves_from((1,3)), ["left", "down"])
        self.assertEqual(possible_moves_from((1,2)), ["left", "up"])
        self.assertEqual(possible_moves_from((0,3)), [])
        create_board()
        self.assertEqual(possible_moves_from((4,4)),[])

        

    def test_make_move(self):
        make_move((1,3), left)
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, M, _, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())
        make_move((2,1), left)
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, M, _, _],
                           [R, _, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board()) 

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        all_possible_moves_for_R = [
            ((0, 2), "left"),
            ((0, 2), "down") ]
        self.assertEqual((all_possible_moves_for_R), (all_possible_moves_for("R")))
        all_possible_moves_for_M = [
            ((0,3), "left"),
            ((0,3), "right"),
            ((1,4), "up") ]
        self.assertEqual((all_possible_moves_for_M), (all_possible_moves_for("M")))

    def test_choose_computer_move(self):
        expected_R_move = ((1,2), "left")
        self.assertEqual((expected_R_move), choose_computer_move("R"))
        expected_M_move = ((1,3), "left")
        self.assertEqual((expected_M_move), choose_computer_move("M"))




    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        create_board()
        self.assertFalse(has_some_legal_move_somewhere("R"))
        self.assertTrue(has_some_legal_move_somewhere("M"))
   
    def test_is_enemy_win(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, _, M, _],
                    [_, R, _, _, R],
                    [_, _, _, R, _] ] )
        self.assertTrue(is_enemy_win())
        set_board([ [_, M, M, M, _],
                    [_, R, _, _, _],
                    [_, _, _, _, _],
                    [_, R, _, _, R],
                    [_, _, _, R, _] ] )
        self.assertTrue(is_enemy_win())            
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(is_enemy_win())

unittest.main()
