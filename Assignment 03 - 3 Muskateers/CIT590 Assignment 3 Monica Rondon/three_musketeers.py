# The Three Musketeers Game
# by David Matuszek and Monica Rondon.

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],    #row 0 [col_0, col_1, ... col_4]
              [r, r, r, r, r],    #row 1
              [r, r, m, r, r],    #row 2
              [r, r, r, r, r],    #row 3
              [m, r, r, r, r] ]   #row 4

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= "A" and s[0] <= "E"
    assert s[1] >= "1" and s[1] <= "5"
    row_lookup = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4}
    col_lookup = {"1" : 0, "2" : 1, "3" : 2, "4" : 3, "5" : 4}
    return (row_lookup[s[0]], col_lookup[s[1]])

def location_to_string(location):
    """Returns the string representation of a location."""
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4
    row_lookup = {0 : "A", 1 : "B", 2 : "C", 3 : "D", 4 : "E"}
    col_lookup = {0 : "1", 1 : "2", 2 : "3", 3 : "4", 4 : "5"}
    return (row_lookup[location[0]] + col_lookup[location[1]])

def at(location):
    """Returns the contents of the board at the given location."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board as tuples."""
    list = []
    #for every row in the range 0 to 5
    for row in range(0, 5):
        #run the following code once using the value of 0 then again
        #using the value of 1 etc... 2,3,4
        #then start a SECOND loop"""
        for col in range(0, 5): 
            """run once with the col value of 0
            # then with 1...""" 
            list.append((row, col)) 
    return list  

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    (row, col) = location
    #if we know the incoming location is 0, 0
    #and we know the direction is the string 'right'
    #then we know that the result should be 0, 1
    if direction == "right":
        location = (row, col + 1)
    if direction == "left":
        location = (row, col - 1)
    if direction == "up":
        location = (row - 1, col)
    if direction == "down":
        location = (row + 1, col)
    return location

def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    return is_legal_location(adjacent_location(location, direction)) 

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    (row, col) = location
    if row  >= 0 and row <= 4:
        if col >= 0 and col <= 4:
            return True     
    return False 

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    assert at(location) == 'M'
    #is the move in the board 
    if is_within_board(location, direction):
    #is the move to a location == "R" 
        if at(adjacent_location(location, direction)) == "R":
            return True 
    return False

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    assert at(location) == 'R'
     # is the move in the board
    if is_within_board(location, direction):
     # is the move to a location == "-"
        if at(adjacent_location(location, direction)) == "-":
            return True 
    return False

def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location"""
    what_at_location = at(location)
    if what_at_location == "M":
        return is_legal_move_by_musketeer(location, direction)
    elif what_at_location == "R":
        return is_legal_move_by_enemy(location, direction)
    else:
        return False         


def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    # is there a move? 
    possible_moves = []
    if is_legal_move(location, "left"):
        possible_moves.append("left")
    if is_legal_move(location, "right"):
        possible_moves.append("right")
    if is_legal_move(location, "up"):
        possible_moves.append("up")
    if is_legal_move(location, "down"):
        possible_moves.append("down")
    return possible_moves

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available."""
    can_move_up = is_legal_move(location, "up")
    can_move_down = is_legal_move(location, "down")
    can_move_right = is_legal_move(location, "right")
    can_move_left = is_legal_move(location, "left")
    return can_move_up or can_move_down or can_move_right or can_move_left

def make_move(location, direction):
    """Moves the piece in location in the indicated direction."""
    # we know that the square we move out of will always be empty
    # we know that MAKE_MOVE will only ever be called on a LEGAL move 
    # we MUST write the VALUE AT location in the NEW location
    current_value_at_location = at(location)  
    #2 - GET board store this in a temporary variable
    current_board = get_board()
    #3 - set the value in LOCATION to blank ON the current_board
    #    (hint, location has a ROW and COLUMN)
    (row, col) = location
    current_board[row][col] = "-"
    #4 - get the destination location 
    destination_location = adjacent_location(location, direction)
    #5 - SET the value at the destination, to (#1) value
    (row, col) = destination_location   
    current_board[row][col] = current_value_at_location
    #6 - SAVE the updated board (using set_board)
    set_board(current_board)
   

def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    all_possible_moves = []
    for location in all_locations():
        # all locations example: [(0,0), (0,1), (0, 2),  ... (4, 4)]
        # so on the first loop, location in all location would be (0, 0)
        current_value_at_location = at(location) 
        if current_value_at_location == player: 
            possible_moves = possible_moves_from(location)
            # example list: ['left', 'right', 'up', 'down']
            for move in possible_moves: # this can happen 0 to 4 times
                # the first time, with the above example the move would be 'left'
                all_possible_moves.append((location, move))
                # so where we are here the thing we append would be
    return all_possible_moves

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is."""
    any_legal_move = all_possible_moves_for(who)
    if len(any_legal_move) == 0:
        return False
    else:
        return True

def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    all_moves = all_possible_moves_for(who)
    return all_moves[0]

def is_enemy_win(): 
    """Returns True if all 3 Musketeers are in the same row or column."""
    list_of_M = []
    for location in all_locations():
        if at(location) == "M":
            list_of_M.append(location)
    (M1, M2, M3) = list_of_M
    if M1[0] == M2[0] and M2[0] == M3[0]:
        return True
    if M1[1] == M2[1] and M2[1] == M3[1]:
        return True
    else:
        return False

#---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break
def main():
    start()
    
if __name__ == '__main__': 
    main()
