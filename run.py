import os
import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def clear_old_term():
    """
    Clears the old output in the terminal when called.
    """
    os.system("cls" if os.name == "nt" else "clear")


def request_player_name():
    """Function to get the player's name and handle errors
    if the input contains other than A-Z alphabets or/and
    exceeds 40 characters"""
    while True:
        player_name = input(
                Fore.YELLOW + "\nEnter your name to start the game: ")
        if not player_name.isalpha():
            print(
                Fore.RED + "Error: Name should only"
                "contain alphabets A-Z or a-z."
                )
        elif len(player_name) > 40:
            print(Fore.RED + "Error: Name should not exceed 40 characters.")
        else:
            return player_name


def main_menu():
    """Function to print the main menu of the game
    and request the player to enter name before
    playing the game"""
    clear_old_term()
    print(Fore.YELLOW + """
    ____                           __   __
   / __ \\  ___    ____   ____ _   / /  / /_   __  __
  / /_/ / / _ \\  / __ \\ / __ `/  / /  / __/  / / / /
 / ____/ /  __/ / / / // /_/ /  / /  / /_   / /_/ /
/_/_____ \\___/ /_/ /_/ \\__,_/  /_/_  \\__/   \\__, /           __
  / ___/   / /_   ____   ____   / /_       /____/   __  __  / /_
  \\__ \\   / __ \\ / __ \\ / __ \\ / __/ ______ / __ \\ / / / / / __/
 ___/ /  / / / // /_/ // /_/ // /_  /_____// /_/ // /_/ / / /_
/____/  /_/ /_/ \\____/ \\____/ \\__/         \\____/ \\__,_/  \\__/
    \n""")
    print("Instructions:")
    print("1. A coin toss will decide who goes first.")
    print("2. When shooting, choose a goalpost to aim your shot")
    print("    (LT, LB, C, RT, RB).")
    print("    LT - Left Top")
    print("    LB - Left Bottom")
    print("    C - Centre")
    print("    RT - Right Top")
    print("    RB - Right Bottom")
    print("3. When saving, choose a goalpost to save the shot")
    print("    (LT, LB, C, RT, RB).")
    print("4. The game alternates between shooting and saving.")
    print("5. Have fun!\n")
    print(Fore.BLUE + "Are you ready for the penalty challenge?")
    return request_player_name()


def toss_coin(player_name):
    """Function to handle the coin toss by asking the player
    input to choose head or tail. The coin toss will simulate
    after the player's input and the result output tells the
    player who won the coin toss and who goes first in the game"""
    clear_old_term()
    print(Fore.GREEN + f"Welcome to the game, {player_name}!\n")
    print("Let's toss a coin to decide who goes first in the penalty.")
    print(Fore.BLUE + """
    HEAD           | TAIL
                   |
        ======     |    ======
      /        \\   |  / _____  \\
     |  |   |   |  | |    |     |
     |  |___|   |  | |    |     |
     |  |   |   |  | |    |     |
     |  |   |   |  | |    |     |
      \\        /   |  \\        /
        ======     |    ======
    """)
    while True:
        player_choice = input(
                Fore.YELLOW + "Choose H for head or T for tail: ").upper()
        if player_choice not in ['H', 'T']:
            print(
                Fore.RED + "\nError: "
                "Please choose either H or T.\n" + Fore.RESET
                )
        else:
            break

    # Simulate and display the coin toss result
    coin_result = random.choice(['H', 'T'])
    print(
        f"\n{Back.BLUE}The coin toss result is: "
        f"{'Head' if coin_result == 'H' else 'Tail'}{Back.RESET}\n"
    )

    # Decide who goes first based on the coin toss result
    if player_choice == coin_result:
        print(
            Back.GREEN + "You won the coin toss!" + Back.RESET,
            "You will go first.\n"
            )
    else:
        print(
            Back.RED + "You lost the coin toss." + Back.RESET,
            "The opponent will go first.\n"
            )

    # Prompt the player to start the game after
    # the outcome of the toss coin result
    while True:
        start = input(Fore.YELLOW + "Press Y to start the game: ").upper()
        if start != 'Y':
            print(
                Fore.RED + "\nError: "
                "Please press Y to start the game.\n" + Fore.RESET
                )
        else:
            break


def print_goalpost():
    """Function to print a visual representation of the goalpost"""
    print(Fore.YELLOW + """
    ===================
    || LT |  C  | RT ||
    || ------------- ||
    || LB |  C  | RB ||
    """ + Fore.RESET)


def print_goal(player):
    """Function to print the goal message.
    Green colour is for the player who takes
    the penalty and score. Red colour is for
    the player that fails to save from being
    scored by the opponent."""
    color = Fore.GREEN if player == player_name else Fore.RED
    print(color + """
       _  _  _         _  _  _  _            _          _                _
    _ (_)(_)(_) _    _(_)(_)(_)(_)_        _(_)_       (_)              (_)
   (_)         (_)  (_)          (_)     _(_) (_)_     (_)              (_)
   (_)    _  _  _   (_)          (_)   _(_)     (_)_   (_)              (_)
   (_)   (_)(_)(_)  (_)          (_)  (_) _  _  _ (_)  (_)              (_)
   (_)         (_)  (_)          (_)  (_)(_)(_)(_)(_)  (_)
   (_) _  _  _ (_)  (_)_  _  _  _(_)  (_)         (_)  (_) _  _  _  _    _
      (_)(_)(_)(_)    (_)(_)(_)(_)    (_)         (_)  (_)(_)(_)(_)(_)  (_)
    """)


# Call the various functions to play the game
player_name = main_menu()
print(Fore.GREEN + f"Welcome to the game, {player_name}!")
toss_coin(player_name)