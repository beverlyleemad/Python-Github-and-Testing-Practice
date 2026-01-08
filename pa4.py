import random  # for selecting a random word
import termcolor as colored  # for adding colored output
import time  # for adding pauses

def load_wordlist(filename):
    """
    Load a list of words from a file and create a dictionary with numeric keys.

    Parameters:
        filename (str): The name of the file containing the word list.

    Returns:
        dict: A dictionary with numeric keys and word values.
    """
    with open(filename, 'r') as file:
        word_list = file.read().split()  # Split words by spaces
    word_dict = {i: word_list[i] for i in range(len(word_list))}  # Convert list to dictionary with number keys
    return word_dict

def validate(list, word):
    """
    Validate if a word is in the given list of options.

    Parameters:
        options (list): The list of valid options.
        word (str): The word to validate.

    Returns:
        str: The validated word.
    """
    while True:
        if word in list:
            return word
        else: 
            print("Invalid word")


def is_repeat_guess(guess, previous_guesses):
    """
    Docstring for is_repeat_guess
    check whether a guess has already been used in the current game
    """
    return guess in previous_guesses

def check_guess(secret_word, guess, keyboard):
    """
    Check a player's guess against the secret word and update feedback and keyboard.

    Parameters:
        secret_word (str): The word the player is trying to guess.
        guess (str): The player's guessed word.
        keyboard (dict): A dictionary representing the state of the keyboard.

    Returns:
        tuple: Two lists containing colored feedback and emoji feedback.
    """
    secret_word = secret_word.upper()  # check uppercases (code works this way)
    guess = guess.upper()

    secret_letters = list(secret_word)  # convert secret word into a list of characters
    results = [''] * len(guess)  # feedback to display the colored result
    emoji_results = ['⬜'] * len(guess)  # feedback as emojis for visual clarity

    # check for correct letters in the correct positions
    for i, letter in enumerate(guess):
        if letter == secret_letters[i]:
            results[i] = colored.colored(letter, 'black', 'on_light_green')  # correct letter and position
            emoji_results[i] = '🟩'
            secret_letters[i] = None  # mark as used
            keyboard[letter] = 'green'

    # check for correct letters in incorrect positions
    for i, letter in enumerate(guess):
        if results[i]:
            continue  # skip already matched letters
        if letter in secret_letters:
            results[i] = colored.colored(letter, 'black', 'on_yellow')  # correct letter, wrong position
            emoji_results[i] = '🟨'
            secret_letters[secret_letters.index(letter)] = None  # mark as used
            if keyboard[letter] != 'green':
                keyboard[letter] = 'yellow'
        else:
            results[i] = colored.colored(letter, 'white', 'on_light_grey')  # incorrect letter
            if keyboard[letter] not in ['green', 'yellow']:
                keyboard[letter] = 'grey'

    return results, emoji_results

def initialize_board(rows=6, cols=5):
    """
    Creates a blank game board.

    Parameters:
        rows (int): The number of rows in the board.
        cols (int): The number of columns in the board.

    Returns:
        list: A 2D list representing the board.
    """
    return [['_' for x in range(cols)] for y in range(rows)]

def display_board(board):
    """
    Display the current state of the game board.

    Parameters:
        board (list): A 2D list representing the game board.
    """
    for row in board:
        print(' '.join(row))
    print("\n")

def display_keyboard(keyboard):
    """
    Display the keyboard with color-coded letters.

    Parameters:
        keyboard (dict): A dictionary representing the state of the keyboard.
    """
    rows = ["QWERTYUIOP", "ASDFGHJKL", "➡️ZXCVBNM⏟"]
    for row in rows:
        for letter in row:
            color = keyboard.get(letter, 'white')
            if color == 'green':
                print(colored.colored(letter, 'white', 'on_green'), end=' ')
            elif color == 'yellow':
                print(colored.colored(letter, 'black', 'on_yellow'), end=' ')
            elif color == 'grey':
                print(colored.colored(letter, 'black', 'on_light_grey'), end=' ')
            else:
                print(letter, end=' ')
        print()

def update_board(board, attempt, feedback):
    """
    Update the game board with feedback for a given attempt.

    Parameters:
        board (list): A 2D list representing the game board.
        attempt (int): The attempt number (row index) to update.
        feedback (list): The feedback to place on the board.
    """
    board[attempt] = feedback

def record_results(filename, wordle_number, attempts, emoji_board, elapsed_time):
    """
    Record game results to a file.

    Parameters:
        filename (str): The file to save results.
        wordle_number (int): The current Wordle game number.
        attempts (int): The number of attempts taken.
        emoji_board (list): The emoji feedback for the game.
    """
    with open(filename, 'a') as file:
        file.write(
            f"Bevordle #{wordle_number} {attempts}/6"
            f"({format_time(elapsed_time)})\n"
        )
        for emoji_row in emoji_board:
            file.write(''.join(emoji_row) + '\n')
        file.write('\n')  # blank line to separate games

