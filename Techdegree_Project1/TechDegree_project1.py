import random

#random = random.randint(1, 10)
#random = random.randint(1, 10)

name = input( "Hey what is your name!  ")  

def start_game():
    
    choice_1 = input("Hello, {} welcome to the number guessing game!".format(name))
    guesses = 1
   
    random = random.randint(1, 10)
    
    #random = random.randint(1, 10)
    
    while True:
        
        try:
            choice_2 = input("Pick a number Between 1 and 10!  ")
            choice_2 = int(choice_2)
        
        except ValueError as wrong_value:
            print("oops! you can only use a number for a guess.")
            continue
       
               
        if choice_2 > random:
            print( " Uh oh, the number your looking for is lower")
            guesses += 1
            continue
            
        if choice_2 < random:
            print("uh oh, the number your looking for is higher")
            guesses += 1
            continue
            
        if choice_2 == random:
            print (" You guessed the right number congrats!")
            print(" It took you {} times to find the right number!".format(guesses))
            choice_3 = input(" Would you like to play again?\n Yes/No  ")
           
            if choice_3.lower() == "yes":
                return start_game ()
            else:
                break

                
start_game()
