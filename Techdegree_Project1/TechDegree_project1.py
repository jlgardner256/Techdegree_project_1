import random

#random = random.randint(1, 10)
#random = random.randint(1, 10)

name = input( "Hey what is your name!  ")  

def start_game():
    
    choice_1 = input("Hello, {} welcome to the number guessing game!".format(name))
    guesses = 1
   
    randoms = random.randint(1, 10)
    
    #random = random.randint(1, 10)
    play = True
    while play:
        
        try:
            choice_2 = int(input("Pick a number Between 1 and 10!  "))
                    
        except ValueError as wrong_value:
            print("oops! you can only use a number for a guess.")
            continue
       
               
        if choice_2 > randoms:
            print( " Uh oh, the number your looking for is lower")
            guesses += 1
            continue
            
        elif choice_2 < randoms:
            print("uh oh, the number your looking for is higher")
            guesses += 1
            continue
       
        else:
            print(" You guessed the right number congrats!")
            print(" It took you {} times to find the right number!".format(guesses))
            choice_3 = input(" Would you like to play again?\n Yes/No  ")

            if choice_3.lower() == "yes":
                return start_game()
            else:
                play = False
        

                
start_game()
