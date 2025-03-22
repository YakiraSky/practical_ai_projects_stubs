# Hangman Game
# A simple word guessing game using strings, lists, and functions

# TODO: Import the random module to select random words
import random


word_list = [
    "python",
    "hangman",
    "computer",
    "programming",
    "keyboard",
    "elephant",
    "calendar",
    "sunshine",
    "mountain",
    "basketball",
    "orchestra",
    "universe",
    "chemistry",
    "adventure"
]


# TODO: Create a function to select a random word that:
# - Takes no parameters
# - Uses random.choice to select a random word from your word list
# - Returns the selected word in lowercase
def select_random():
    selected_word=random.choice(word_list)
    return selected_word.lower()


# TODO: Create a function to initialize the game state that:
# - Takes parameter: word (str)
# - Creates and returns a dictionary with these keys:
#   - "word": the word to guess
#   - "guessed_letters": an empty list to track guessed letters
#   - "word_completion": a string of underscores representing unguessed letters (e.g., "_ _ _ _")
#   - "tries_remaining": number of incorrect guesses allowed (start with 6)
def initialize_game_state(word):
    guessed_letters = []
    word_completion = "_ " * len(word)
    word_completion = word_completion.strip()
    tries_remaining = 6
    return {
        "word": word,
        "guessed_letters": guessed_letters,
        "word_completion": word_completion,
        "tries_remaining": tries_remaining
    }

    # TODO: Create a function to display the game state that:
# - Takes parameter: game_state (dict)
# - Prints the current hangman state based on tries_remaining
#   (You can use ASCII art for different hangman states)
# - Prints the current word completion (with spaces between letters)
# - Prints the letters that have been guessed so far
# - Prints the number of tries remaining
# ASCII art for hangman states
# ASCII art for hangman stages (reversed order)
HANGMAN_STAGES = [
    
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    ========='''
]

def display_game_state(game_state):
    print(HANGMAN_STAGES[game_state['tries_remaining']])
    print("Current word: " + " ".join(game_state['word_completion']))
    print("Guessed letters: " + ", ".join(game_state['guessed_letters']))
    print("Tries remaining: " + str(game_state['tries_remaining']))


# TODO: Create a function to get a valid letter guess that:
# - Takes parameter: game_state (dict)
# - Asks the user to guess a letter
# - Validates that the input is:
#   - A single character
#   - A letter (not a number or symbol)
#   - Not already guessed
# - Returns the valid guessed letter in lowercase
# - Keeps asking until a valid letter is entered
def get_valid_letter_guess(game_state):
    while True:
        guess = input("Please guess a letter: ").lower()
        if len(guess) !=1:
            print("Please enter only a single letter :) ")
        elif not guess.isalpha():
            print("Please enter a letter, not a number or symbol :/ ")
        elif guess in game_state['guessed_letters']:
            print("You have already guessed that letter. Try again :O ")
        else:
            return guess
    

# TODO: Create a function to update the game state that:
# - Takes parameters: game_state (dict) and guessed_letter (str)
# - Adds the guessed letter to the guessed_letters list
# - Checks if the guessed letter is in the word
# - If it is, updates the word_completion to reveal the letter
# - If it's not, decreases the tries_remaining
# - Returns True if the guess was correct, False otherwise
def update_game_state(game_state, guessed_letter):
    game_state['guessed_letters'].append(guessed_letter) 
    if guessed_letter in game_state['word']:
        new_completion = list(game_state['word_completion'])
        for idx, char in enumerate(game_state['word']):
            if char == guessed_letter:
                new_completion[idx * 2] = guessed_letter
        game_state['word_completion'] = ''.join(new_completion)
        return True
    else:
        game_state['tries_remaining'] -= 1
        return False

# TODO: Create a function to check if the game is over that:
# - Takes parameter: game_state (dict)
# - Returns True if the word is completely guessed or no tries remain
# - Returns False otherwise
def is_game_over(game_state):
    if "_" not in game_state['word_completion'] or game_state['tries_remaining'] <= 0:
        return True
    return False

# TODO: Create a function to check if the player won that:
# - Takes parameter: game_state (dict)
# - Returns True if the word_completion matches the word (no more underscores)
# - Returns False otherwise
def check_win(game_state):
    if game_state['word_completion'].replace(' ', '') == game_state['word']:
        return True
    return False

# TODO: Create the main game function that:
# - Takes no parameters
# - Selects a random word
# - Initializes the game state
# - Displays welcome message and initial game state
# - Loops until the game is over:
#   - Gets a valid letter guess
#   - Updates the game state with the guess
#   - Displays the updated game state
# - When game ends, displays win or lose message
# - Reveals the word if the player lost
# - Asks if the player wants to play again
def play_game():
    word = select_random()
    game_state = initialize_game_state(word)
    print("Welcome to Hangman!")
    display_game_state(game_state)
    while not is_game_over(game_state):
        guessed_letter = get_valid_letter_guess(game_state)
        update_game_state(game_state, guessed_letter)
        display_game_state(game_state)
    if check_win(game_state):
        print("Congratulations! You've won! :D")
    else:
        print(f"Sorry, you've lost. :( The word was '{game_state['word']}'.")

# TODO: Create the main program that:
# - Prints a welcome message
# - Calls the main game function
# - Handles play again logic
# Print a welcome message
# Call the main game function to start the game
if __name__ == "__main__": 
  while True:
    play_game()
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            break
        elif play_again == 'n':
            print("Goodbye! Thanks for playing Hangman!")
            exit()
        else:
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")