# This code picks a random food item:
import pprint
from random import choice #DON'T CHANGE!
for x in range(1,10):
    food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

    #DON'T CHANGE THIS DICTIONARY EITHER!
    bakery_stock = {
        "almond croissant" : 12,
        "toffee cookie": 3,
        "morning bun": 1,
        "chocolate chunk cookie": 9,
        "tea cake": 25
    }

    # YOUR CODE GOES BELOW:
    if food in bakery_stock:
        print("{} {} left".format(bakery_stock[food], food))
    else:
        print("We don't make {}".format(food))

print()
#using fromkey to initialize a new dictionary to 0, kinda like setting a new
#character up 
#DO NOT TOUCH game_properties!
game_properties = ["current_score", "high_score", "number_of_lives", "items_in_inventory", "power_ups", "ammo", "enemies_on_screen", "enemy_kills", "enemy_kill_streaks", "minutes_played", "notifications", "achievements"] 

# Use the game_properties list and dict.fromkeys() to generate a dictionary with all values set to 0. Save the result to a variable called initial_game_state
initial_game_state = dict.fromkeys(game_properties, 0)
pprint.pprint(initial_game_state)


#dictionary comprehension
num_list = range(1,101)
num = {num:("even" if num%2==0 else "odd") for num in num_list}
pprint.pprint(num)