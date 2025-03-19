# Import necessary modules
# We'll need the 'random' module to select random responses
import random

# Define a list of generic responses
# These should be general enough to respond to many inputs
# Examples: "Interesting, tell me more.", "I see.", "Can you elaborate?"
responses = [
    "Interesting, tell me more.",
    "I see.",
    "Can you elaborate?",
    "That's fascinating.",
    "I'm not sure I understand.",
    "Could you clarify that?",
    "What do you mean by that?",
    "How does that make you feel?",
    "Why do you think that is?",
    "That's a good point."
]

# Function to get a random response
# This will randomly select one response from our list
# It should return the selected response
def get_random_responses():
    choice_response=random.choice(responses)
    return choice_response

# Function to process user input
# This function will take user input and return a response
# call the get_random_response function to get a response
# return the response to the user
# Note: In this minimal version, we won't process the input in any way
def process_user_input(user_input):
    random_response=get_random_responses()
    return random_response

# Main function to run the chatbot
if __name__ == "__main__":
# Should have a loop that:
#   - Gets input from the user
#   - Checks if the user wants to exit
#   - Processes the input (minimally in this version)
#   - Selects and displays a random response
    while True:
        user_input=input("Say something, or, to exit, type 'exit': ") 
        if user_input.lower()== "exit":
            print("Goodbye :3")
            break
        print(process_user_input(user_input)) 


# Exit condition
# Determine how the user can exit the chat (e.g., typing "quit" or "exit")

# Run the main function when the script is executed directly