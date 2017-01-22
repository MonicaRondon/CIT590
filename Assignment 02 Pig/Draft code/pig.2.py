""" This is a program written by Monica Rondon that is called "Pig".
"Pig" simulates the game Pig.
In the game Pig, two players each take turns rolling a six-sided die.
When it is a player's turn they may roll the die as many times as they wish or until they roll a 1.
Each number the player rolls in a turn, except a 1, is added to their score.
If the player rolls a 1, their score for this turn is zero, and their turn ends.
The score from each turn is cumulative.
The first player to reach or exceed a score of 100 wins. """

def main():
    """function executes program"""
    start_game()
    
def start_game():
    """function starts game"""
    player_response = input("Hello, would you like to play a game?\nEnter Y or N followed by the 'Enter' key: ")
    if len(player_response) == 0:
        print("Sorry, I didn't catch that. ")
        start_game()
    if player_response == "Y" or "y":
        instructions()
    elif player_response == "N" or "n":
        print("That is a shame. ")
    else:
        print("Sorry, I didn't catch that. ")
        start_game()
            

def instructions():
    """function gives the user instructions on how to play the game"""
    print("Let's play Pig!\nPig is a simple game.\nYou and the computer take\
turns rolling a die.\nEach turn you can roll the die as many times as you\
want.\nAny number you roll, two to six, is added to your score.\n\
But if you roll a one you lose your turn and you score for that turn is zero!\n\
The object of the game is to be the first to reach a score of 100 or greater.\n\
The computer always starts first.\nIf the computer reaches 100 first, you get\
one more turn to try and beat their score.\n ")
    play_game()
   

def play_game():
    """function sets the conditions for when game play is active"""
    computer_score = 0
    human_score = 0
    while not is_game_over(computer_score, human_score):
        computer_score = computer_move(computer_score, human_score)
        human_score = human_move(computer_score, human_score)
    show_results(computer_score, human_score)
    
        
def computer_move(computer_score, human_score):
    """ function simulates the computer's turn by rolling the die and displaying the results """
    current_comp_score = computer_score
    total_rolls = 0
    num_rolled = roll ()
    print ("Computer rolled a:", num_rolled)
    if num_rolled != 1:
        current_comp_score = num_rolled + current_comp_score
        total_rolls = total_rolls + 1
        while not is_game_over(current_comp_score, human_score): 
            if current_comp_score - human_score >= 15:
                print ("Computer's total for this round is:", current_comp_score)
                return current_comp_score
            if  total_rolls <= 5:
                num_rolled = roll ()
                print ("Computer rolled a:", num_rolled)
                if num_rolled != 1:
                    current_comp_score = num_rolled + current_comp_score
                    total_rolls = total_rolls + 1
            else: 
                print ("Computer rolled a:", num_rolled)
                return computer_score
    else:
        
        return computer_score
    
 
def human_move(computer_score, human_score):
    current_human_score = human_score
    print ("Your current score is: ", current_human_score)
    print ("The computer's score is: ", computer_score)
    current_human_score = one_human_turn(current_human_score)
    if current_human_score == 0:
        return human_score
    else:
        return current_human_score

def one_human_turn(current_human_score):
    if ask_yes_or_no("Would you like to roll the die?\nPlease enter 'Y' or 'N': "):
        num_rolled = roll ()
        if num_rolled != 1:
            current_human_score = current_human_score + num_rolled
            print ("You rolled a:", num_rolled)
            return one_human_turn(current_human_score)
        else:
            print ("Oh no! You rolled a 1.\nYou get no points this turn.")
            return 0
    else:
        return current_human_score

def is_game_over(computer_score, human_score):
    if computer_score == human_score:
        return False
    if computer_score >= 100 or human_score >= 100:
        return True
    else:
        return False

def roll():
    import random
    return random.randint(1,6)

def ask_yes_or_no(prompt):
    human_response = input(prompt)
    if human_response == "N" or human_response == "n":
        return False
    elif human_response == "Y" or human_response == "y":
        return True
    else:
        ask_yes_or_no(prompt)

def show_results(computer_score, human_score):
    # Tells whether the human won or lost, and by how much. (Call this when the game has ended.)
    if human_score > computer_score:
        print ("Congratulations, you won!\nYour score:", human_score, "Computer's score is:", computer_score)
    else:
        print ("So sorry, the machine has triumphed!\nYour score:", human_score, "Computer's score is:", computer_score)

main()
