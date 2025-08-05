import random

class Dice:
    def __init__(self, n_sides: int, cheat_side: int, cheat_prob: float = 0.3):
        self.n_sides = n_sides
        self.cheat_side = cheat_side
        self.cheat_prob = cheat_prob
    
    def throw(self):
        return self.cheat_side if random.random() <= self.cheat_prob else random.randint(1, self.n_sides)
    
dice = Dice(7, 3)

counts = {}
for i in range(1000):
    value = dice.throw()
    if not counts.get(value):
        counts[value] = 1
    else:
        counts[value] += 1

print(counts)
