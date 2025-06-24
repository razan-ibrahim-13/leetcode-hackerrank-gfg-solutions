import random

r = random.randint(1, 100)
print("Welcome to the guessing game!")
while True:

    try:
        guess = int(input("Guess a number between 1 and 100 : "))

        if guess>r:
           print("high")
        elif guess<r:
           print("low")
        elif guess==r :
           print("you guessed it ")
           break
        
    except:
        print("enter a valid number")


    #this can be used when you are adding an exit message
    # elif str(guess) == exit: 
    #     print("thank u")
    #     break
   

    