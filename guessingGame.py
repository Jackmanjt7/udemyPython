from random import randint

playing = input("Would you like to play a guessing game? Y/N ")

while playing!="N":
    number = randint(1,10)
    guess = 0
    while guess!=number:
        guess = int(input("Guess a number between 1 and 10! "))
        if(guess>number):
            print("your guess was too high!\n")
        elif(guess<number):
            print("your guess was too low!\n")
    print("You got it!")    
    playing = input("Play again? Y/N ")
