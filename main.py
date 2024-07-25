import random  # Import the random module to generate random choices for computer

while True:  # Start an infinite loop to keep playing the game until the user decides to stop

    # Prompt the user to enter their choice and convert the input to an integer
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

    # Generate a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
    computer_choice = random.randint(0, 2)

    # Display the computer's choice
    print(f"Computer choice is {computer_choice}")

    # Check if the user entered an invalid number (not 0, 1, or 2)
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
 
    # Check if the user chose Rock (0) and the computer chose Scissors (2)
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
   
    # Check if the computer's choice beats the user's choice
    elif computer_choice > user_choice:
        print("You lose")
 
    # Check if both choices are the same, resulting in a draw
    elif computer_choice == user_choice:
        print("It's a draw")

    # Check if the computer chose Rock (0) and the user chose Scissors (2)
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")

    # Check if the user's choice beats the computer's choice
    elif user_choice > computer_choice:
        print("You win")

    # Ask the user if they want to play again
    user_rematch = input("Play again? Yes or no\n")

    # Break the loop if the user does not want to play again
    if user_rematch.lower() != "yes":
        break