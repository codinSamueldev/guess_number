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

def computer_guess(y):
    print("\nDear user, please think of a number and do not tell anyone. I am going to guess it.")
    low = 1
    high = y
    i = ""
    guessTimes = 0

    while i != 'r':
        computer_guess = random.randint(low, high)
        i = input(f"\nDear user, my lucky number is {computer_guess}, type: \nf). If I am far away\nc). If I am close\nr). If I guessed right.\n-> ").lower()
        if i == 'f':
            print("Ok I will try again.")
            guessTimes += 1
        elif i == 'c':
            print("Ok, that it is good to know. I will try again.")
            guessTimes += 1

    print(f"Dude, took me {guessTimes} tries. Anyways, it was fun!")



if __name__ == '__main__':
    #user_guess(10)
    computer_guess(8)