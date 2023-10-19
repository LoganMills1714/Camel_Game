import random
from os import name, system

def clear():  # Function to clear screen for new question
    if name == 'nt':
        _ = system('cls')  # Clear Screen for Windows computers
    else:
        _ = system('clear')  # Clear Screen for Unix systems

done = False
miles = 0
thirst = 0
drinks = 6
eopie = 0
feds = -20

clear()
print("\u001b[37mYour name is Edward Snowden, you're a US fugitive being")
print("hunted by the US Government for leaking classified NSA information")
print("Your goal is to flee 200 miles to Russia without being captured or dying")

while not done:

    gap = miles - feds
    oasis = random.randint(1, 20)

    print("\u001b[37m\n")
    print("Commands")
    print("\n")
    print("A. Get a cup of coffee")
    print("B. Walk")
    print("C. Run")
    print("D. Stop For The Night")
    print("E. Status Check")
    print("Q. Quit")
    print("\n")

    command = input("What is your command? ")
    if command.lower() == "a":
        if drinks >= 1:
            thirst = 0
            drinks -= 1
            print("\n")
            print("That was a refreshing cup of coffee!")
            if not done and oasis == 7:
                print("\n")
                print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
                drinks = 6
                eopie = 0
                thirst = 0
        else:
            print("\n")
            print("You have no coffee left :(")
    elif command.lower() == "b":
        travel = random.randint(5, 12)
        miles += travel
        print("\n")
        print("You traveled", travel, "miles!")
        thirst += 1
        eopie += 1
        closer = random.randint(7, 14)
        feds += closer
        if not done and oasis == 7:
            print("\n")
            print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
            drinks = 6
            eopie = 0
            thirst = 0

    elif command.lower() == "c":
        travel = random.randint(10, 20)
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
        eopie = 0
        print("\n")
        print("You stopped for the night, you've regained your energy")
        closer = random.randint(7, 14)
        feds += closer
        if not done and oasis == 7:
            print("\n")
            print("\u001b[32mYou've found a fellow whistleblower, he gave you coffee and let you stay for the night")
            drinks = 6
            eopie = 0
            thirst = 0

    elif command.lower() == "e":
        print("\n")
        print("Miles Traveled", miles)
        print("Coffee's Left", drinks)
        print("The feds are", gap, "miles behind you")

    elif command.lower() == "q":
        done = True

    else:
        print("\n")
        print("Please enter a valid command")

    if miles >= 200:
        quote = random.randint(1, 70) 
        print("\n")
        print("\u001b[32mCongrats, you've avoided the feds and made it to Mother Russia")
        if quote == 1:
            print("\"There can be no faith in government if our highest offices are excused from scrutiny - they should be setting the example of transparency.\" -Edward Snowden")
        elif quote == 2:
            print("\"\" -Edward Snowden")
        elif quote == 3:
            print("\"\" -Edward Snowden")
        elif quote == 4:
            print("\"\" -Edward Snowden")
        elif quote == 5:
            print("\"\" -Edward Snowden")
        elif quote == 6:
            print("\"\" -Edward Snowden")
        elif quote == 7:
            print("\"\" -Edward Snowden")
        elif quote == 8:
            print("\"\" -Edward Snowden")
        elif quote == 9:
            print("\"\" -Edward Snowden")
        elif quote == 10:
            print("\"\" -Edward Snowden")
        elif quote == 11:
            print("\"\" -Edward Snowden")
        elif quote == 12:
            print("\"\" -Edward Snowden")
        elif quote == 13:
            print("\"\" -Edward Snowden")
        elif quote == 14:
            print("\"\" -Edward Snowden")
        elif quote == 15:
            print("\"\" -Edward Snowden")
        elif quote == 16:
            print("\"\" -Edward Snowden")
        elif quote == 17:
            print("\"\" -Edward Snowden")
        elif quote == 18:
            print("\"\" -Edward Snowden")
        elif quote == 19:
            print("\"\" -Edward Snowden")
        elif quote == 20:
            print("\"\" -Edward Snowden")
        elif quote == 21:
            print("\"\" -Edward Snowden")
        elif quote == 22:
            print("\"\" -Edward Snowden")
        elif quote == 23:
            print("\"\" -Edward Snowden")
        elif quote == 24:
            print("\"\" -Edward Snowden")
        elif quote == 25:
            print("\"\" -Edward Snowden")
        elif quote == 26:
            print("\"\" -Edward Snowden")
        elif quote == 27:
            print("\"\" -Edward Snowden")
        elif quote == 28:
            print("\"\" -Edward Snowden")
        elif quote == 29:
            print("\"\" -Edward Snowden")
        elif quote == 30:
            print("\"\" -Edward Snowden")
        elif quote == 31:
            print("\"\" -Edward Snowden")
        elif quote == 32:
            print("\"\" -Edward Snowden")
        elif quote == 33:
            print("\"\" -Edward Snowden")
        elif quote == 34:
            print("\"\" -Edward Snowden")
        elif quote == 35:
            print("\"\" -Edward Snowden")
        elif quote == 36:
            print("\"\" -Edward Snowden")
        elif quote == 37:
            print("\"\" -Edward Snowden")
        elif quote == 38:
            print("\"\" -Edward Snowden")
        elif quote == 39:
            print("\"\" -Edward Snowden")
        elif quote == 40:
            print("\"\" -Edward Snowden")
        elif quote == 41:
            print("\"\" -Edward Snowden")
        elif quote == 42:
            print("\"\" -Edward Snowden")
        elif quote == 43:
            print("\"\" -Edward Snowden")
        elif quote == 44:
            print("\"\" -Edward Snowden")
        elif quote == 45:
            print("\"\" -Edward Snowden")
        elif quote == 46:
            print("\"\" -Edward Snowden")
        elif quote == 47:
            print("\"\" -Edward Snowden")
        elif quote == 48:
            print("\"\" -Edward Snowden")
        elif quote == 49:
            print("\"\" -Edward Snowden")
        elif quote == 50:
            print("\"\" -Edward Snowden")
        elif quote == 51:
            print("\"\" -Edward Snowden")
        elif quote == 52:
            print("\"\" -Edward Snowden")
        elif quote == 53:
            print("\"\" -Edward Snowden")
        elif quote == 54:
            print("\"\" -Edward Snowden")
        elif quote == 55:
            print("\"\" -Edward Snowden")
        elif quote == 56:
            print("\"\" -Edward Snowden")
        elif quote == 57:
            print("\"\" -Edward Snowden")
        elif quote == 58:
            print("\"\" -Edward Snowden")
        elif quote == 59:
            print("\"\" -Edward Snowden")
        elif quote == 60:
            print("\"\" -Edward Snowden")
        elif quote == 61:
            print("\"\" -Edward Snowden")
        elif quote == 62:
            print("\"\" -Edward Snowden")
        elif quote == 63:
            print("\"\" -Edward Snowden")
        elif quote == 64:
            print("\"\" -Edward Snowden")
        elif quote == 65:
            print("\"\" -Edward Snowden")
        elif quote == 66:
            print("\"\" -Edward Snowden")
        elif quote == 67:
            print("\"\" -Edward Snowden")
        elif quote == 68:
            print("\"\" -Edward Snowden")
        elif quote == 69:
            print("\"\" -Edward Snowden")
        elif quote == 70:
            print("\"\" -Edward Snowden")
        
        print("\n")
        again = input("\u001b[37mWould you like to play again? y/n ")
        if again == "y" or again == "yes":
            miles = 0
            thirst = 0
            drinks = 6
            eopie = 0
            feds = -20
        if again == "n" or again == "no":
            done = True

    
    if not done and thirst >= 4:
        print("\n")
        print("\u001b[31;1mWarning: You need some coffee")
    if not done and thirst >= 6:
        print("\n")
        print("You died from a lack of coffee")
        done = True

    if not done and eopie >= 5:
        print("\n")
        print("\u001b[31;1mWarning: You're getting tired, consider stopping to rest")
    if not done and eopie > 8:
        print("\n")
        print("You died of exhaustion :(")
        print("Guess you should've rested more")
        done = True

    if not done and miles - feds < 15:
        print("\n")
        print("\u001b[31;1mWarning: The feds are getting close")
    if not done and feds >= miles:
        print("\n")
        print("You've been captured, off to prison you go")
        done = True
    
