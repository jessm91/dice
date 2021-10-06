from random import randint

"""Create die and roll function"""
class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = randint(1, self.sides)
        return result

die1 = Die()
die2 = Die()
numbs = []

"""Roll two dice"""
outcome1 = die1.roll_die()
numbs.append(outcome1)
outcome2 = die2.roll_die()
numbs.append(outcome2)

print("Numbers rolled: ")
print(numbs)
