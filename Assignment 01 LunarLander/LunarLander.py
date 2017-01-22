""" This is a Lunar Lander game by Monica Rondon. The purpose of the game is to
safely land your Lunar Lander on the moon.The Lunar Lander is 1000 meters above
the moon's surface. Gravity is pulling it down at an increasing velocity. Everytime the user burns fuel,
the velocity slows. The user has 1000 litres of fuel. The user must input the correct amount of
fuel to burn at the right time to land safely on the moon's surface. """

print("Welcome to Lunar Lander.\nYou are in a spaceship far above the moon.\nYou need to land your craft safely on the moon's surface.\nBurn fuel to counteract gravity to land your craft safely.\n")

def play_game(play_game_text):
    # this function checks to see if the user wants to play the game
    user_response = input(play_game_text)
    if len(user_response) == 0:
    # solution to ensuring one letter is inputted from stackoverflow
        print("Incorrect response.\n ")   
        play_game("Enter Y or N, followed by the 'Enter' key.\n ")
    else:
        user_response = user_response[0].lower()
        # makes sure just the first letter is stored as user_response in lowercase
        if user_response == "y":
            start_game()
        elif user_response == "n":
            print("Your loss. ")
        else:
            print("Incorrect response.\n ")   
            play_game("Enter Y or N. ")

global current_altitude
global current_fuel
global current_velocity
""" solution to declaring variables as global to allow variables to be altered in
multiple functions found from stackoverflow """

def start_game():
# this function is primary piece of code that simulates the game play
    global current_altitude
    current_altitude = 1000
    global current_fuel
    current_fuel = 1000
    global current_velocity
    current_velocity = 0
    while current_altitude > 0:
        report_user_status()
        fuel_burned = ask_user_to_burn_fuel()
        process_gravity_and_fuel(fuel_burned)
        assess_safe_landing()
    play_game("Do You Want to Play Again?\n\nEnter Y or N, followed by the 'Enter' key. ")
      
def report_user_status():
    # this function tells the user their current_altitude, current_velocity, current_fuel
    print("Your current altitude is:", current_altitude)
    print("Your current velocity is:", current_velocity)
    print("Your current fuel level is:", current_fuel)

def ask_user_to_burn_fuel():
    """ this function asks the user how much fuel they want to burn each turn and
    calculates the fuel_burned variable to be used as a parameter for the next function. """
    global current_fuel 
    fuel_input = input("How much fuel would you like to burn?\n\nEnter a number, followed by the 'Enter' key:\n ")
    if len(fuel_input) == 0:
        fuel_input = 0
    # this ensures if the user just hits 'Enter' the game will still run
    else:
        fuel_input = int(fuel_input)
    if fuel_input <= 0:
        fuel_input = 0
    elif fuel_input > current_fuel:
        fuel_input = current_fuel
    current_fuel = current_fuel - fuel_input
    return fuel_input
    # returns the fuel_input so that it can be passed to the next function

def process_gravity_and_fuel(fuel_burned):
    # this function calculates how far the Lunar Lander has fallen and how much fuel has been burned
    global current_velocity
    current_velocity = current_velocity + 1.6 - 0.15  *fuel_burned
    global current_altitude
    current_altitude = current_altitude - current_velocity

def assess_safe_landing():
    """ this function uses the variables current_alitude and current_velocity to determine when
    the user has landed and if they landed safely """
    if current_altitude <= 0:
        if current_velocity <= 10:
            win_condition()
        else: 
            lose_condition()

def win_condition():
    # this function let's the user know they have landed safely
    global current_altitude 
    current_altitude = 0
    global current_velocity
    current_velocity = 0
    report_user_status()
    print("\n")
    print("Congratulations cosmonaut!\nYou have landed safely on the moon! ")

def lose_condition():
    # this function let's the user know they crashed
    crater_size = current_velocity * 2
    print("\n")
    print("Oh no!\nYou have crashed on the moon.\nYou made a crater that is " + str(crater_size) + " meters deep! ")
    print("\n")
play_game("Would you like to play Lunar Lander?\n\nEnter Y or N, followed by the 'Enter' key.\n ")
