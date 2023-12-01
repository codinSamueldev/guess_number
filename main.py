import random

def user_guess(x):
    numberToGuess = random.randint(1, x)
    userInput = 0

    while userInput != numberToGuess:
        userInput = int(input("\nType your lucky number: "))

        if userInput > numberToGuess:
            print("Nope, you are far away.")
        elif userInput < numberToGuess:
            print("Nope, but you are close.")

    print(f"\nCongrats! your lucky {userInput} number it is correct. ")

##################################################

def computer_guess(y):
    low = 1
    high = y
    i = ""
    guessTimes = 0

    while i != 'r':
        if low != high:
            currentComputerGuess = random.randint(low, high)
        else:
            currentComputerGuess = low

        i = input(f"\nDear user, my lucky number is {currentComputerGuess}, type: \nh). If it is higher\nl). If it is less\nr). If I guessed right.\n-> ").lower()
        if i == 'h':
            print("Ok I will try again.")
            low = currentComputerGuess + 1
            guessTimes += 1
        elif i == 'l':
            print("Ok, that is good to know. I will try again.")
            high = currentComputerGuess - 1
            guessTimes += 1

    print(f"Dude, took me {guessTimes} tries. Anyways, it was fun!")



if __name__ == '__main__':
    """ user_guess(10) """
    #####################################

    print("\nDear user, please think of a number from 1 to 1000 and do not tell anyone. I am going to guess it.")
    ready = ""
    while ready != "yes":
        ready = input("Type and enter YES if you are ready -> ").lower()

    computer_guess(1000)