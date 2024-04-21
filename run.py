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
                Fore.RED + "\nError: Name should only "
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
    \n""" + Fore.RESET)
    print("==================== Instructions: ====================\n")
    print("1. A coin toss will decide who goes first.")
    print("2. When shooting, choose your target to aim your shot:")
    print("    (LT, LB, C, RT, RB).")
    print("    LT - Left Top, RT - Right Top")
    print("    C- Centre")
    print("    LB - Left Bottom, RB - Right Bottom")
    print("3. When saving, choose an area you expect the opponent to aim:")
    print("    (LT, LB, C, RT, RB).")
    print("4. The game alternates between shooting and saving.")
    print("5. The game ends when the final score has a +1 goal advantage ")
    print("     to either the player or the computer opponent at the end ")
    print("     of 10 turns or more if the final score is still draw until")
    print("     a +1 goal advantage after completing each turn.")
    print("6. Have fun!\n")
    print(Fore.BLUE + "Are you ready for the penalty challenge?" + Fore.RESET)
    return request_player_name()


def toss_coin(player_name):
    """Function to handle the coin toss by asking the player
    input to choose head or tail. The coin toss will simulate
    after the player's input and the result output tells the
    player who won the coin toss and who goes first in the game"""
    clear_old_term()
    print(Fore.GREEN + f"Welcome to the game, {player_name}!\n" + Fore.RESET)
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
    """ + Fore.RESET)
    # Player input for H or T and error if H or T input not detected
    while True:
        player_choice = input(
                Fore.YELLOW + "Choose H for head or T for tail: "
                + Fore.RESET).upper()
        if player_choice not in ['H', 'T']:
            print(
                Fore.RED + "\nError: "
                "Please choose either H or T.\n" + Fore.RESET
                )
        else:
            break

    # Simulate and display the coin toss result
    coin_result = random.choice(['H', 'T'])

    # Decide who goes first based on the coin toss result
    if player_choice == coin_result:
        return player_name
    else:
        return 'Opponent'


def print_goalpost():
    """Function to print a visual representation of the goalpost"""
    print(Fore.YELLOW + """
    ===================
    || LT |  C  | RT ||
    || ------------- ||
    || LB |  C  | RB ||
    """ + Fore.RESET)


