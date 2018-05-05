import random

MAX_ROLLS = 100000
MAX_SIDES = 20

def roll_die(sides):
    return random.randint(1, sides)  

# exclude 1 sided die sum, because it's always equal to number of rolls
# + 1 because last number is excluded in Python ranges
dice = [i for i in range(2, MAX_SIDES + 1)] 
 
for die in dice:
    print("Sum of {} rolls for die with {} sides: ".format(MAX_ROLLS, die))
    sum = 0
    for i in range(MAX_ROLLS):
        sum += roll_die(die)
    print(sum)

