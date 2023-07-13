print("i'm thinking of a number between 1-100. you have 7 guesses.")

import random
a=random.randint(1,100)
tries=1
while True:
    guess=int(input(f"guess # {tries}:\n"))
    tries=tries+1
    if tries>7:
        print("sorry, you didn't guess it in 7 tries. you lose" )     
        break  
    elif guess==a:
        print("you guessed it! what are the odds?!?")
        break
    elif guess >a:
        print("sorry, you are too high.")
    elif guess <a:
        print("sorry, you are too low.")