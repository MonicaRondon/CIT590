
computer_score = 0
human_score = 0


def computer_move(computer_score, human_score):
    comp_current_score = 0
# This function simulates the computer's turn by rolling the die and displaying the results
# The function may use its parameters in order to play more intelligently (for example, it may wish to gamble more agressively if it is behind)
    while computer_score - human_score <= 15:
        num_rolled = roll ()
        if num_rolled != 1:
            comp_current_score = comp_current_score + num_rolled
            computer_score = computer_score + comp_current_score
        else:
            comp_current_score = 0
            computer_score = computer_score + comp_current_score

computer_move()

        