def print_goal(player, player_name):
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
    """ + Fore.RESET)


def print_save(player, player_name):
    """Function to print the save message.
    Green colour is for the player who save
    the penalty and prevent the opponet from
    being scored a goal. Red colour is for
    the player that fails to score a goal
    as the opponent saves a ball from being
    scored by the player."""
    color = Fore.RED if player == player_name else Fore.GREEN
    print(color + """
      _  _  _  _            _          _           _    _  _  _  _  _    _
    _(_)(_)(_)(_)_        _(_)_       (_)         (_)  (_)(_)(_)(_)(_)  (_)
   (_)          (_)     _(_) (_)_     (_)         (_)  (_)              (_)
   (_)_  _  _  _      _(_)     (_)_   (_)_       _(_)  (_) _  _         (_)
     (_)(_)(_)(_)_   (_) _  _  _ (_)    (_)     (_)    (_)(_)(_)        (_)
    _           (_)  (_)(_)(_)(_)(_)     (_)   (_)     (_)
   (_)_  _  _  _(_)  (_)         (_)      (_)_(_)      (_) _  _  _  _    _
     (_)(_)(_)(_)    (_)         (_)        (_)        (_)(_)(_)(_)(_)  (_)
    """ + Fore.RESET)


def print_win(player):
    """Function to print the win message.
    If the player wins the game, then
    the win message will display."""
    print(Fore.YELLOW + """
     _             _    _  _  _    _           _    _
    (_)           (_)  (_)(_)(_)  (_) _       (_)  (_)
    (_)           (_)     (_)     (_)(_)_     (_)  (_)
    (_)     _     (_)     (_)     (_)  (_)_   (_)  (_)
    (_)   _(_)_   (_)     (_)     (_)    (_)_ (_)  (_)
    (_)  (_) (_)  (_)     (_)     (_)      (_)(_)
    (_)_(_)   (_)_(_)   _ (_) _   (_)         (_)   _
      (_)       (_)    (_)(_)(_)  (_)         (_)  (_)
    """ + Fore.RESET)


def print_lose(player):
    """Function to print the lose message.
    If the player loses the game, then
    the lose message will display."""
    print(Fore.BLUE + """
    _                  _  _  _  _        _  _  _  _      _  _  _  _  _    _
   (_)               _(_)(_)(_)(_)_    _(_)(_)(_)(_)_   (_)(_)(_)(_)(_)  (_)
   (_)              (_)          (_)  (_)          (_)  (_)              (_)
   (_)              (_)          (_)  (_)_  _  _  _     (_) _  _         (_)
   (_)              (_)          (_)    (_)(_)(_)(_)_   (_)(_)(_)        (_)
   (_)              (_)          (_)   _           (_)  (_)
   (_) _  _  _  _   (_)_  _  _  _(_)  (_)_  _  _  _(_)  (_) _  _  _  _    _
   (_)(_)(_)(_)(_)    (_)(_)(_)(_)      (_)(_)(_)(_)    (_)(_)(_)(_)(_)  (_)
   """ + Fore.RESET)


def choose_goalpost():
    """Function for the opponent to choose a target
    on the goalpost randomly."""
    return random.choice(['LT', 'LB', 'C', 'RT', 'RB'])


def play_game(player_name, first_player):
    """Function to play the turn-based game.
    The game ends once the game completed
    10 turns (5 turns for each player) and
    either player or opponent have one or
    more goal advantages over an opponent or
    player. Otherwise, the game will continue
    beyond 10 turns if the score result is
    the same (draw) until either player or
    opponent have a goal advantage by one after
    completing each player's turn. The game
    will end when the final score does not
    match upon completing both turns."""
    player_score = 0
    opponent_score = 0
    valid_goalposts = ['LT', 'LB', 'C', 'RT', 'RB']
    turn = 0
    # Determine the order of turns based on the coin toss
    players_order = (
        [first_player, 'Opponent'] if first_player == player_name
        else ['Opponent', player_name]
        )
    # Change this to an infinite loop until
    # the game ends based on turns or +1 goal
    while True:
        current_player = players_order[turn % 2]
        turn += 1
        clear_old_term()
        print_goalpost()
        if current_player == player_name:  # Check if the player wins coin toss
            while True:  # If win, player start penalty kick first
                print("You are the penalty kicker")
                print(
                    f"\n{Fore.BLUE}{player_name}, please "
                    f"select your target {Fore.RESET}"
                    )
                print(
                    f"{Fore.BLUE}area on the goalpost "
                    f"for your shot.{Fore.RESET}"
                    )
                player_choice = input(
                                    f"\n{Fore.YELLOW}(LT, LB, C, RT, RB): "
                                    f"{Fore.RESET}"
                                    ).upper()
                if player_choice not in valid_goalposts:  # Error handling
                    print(
                        Fore.RED + "\nError: Please choose a valid "
                        "target area (LT, LB, C, RT, RB).\n" + Fore.RESET
                        )
                else:
                    break
            opponent_choice = choose_goalpost()
            clear_old_term()
            if player_choice == opponent_choice:  # Print penalty outcome
                print(f"{Fore.YELLOW}Opponent saves the shot!{Fore.RESET}")
                print_save(current_player, player_name)
            else:
                print(f"{Fore.YELLOW}{player_name} scores!{Fore.RESET}")
                print_goal(current_player, player_name)
                player_score += 1
        else:
            opponent_choice = choose_goalpost()
            while True:  # Player take goalkeeper while opponent take kick
                print("You are the goalkeeper")
                print(
                    f"\n{Fore.BLUE}{player_name}, please "
                    f"select the area on{Fore.RESET}"
                )
                print(
                    f"{Fore.BLUE}the goalpost you "
                    f"want to defend.{Fore.RESET}"
                    )
                player_choice = input(
                                    f"\n{Fore.YELLOW}(LT, LB, C, RT, RB): "
                                    f"{Fore.RESET}"
                                    ).upper()
                if player_choice not in valid_goalposts:
                    print(
                        Fore.RED + "\nError: Please choose a valid "
                        "area (LT, LB, C, RT, RB).\n" + Fore.RESET)
                else:
                    break
            clear_old_term()
            if player_choice == opponent_choice:  # Print penalty outcome
                print(
                    f"{Fore.YELLOW}{player_name} "
                    f"saves the shot!{Fore.RESET}"
                    )
                print_save(current_player, player_name)
            else:
                print(Fore.YELLOW + "Opponent scores!" + Fore.RESET)
                print_goal(current_player, player_name)
                opponent_score += 1
        # Display the score result after taking each turn
        print(
            f"{Back.BLUE}Score: {player_name} {player_score} - "
            f"{opponent_score} Opponent{Back.RESET}\n"
            )
        # Display the penalty shootout result
        if turn >= 10 and player_score != opponent_score:
            if player_score > opponent_score:
                clear_old_term()
                print_win(player_name)
                print(
                    f"{Back.BLUE}Score: {player_name} {player_score} - "
                    f"{opponent_score} Opponent{Back.RESET}\n"
                    )
                print(
                    f"Congratulations, {player_name}! You won the game!\n"
                    )
            else:
                print_lose(player_name)
                print(
                    f"{Back.BLUE}Score: {player_name} {player_score} - "
                    f"{opponent_score} Opponent{Back.RESET}\n"
                    )
                print("The opponent won the game. Better luck next time!")
            return
        # The game will continue until it detects 10 turns has completed
        # or +1 goal advantage if the score is draw at the end
        # of 10 turns
        elif turn < 10 or player_score == opponent_score:
            while True:  # Show continue input until stop by 5(+1 adv) goal
                continue_key = input(
                        Fore.YELLOW + "Press Enter to continue: " + Fore.RESET
                        ).upper()
                if continue_key == '':
                    clear_old_term()
                    break
                else:  # Change this to allow error handling
                    print(
                        Fore.RED + "\nError: Please press Enter "
                        "to continue.\n" + Fore.RESET
                        )


def game():
    while True:
        player_name = main_menu()
        print(Fore.GREEN + f"Welcome to the game, {player_name}!" + Fore.RESET)
        first_player = toss_coin(player_name)

        # Display the result of the coin toss
        if first_player == player_name:
            print(
                f"\n{Back.GREEN}You won the coin toss!{Back.RESET}"
                f" You will go first.\n"
                )
        else:
            print(
                f"\n{Back.RED}You lost the coin toss.{Back.RESET}"
                " The opponent will go first.\n"
                )

        # Prompt the player to start the game
        while True:
            start = input(
                        Fore.YELLOW + "Press Enter to start the game: "
                        + Fore.RESET).upper()
            if start != '':
                print(
                    Fore.RED + "\nError: "
                    "Please press Enter to start the game.\n" + Fore.RESET
                    )
            else:
                break

        play_game(player_name, first_player)

        # Ask the player if they want to play again or exit
        while True:
            print(Fore.YELLOW + "\n1. Play Again\n" + Fore.RESET)
            print(Fore.YELLOW + "2. Exit Game\n" + Fore.RESET)
            player_choice = input(
                                Fore.BLUE + "Enter your choice: "
                                + Fore.RESET
                                )
            if player_choice == '1':
                break  # Break the inner loop to start a new game
            elif player_choice == '2':
                print("\nSad to see you go. Come back and play again soon!\n")
                return  # End the game
            else:
                print(
                    Fore.RED + "\nInvalid choice. "
                    "Please enter 1 or 2." + Fore.RESET
                    )


# Call the game function to start the game
game()
