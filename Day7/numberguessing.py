import random

print(
    """  _____                          _    _             _   _                    _
 / ____|                        | |  | |           | \ | |                  | |                
| |  __  _   _   ___  ___  ___  | |_ | |__    ___  |  \| | _   _  _ __ ___  | |__    ___  _ __ 
| | |_ || | | | / _ \/ __|/ __| | __|| '_ \  / _ \ | . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|
| |__| || |_| ||  __/\__ \\\__ \ | |_ | | | ||  __/ | |\  || |_| || | | | | || |_) ||  __/| |   
 \_____| \__,_| \___||___/|___/  \__||_| |_| \___| |_| \_| \__,_||_| |_| |_||_.__/  \___||_|                                                                                       
"""
)
print(f"Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
guesses = 0
if difficulty == "easy":
    guesses = 10
else:
    guesses = 5
answer = random.randint(0, 100)
print(f"Hint hint, the answer is {answer}")
while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"You got it! The answer is {answer}")
        exit()
    elif guess < answer:
        print(f"Too low.\nGuess again.")
    else:
        print(f"Too high.\nGuess again.")
    guesses -= 1
print(f"Sorry! You lost! The answer was {answer}")
