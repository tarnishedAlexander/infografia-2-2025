from character import Character

rogue = Character(100, 10, 0.1, 0.4)
tank = Character(500, 8, 0.3, 0.1)

n_turns = int(input("Ingrese numero de turnos: "))

for turn in range(n_turns):
    # ataca rogue
    rogue.attack(tank)
    # ataca tank
    tank.attack(rogue)