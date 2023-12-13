import random      #Importing the random libraries/module which is built-in


def togetwelcomemessage():   #Define function to display a welcome message and the available flowers
    
    print("Welcome to the Flower Guessing Game! Hope You  Doing Great.")  #Display a welcome message and the available flowers.
    print("List of flowers:", flowers)


def togetuserchoice():     #Define function to get and validate the user's choice
   
    while True:            # To Get and validate the user's choice by using while loop

        
        userchoice = input("Select your choice: ").lower() #Get user input and convert to lowercase for case-insensitive comparison

        if userchoice in flowers:  # Check if the user's choice is in the list of available flowers

            return userchoice  # Return the valid choice


        else:
            print("Invalid choice. Please select from the available List of flowers.")

def togetcomputerchoice():   # Define function to get  the computer's choice.
   
    return random.choice(flowers)  # Return a randomly chosen flower from the list of flowers by using random.choice function.


def togetdisplayresult(userchoice, computerchoice):   # Define function to display the result of the game.

    print("Computer's answer is:", computerchoice)
    print("Your answer is:", userchoice)

    
    if computerchoice == userchoice:   # Check if the computer's choice matches the user's choice
        print("Congratulations! You guessed it correctly!")
    else:
        print("Sorry, you didn't guess correctly.")


def flowerguessinggame():  # Define the main function to run the Flower Guessing Game.
   
    togetwelcomemessage()  # Display the welcome message and list of  flowers.

    maxattempts = 3  # Setting  the maximum number of attempts

    for attempt in range(1, maxattempts + 1): #The range() is used to generate a sequence of numbers within a specified range where it is used in loops to iterate over a sequence of numbers. 

        userchoice = togetuserchoice()  # Get the user's choice
        computerchoice = togetcomputerchoice()  # Get the computer's choice

        togetdisplayresult(userchoice, computerchoice)  # Display the result of the current attempt

    
        if computerchoice == userchoice:       # Check if the user guessed correctly

            print(f"You won on attempt {attempt}!")  #It will show that if you are won in which attempt that you completed 
            break                                   # Exit the loop if the user guessed correctly
        elif attempt < maxattempts:                 # Check if the user's current attempt is less than maximum attempts
            print(f"You have {maxattempts - attempt} attempts remaining.")   # if current attempt is less than max attempts ,it will Shows how many attempts are left
    else:
        print(f"\nOut of attempts. The correct answer was {computerchoice}.")  # if current attempt is more than max attempt, it will show you  have no more attempts left and shows the computers choice

    print("\nThank you for playing! Come again!")   # displaying thanking messages


flowers = ["rose", "lily", "jasmine", "lotus"] # Define the list of available flowers


flowerguessinggame()  # Run the Flower Guessing Game

