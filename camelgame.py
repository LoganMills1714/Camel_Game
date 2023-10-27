import random
from os import name, system

def clear():  # Function to clear screen for new question
    if name == 'nt':
        _ = system('cls')  # Clear Screen for Windows computers
    else:
        _ = system('clear')  # Clear Screen for Unix systems

done = False  # Set start variables
miles = 0
thirst = 0
drinks = 6
eopie = 0  # Was originally star wars themed, never ended up changing it
feds = -20

clear()
print("\u001b[37mYour name is Edward Snowden, you're a US fugitive being")  # Backstory
print("hunted by the US Government for leaking classified NSA information")
print("Your goal is to flee 200 miles to Russia without being captured or dying")

while not done:  # Until game is done

    gap = miles - feds  # Calculate gap
    oasis = random.randint(1, 20)  # Random number for oasis

    print("\u001b[37m\n")
    print("Commands")  # Print commands
    print("\n")
    print("A. Get a cup of coffee")
    print("B. Walk")
    print("C. Run")
    print("D. Stop For The Night")
    print("E. Status Check")
    print("Q. Quit")
    print("\n")

    command = input("What is your command? ")  # Ask for command
    if command.lower() == "a":
        if drinks >= 1:  # Check if user has enough coffee
            thirst = 0  # If they do reset thirst to 0 and drinks down 1
            drinks -= 1
            print("\n")
            print("That was a refreshing cup of coffee!")
            if not done and oasis == 7:  # Check for oasis
                print("\n")  # If oasis print story message
                print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
                drinks = 6  # Reset variables because of oasis
                eopie = 0
                thirst = 0
        else:
            print("\n")
            print("You have no coffee left :(")  # If user doesn't have coffee left let them know
    elif command.lower() == "b":
        travel = random.randint(5, 12)  # Move 5 to 12
        miles += travel  # Add how far you moved
        print("\n")
        print("You traveled", travel, "miles!")  # Let user know
        thirst += 1  # Add thirst and tiredness
        eopie += 1
        closer = random.randint(7, 14)  # Feds move
        feds += closer  # Add how far feds moved
        if not done and oasis == 7:  # Check for oasis
            print("\n")
            print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
            drinks = 6
            eopie = 0
            thirst = 0

    elif command.lower() == "c":
        travel = random.randint(10, 20)  # Moves a bit further, rest of the code is about the same as previous block
        miles += travel
        print("\n")
        print("You traveled", travel, "miles!")
        thirst += 1
        tiredness = random.randint(1, 3)
        eopie += tiredness
        closer = random.randint(7, 14)
        feds += closer
        if not done and oasis == 7:
            print("\n")
            print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
            drinks = 6
            eopie = 0
            thirst = 0

    elif command.lower() == "d":
        eopie = 0  # Regain energy
        print("\n")
        print("You stopped for the night, you've regained your energy")
        closer = random.randint(7, 14)  # Move feds
        feds += closer
        if not done and oasis == 7:
            print("\n")
            print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
            drinks = 6
            eopie = 0
            thirst = 0

    elif command.lower() == "e":
        print("\n")
        print("Miles Traveled", miles)  # Print current stats
        print("Coffee's Left", drinks)
        print("The feds are", gap, "miles behind you")

    elif command.lower() == "q":  # Quit game
        done = True

    else:
        print("\n")
        print("Please enter a valid command")  # Catch other letters or numbers

    if miles >= 200:  # Check win condition
        print("\n")
        print("\u001b[32mCongrats, you've avoided the feds and made it to Mother Russia")  # Print win message        
        print("\n")
        again = input("\u001b[37mWould you like to play again? y/n ")  # Ask user if they want to play again
        if again == "y" or again == "yes":
            miles = 0  # If they choose to play again, reset all the stats
            thirst = 0
            drinks = 6
            eopie = 0
            feds = -20
        if again == "n" or again == "no":
            done = True  # Exit code if they don't want to play again

    
    if not done and thirst >= 4:
        print("\n")
        print("\u001b[31;1mWarning: You need some coffee")  # Thirst warning at 4 thirst
    if not done and thirst >= 6:
        print("\n")
        print("You died from a lack of coffee")  # Thirst death at 6 thirst
        done = True

    if not done and eopie >= 5:
        print("\n")
        print("\u001b[31;1mWarning: You're getting tired, consider stopping to rest")  # Energy warning at 5 tiredness
    if not done and eopie >= 8:
        print("\n")
        print("You died of exhaustion :(")  # Exhaustion death at 8 tiredness
        print("Guess you should've rested more")
        done = True

    if not done and miles - feds < 15:
        print("\n")
        print("\u001b[31;1mWarning: The feds are getting close")  # Fed warning if they're less than 15 miles away
    if not done and feds >= miles:
        print("\n")
        print("You've been captured, off to prison you go")  # Feds caught you, game over
        done = True
    
