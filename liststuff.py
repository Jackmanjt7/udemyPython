# Create a list called instructors
instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.append("Colt")
instructors.append("Blue")
instructors.append("Lisa")

# Remove the last value in the list
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0,"Done")
print(instructors)
# Run the tests to make sure you've done this correctly!

#list comprehension is a powerful way to make it so you can do things inside
# of a list to redefine what is inside the list below are some examples

#This takes the first char of every word
answer = [char[0] for char in ["Elie", "Tim", "Matt"] ]
print(answer)

#This is an example of using an if statement inside of the comprehension stuff
answer2 = [x for x in [1,2,3,4,5,6] if x%2==0]
print(answer2)

#example of using this for intersection
answer3 = [x for x in [1,2,3,4] if x in [3,4,5,6]]
print(answer3)

#creative ways to use list comp and slices
answer4 = [char[::-1].lower() for char in ["ELIE","TIM","MATT"]]
print(answer4)

#using ranges inside list comp
answer5 = [x for x in range(1,101) if x%12==0]
print(answer5)

#nested lists
answer6 = [[x for x in range(0,10)] for y in range(1,10)]
print(answer6)