def view_results(filename):
    """
    Displays past game results.
    Parameters:
        filename (str): The file containing game results.
    """
    viewing_results = True  # start with the condition true
    while viewing_results is True:  # continue while viewing results is true
        print("\nResults Menu:")
        print("1. View all results (A)")
        print("2. View a specific result (S)")
        print("3. Exit results menu (X)")
        time.sleep(0.5)

        choice = input("Enter your choice (A, S, or X): ").strip().lower()
        if choice == 'a':  # view all results
            print("\nAll Results:")
            time.sleep(0.5)
            with open(filename, 'r') as file:
                print(file.read())
            time.sleep(1)
        elif choice == 's':
            wordle_number = input("Enter Wordle number to view: ").strip()
            with open(filename, 'r') as file:
                results = file.read().split('\n\n')
                found = False
                for result in results:
                    if result.startswith(f"Bevordle #{wordle_number} "):
                        print(f"\n{result}")
                        found = True
                        break
                if not found:
                    print("Invalid Bevordle number.")
            time.sleep(0.5)
        elif choice == 'x':
            return("Exiting results menu...")
        else:
            print("Invalid choice. Please try again.")
            time.sleep(0.5)

wordle_number = 1  # Start with #1

# formatting time function
def format_time(seconds):
    minutes = int(seconds//60)
    secs=int(seconds % 60) #renamed to secs
    return f"{minutes}:{secs:02d}"



def play_wordle(word_dict, wordle_number, results_file):
    """
    Play a game of Bevordle.

    Parameters:
        word_dict (dict): A dictionary of words.
        wordle_number (int): The current game number.
        results_file (str): The file to save game results.
    """
    secret_word_index = random.randint(1, len(word_dict))  # Random key from dictionary
    secret_wordle = word_dict[secret_word_index]
    game_board = initialize_board()  # Initialize a blank game board
    emoji_board = []  # Track emoji feedback for each attempt
    keyboard = {letter: 'white' for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}  # Initialize keyboard

    previous_guesses=set() # will start fresh every game (i know people like their specific starting words... boring)

    print(f"\nWelcome to Bevordle #{wordle_number}!")
    time.sleep(1)  # Pause to let the user read the message
    start_time=time.time()
    display_board(game_board)
    display_keyboard(keyboard)

    for attempt in range(6):  # Maximum of 6 attempts
        guess_check = True  # Initial condition to ensure valid input
        while guess_check is True:
            guess = input("\nYour guess (5 letters): ").upper().strip()
            if len(guess) != 5:  # Condition for invalid input
                print("Invalid input! Your guess must be exactly 5 letters. Try again.")
                time.sleep(0.5)
                continue

            if not guess.isalpha():
                print("Invalid input! Guess must contain only letters (A-Z)... not whatever you put in.")
                continue

            if is_repeat_guess(guess, previous_guesses):
                print("You've already guessed that word this game! Try a new one... that must've been a mistake.")
                time.sleep(0.5)
                continue
            
            previous_guesses.add(guess)
            guess_check = False


                

        feedback, emoji_feedback = check_guess(secret_wordle, guess, keyboard)
        update_board(game_board, attempt, feedback)  # Update board with feedback
        emoji_board.append(emoji_feedback)  # Emoji feedback for results display

        display_board(game_board)
        display_keyboard(keyboard)
        time.sleep(0.5)  # Pause to let the player see the updated board

        if guess == secret_wordle:
            print("\nCongratulations! You guessed the word!")
            time.sleep(1)
            break  # Player wins
    else:
        print(f"\nSorry, you've used all your attempts. The word was: {secret_wordle}")
        time.sleep(1)

    end_time=time.time()
    elapsed_time = end_time-start_time
    record_results(results_file, wordle_number, attempt + 1, emoji_board, elapsed_time)

    print("\nBevordle Results:")
    print(f"Bevordle #{wordle_number} {attempt + 1}/6")
    print(f"Time taken: {format_time(elapsed_time)}\n")
    for emoji_row in emoji_board:
        print(''.join(emoji_row))
    time.sleep(2)



def main():
    wordlist = load_wordlist('wordle.txt')  # Load the word list from a file
    wordle_number = 1  # Start with #1
    results_file = 'bevordle_results.txt'  # File to store game results

    playing_game = True  # Initial condition for the main loop
    while playing_game:  # Continue while the player wants to play
        play_wordle(wordlist, wordle_number, results_file)  # Start a new game
        ask_play_again = True  # Initial condition to check replay status

        while ask_play_again:
            play_again_options = ['yes', 'y', 'n', 'no', 'view results', 'v']
            input_play_again = input("\nWould you like to play again? Yes, no, or view results (y/n/v): ").strip().lower()
            play_again = validate(play_again_options, input_play_again)

            if play_again in ['yes', 'y']:
                wordle_number += 1  # Increment Wordle number for the next game
                ask_play_again = False  # Stop asking and start a new game
            elif play_again in ['no', 'n']:
                print("\nThanks for playing Bevordle!")
                time.sleep(1)
                with open(results_file, 'w'):
                    pass
                playing_game = False  # Exit the main loop
                ask_play_again = False  # Stop asking
            else:
                view_results(results_file)  # Display past game results
                # After viewing results, reprompt for replay or exit decision

main()

#THIS IS THE RIGHT FILE!!!
