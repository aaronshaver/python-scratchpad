# yes, I'm aware there's probably a mathematical way to do this instead of Monte Carlo-style

from random import randrange

offset = 1
die = 20 + offset
num_rolls = 1000000

standard_rolls = []
for i in range(num_rolls):
	standard_rolls.append(randrange(die))

print("Average of " + "standard rolls:")
print(str(sum(standard_rolls)/len(standard_rolls)))

advantage_rolls = []
for i in range(num_rolls):
	roll1 = randrange(die)
	roll2 = randrange(die)
	result = roll1 if roll1 > roll2 else roll2
	advantage_rolls.append(result)

print("Average of " + "advantage rolls:")
print(str(sum(advantage_rolls)/len(advantage_rolls)))

disadvantage_rolls = []
for i in range(num_rolls):
	roll1 = randrange(die)
	roll2 = randrange(die)
	result = roll1 if roll1 < roll2 else roll2
	disadvantage_rolls.append(result)

print("Average of " + "disadvantage rolls:")
print(str(sum(disadvantage_rolls)/len(disadvantage_rolls)))
