import time

print("Welcome to Rock Paper Scissors. In a moment player 1 enter your choice")
time.sleep(1)

player1 = input("enter player 1's choice: ")

print("... NO CHEATING ...\n\n\n")
print("... NO CHEATING ...\n\n\n")
print("... NO CHEATING ...\n\n\n")
print("... NO CHEATING ...\n\n\n")
print("... NO CHEATING ...\n\n\n")

player2 = input("enter player 2's choice: ")

print("...  ...\n\n\n")
print("...  ...\n\n\n")
print("...  ...\n\n\n")
print("...  ...\n\n\n")
print("...  ...\n\n\n")

print("...ROCK...")
time.sleep(1)
print("...PAPER...")
time.sleep(1)
print("...SCISSORS...")
time.sleep(1)
print(f"Player 1's choice: {player1}")
print(f"Player 2's choice: {player2}")
player1 = player1.lower()
player2 = player2.lower()
if(player1 == player2):
    print("draw")
elif(player1 == "rock" and player2 == "scissors"):
    print("player 1 wins")
elif(player1 == "scissors" and player2=="paper"):
    print("player 1 wins")
elif(player1 == "paper" and player2=="rock"):
    print("player 1 wins")
else:
    print("player 2 wins")



