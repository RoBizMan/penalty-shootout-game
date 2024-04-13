import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def main_menu():
    """Function to print the main menu of the game"""
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
    print("5. Have fun!")

# Call the function to print the main menu
main_menu()