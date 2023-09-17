import requests
 
def generateWord(list_of_guesses, chosen_word):
    display = ""
    for c in chosen_word:
        if c in list_of_guesses:
            new_c = c
        else:
            new_c = "_"
        display = display + new_c
    print(display)


# generateWord(["a","c"], "abc")

chosen_word = requests.get(url="https://random-word-api.herokuapp.com/word").text[2:-2].lower()

print(chosen_word)
print("""
      #     #  #######  #     #  #######  #     #  #######  #     #
      #     #  #     #  ##    #  #        ##   ##  #     #  ##    # 
      #######  #######  # ### #  #  ####  # # # #  #######  # ### # 
      #     #  #     #  #    ##  #     #  #  #  #  #     #  #    ## 
      #     #  #     #  #     #  #######  #     #  #     #  #     #""")

num_guesses = 0

uniq_chars = list(set(chosen_word))
guessed_chars = []

while num_guesses < 5:
    guess = input("Guess a letter: ").lower()
    #if guess is right
    if guess in guessed_chars:
        print("Already guessed")
    if guess in uniq_chars:
        guessed_chars.append(guess)
        uniq_chars.remove(guess) #we remove the guessed char from the list
        if len(uniq_chars) == 0:
            print("You win!")
            break
        generateWord(guessed_chars, chosen_word)
        print("Correct")
    else:
        print("Wrong")
        num_guesses += 1

if num_guesses < 5:
    print("Out of guesses. You lose")
