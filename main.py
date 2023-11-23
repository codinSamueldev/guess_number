import random

def guess(x):
    numberToGuess = random.randint(1, x)
    userInput = 0
    

    while userInput != numberToGuess:
        userInput = int(input("\nType your lucky number: "))

        if userInput > numberToGuess:
            print("Nope, you are far away.")
        elif userInput < numberToGuess:
            print("Nope, but you are close.")

    print(f"\nCongrats! your lucky {userInput} number it is correct. ")

if __name__ == '__main__':
    guess(10)