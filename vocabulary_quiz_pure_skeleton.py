
# Vocabulary Quiz
# A simple quiz program using dictionaries and lists

# TODO: Create an empty dictionary to store words and their definitions
vocab={}

# TODO: Create two empty lists:
# - One to store correctly answered words
# - One to store incorrectly answered words
correct_words=[]
incorrect_words=[]

# TODO: Create the add_word function that:
# - Takes parameters: word (str) and definition (str)
# - Adds the word and definition to the vocabulary dictionary
# - Prints a message confirming the word was added
def add_word(word , definition):
    vocab[word] = definition
    print("Word added to dictionary!")
    return

# TODO: Create the take_quiz function that:
# - Takes optional parameter: num_questions (int, default 5)
# - Imports the random module to select random words
# - Clears both the correct_answers and incorrect_answers lists
# - Checks if there are any words in the vocabulary
# - If no words, prints a message and returns 0
# - Otherwise, limits the number of questions to the available words
# - Uses random.sample to select random words for the quiz
# - Initializes a score variable to keep track of correct answers
# - Loops through each word in the quiz_words list
# - For each word, asks the user for the definition
# - Checks if the answer is correct (matches the definition)
# - If correct, increments score and adds to correct_answers list
# - If incorrect, adds to incorrect_answers list
# - Prints the final score
# - Returns the score
def take_quiz(num_questions=5):
    import random
    correct_words.clear()
    incorrect_words.clear()
    if not vocab:
        print("The vocabulary list is empty :()")
        return 0
    num_questions = min(num_questions, len(vocab))
    quiz_words = random.sample(list(vocab.keys()), num_questions)
    score = 0
    for word in quiz_words:
        user_input = input(f"What is the definition of '{word}'?")
        if user_input==vocab[word]:
            score +=1
            print("Correct! :D")
            correct_words.append(word)
        else:
            incorrect_words.append(word)
            print("Incorrect :(")
    print(f"Your final score is {score} out of {num_questions}!")
    return score

# TODO: Create the show_results function that:
# - Takes no parameters
# - Prints a header for the quiz results
# - Checks if any quiz has been taken (both results lists are empty)
# - If no quiz taken, prints a message and returns
# - Otherwise, prints all correct answers with their definitions
# - Prints all incorrect answers with their definitions
# - Calculates and prints the final score as a fraction
def show_results():
    print("Quiz Results:")
    if not correct_words and not incorrect_words:
        print("You have not taken this quiz yet. :/")
        return
    print("Correct Answers :D :")
    for word in correct_words:
        print(f"{word}: {vocab[word]}")
    print("Incorrect Answers :( :")
    for word in incorrect_words:
        print(f"{word}: {vocab[word]}")
    final_score = len(correct_words)/(len(correct_words) + len(incorrect_words))
    print(f"Final Score: {len(correct_words)}/ {len(correct_words) + len(incorrect_words)} ({final_score: .2f})")
    
# TODO: Create the main program that:
# - Prints a welcome message
# - Creates a menu loop with these options:
#   1. Add new word
#   2. Take quiz
#   3. Show results
#   4. Exit
# - For option 1: Gets word and definition from user, calls add_word
# - For option 2: Gets number of questions from user, calls take_quiz
# - For option 3: Calls show_results
# - For option 4: Prints goodbye message and exits
# - For invalid options: Shows error message
print("Welcome to the Vocabulary Quiz! :D")
while True:
    print("\nMenu:")
    print("1. Add new word")
    print("2. Take quiz")
    print("3. Show results")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice =='1':
        word = input("Enter the word:")
        definition = input ("Enter the definition:")
        add_word(word, definition)
    elif choice =='2':
        num_questions = int(input("Enter the number of questions for the quiz:"))
        take_quiz(num_questions)
    elif choice =='3':
        show_results()
    elif choice =='4':
        print("Goodbye! :3")
        break
    else:
        print("Invalid option >:( Please choose a valid menu option.")
