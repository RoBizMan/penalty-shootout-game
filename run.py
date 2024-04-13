import os
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
        player_name = input(Fore.YELLOW + "Enter your name to start the game: ")
        if not player_name.isalpha():
            print(Fore.RED + "Error: Name should only contain alphabets A-Z or a-z.")
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


# Call the function to print the main menu
player_name = main_menu()
print(Fore.GREEN + f"Welcome to the game, {player_name}!")