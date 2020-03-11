import time
import random

print("Welcome to Rock Paper Scissors. In a moment player 1 enter your choice")
time.sleep(1)

player1 = input("enter player 1's choice: ")

ai = random.randint(1,3)
print(f"ai's random number:{ai} \n")
if(ai == 1):
    ai = "rock"
elif(ai==2):
    ai = "paper"
elif(ai==3):
    ai = "scissors"
time.sleep(1)
print(f"Player 1's choice: {player1} vs AI's choice: {ai}")
if(player1 == ai):
    print("draw")
elif(player1 == "rock" and ai == "scissors"):
    print("player 1 wins")
elif(player1 == "scissors" and ai=="paper"):
    print("player 1 wins")
elif(player1 == "paper" and ai=="rock"):
    print("player 1 wins")
else:
    print("AI wins")
