import requests

chosen_word = requests.get(url="https://random-word-api.herokuapp.com/word").text[2:-2]
print("""
      #     #  #######  #     #  #######  #     #  #######  #     #
      #     #  #     #  ##    #  #        ##   ##  #     #  ##    # 
      #######  #######  # ### #  #  ####  # # # #  #######  # ### # 
      #     #  #     #  #    ##  #     #  #  #  #  #     #  #    ## 
      #     #  #     #  #     #  #######  #     #  #     #  #     #""")

num_guesses = 0



while num_guesses < 5:
    guess = input("Guess a letter: ")
    #if guess is right
    if chosen_word.index(guess):
        print("")
    #else
    num_guesses += 1
