def main():
    welcome_instructions()
    play_game()

def welcome_instructions():
    """provides an overview of the game and instructions for game play"""
    squarelotron = ([[ 1,  2,  3,  4,  5],
                     [ 6,  7,  8,  9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]])
    print( "Hello.\nThis is a game called 'Squarelotron'\nThe game involves\
 two sets of square rings that move, with a stationary centre.\n\
Check it out:")
    print_squarelotron(squarelotron)
    print("\nYou can flip the outer and inner rings four different ways:\n\
\nUpside Down\nLeft to Right\nAlong the Main Diagonal\nAlong the Inverse\
 Diagonal.")

def play_game():
    """asks the player if they want to play and calls the game"""
    squarelotron = ([[ 1,  2,  3,  4,  5],
                     [ 6,  7,  8,  9, 10],
                     [11, 12, 13, 14, 15],
                     [16, 17, 18, 19, 20],
                     [21, 22, 23, 24, 25]])
    player_response = input("\nPlay Squarelotron?\n\
Enter Y or N followed by the 'Enter' key:")
    if len(player_response) == 0:
        print("\nSorry, I didn't catch that.")
        play_game()
    else:
        player_response = player_response[0].lower()
        if player_response == "y":
            choose_flip(squarelotron)
        elif player_response == "n":
            print("Your loss. ")
        else:
            print("\nSorry, I didn't catch that.")   
            play_game()  

def flip_again_start_over_quit(squarelotron):
    """after a flip, let's player choose to flip again, start  or quit"""
    player_response = input("\nIf you want to flip again enter F.\n\
If you want to start over enter S.\nIf you want to quit enter Q:\n")
    player_response = player_response.upper()
    if player_response == "F":
        choose_flip(squarelotron)
    elif player_response == "S":
        play_game()
    elif player_response == "Q":
        return
    else:
        print("\nSorry, I didn't catch that.")  
        flip_again_start_over_quit(squarelotron)

def print_squarelotron(squarelotron):
    """displays the sqarelotron"""
    print()
    for row in squarelotron:
        display_row = ""
        for i in row:
            if i < 10:
                display_row = display_row + ("  " + str(i))
            else:
                display_row = display_row + " " +str(i)
        print(display_row)

def choose_flip(squarelotron):
    """asks for user input on which flip to do and returns the flipped
    squarelotron"""
    new_squarelotron = []
    print("\nHow do you want to flip the Squarelotron?\nEnter one direction:\n")
    #dir = direction
    dir = input("Upside Down = UD, Left to Right = LR, Along the\
 Main Diagonal = MD, Along the Inverse Diagonal = ID:\n")
    if len(dir) != 2:
        print("\nSorry, I didn't catch that.")
        choose_flip(squarelotron)
    else:
        dir = dir.upper()
    if dir != "UD" and dir != "ID" and dir != "LR" and dir != "MD":
        print("\nSorry, I didn't catch that.")
        choose_flip(squarelotron)
    ring = input("\nWhich ring do you want to flip?\nEnter inner or outer:\n")
    if len(ring) != 5:
        print("\nSorry, I didn't catch that.")
        choose_flip(squarelotron)
    else:
        ring = ring.lower()
    if ring != "inner" and ring != "outer":
        print("\nSorry, I didn't catch that.")
        choose_flip(squarelotron)
    if dir == "UD":
        new_squarelotron = upside_down_flip(squarelotron, ring)
    if dir == "LR":
        new_squarelotron = left_right_flip(squarelotron, ring)
    if dir == "MD":
        new_squarelotron = main_diagonal_flip(squarelotron, ring)
    if dir == "ID":
        new_squarelotron = inverse_diagonal_flip(squarelotron, ring)
    print_squarelotron(new_squarelotron)
    flip_again_start_over_quit(new_squarelotron)


def make_squarelotron(list):
    """Given a "flat" list of 25 numbers, make and return a squarelotron"""
    assert len(list) == 25
    # take list of 25 numbers
    # tell computer to take the first 5 numbers and put into 1 list
    # tell computer to take the next 5 numbers and put into 1 list
    # do this three more times
    # return new list of lists
    squarelotron = []
    for i in range(0, 25, 5):
        squarelotron.append(list[i: i + 5])
    return squarelotron

def make_list(squarelotron):
    """Given a squarelotron, makes and returns a flat list of 25 numbers""" 
    list = []
    #take squarelotron list, add the first row to the empty list
    #add the second row to the empty list
    #do this three more times
    #return full flat list
    for row in squarelotron:
        list = list + row
    return list

def swap(list, index, distance):
    """swaps two spots on a FLAT list based on a starter index and distance
    between the starter and end index"""
    hold = list[index]
    list[index] = list[index + distance] #flips location value
    list[index + distance] = hold

def upside_down_flip(squarelotron, ring):
    """Performs the Upside-Down Flip of the squarelotron 
    and returns the new squarelotron."""
    new_squarelotron = make_list(squarelotron)
    if ring == "inner":
        for i in range(6,9):
            swap(new_squarelotron, i, 10)
        return make_squarelotron(new_squarelotron)
    if ring == "outer":
        for i in range(0,5):
            swap(new_squarelotron, i, 20)
        swap(new_squarelotron, 5, 10)
        swap(new_squarelotron, 9, 10)
    return make_squarelotron(new_squarelotron)

def left_right_flip(squarelotron, ring):
    """Performs the Left-Right Flip of the squarelotron
    and returns the new squarelotron. """
    new_squarelotron = make_list(squarelotron)
    if ring == "inner":
        for i in range (6, 17, 5):
            swap(new_squarelotron, i, 2)
        return make_squarelotron(new_squarelotron)
    if ring == "outer":
        new_squarelotron[0:5] = reversed(new_squarelotron[0:5])
        new_squarelotron[20:25] = reversed(new_squarelotron[20:25])
        for i in range (5, 16, 5):
            swap(new_squarelotron, i, 4)
    return make_squarelotron(new_squarelotron)

def inverse_diagonal_flip(squarelotron, ring):
    """Performs the Main Inverse Diagonal of the squarelotron, 
    and returns the new squarelotron.""" 
    new_squarelotron = make_list(squarelotron)
    if ring == "inner":
        swap(new_squarelotron, 6, 12)
        for i in range(7, 12, 4):
            swap(new_squarelotron, i, 6)
        return make_squarelotron(new_squarelotron)
    if ring == "outer":
        for i in range(0, 4):
            swap(new_squarelotron, i, (24 - (6 * i)))
        for i in range(5, 16, 5):
            swap(new_squarelotron, i, (24 - (6 * (int(i/5)))))
    return make_squarelotron(new_squarelotron)

def main_diagonal_flip(squarelotron, ring):
    """Performs the Main Diagonal Flip of the squarelotron, 
    and returns the new squarelotron.""" 
    new_squarelotron = make_list(squarelotron)
    if ring == "inner":
        swap(new_squarelotron, 8, 8)
        for i in range(7, 14, 6):
            swap(new_squarelotron, i, 4) 
        return make_squarelotron(new_squarelotron)
    if ring == "outer":
        for i in range(1,5):
            swap(new_squarelotron, i, (4*i))
        for i in range(9, 20, 5):
            multiplier =  int((i - 9) / 5)*4
            swap(new_squarelotron, i, (12 - multiplier))
    return make_squarelotron(new_squarelotron)

if __name__ == "__main__":
    main()
