from random import randint

number = randint(1,10)
i = 0

while number!=5:
    i += 1
    number = randint(1,10)
    print(number)

print(f"It took {i} times to break the loop")
