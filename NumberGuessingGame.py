import random
guess=random.randint(1,10)
number=int(input("Enter any number:"))
while number != guess:
    if number > guess:
       print("Too high!")
       number=int(input("Enter any number:"))
    elif number < guess:
       print("Too low!")
       number=int(input("Enter any number:"))
    else:
       break
print("You guess it right!!")

       


