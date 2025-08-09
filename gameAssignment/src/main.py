from character.Samurai import Samurai
from character.tank import Tank
from character.mage import Mage
from character.hero import Hero
import random

samurai = Samurai(health=100, base_attack=20, defense=5, probCrit=0.1)
tank = Tank(health=150, base_attack=15, defense=10, probCrit=0.05)
mage = Mage(health=80, base_attack=25, defense=3, probCrit=0.2)
hero = Hero(health=120, base_attack=18, defense=7, probCrit=0.15)

mode = input("Seleccione modo (auto/interactivo): ")

if mode == "auto":
    n_turns = int(input("Ingrese numero de turnos: "))
    characters = [samurai, tank, mage, hero]
    for turn in range(n_turns):
        print(f"\nTurno {turn + 1}:")
        # Shuffle characters
        random.shuffle(characters)
        # Each character attacks a random opponent
        for attacker in characters:
            targets = [c for c in characters if c != attacker and c.get_health() > 0]
            if targets:
                target = random.choice(targets)
                attacker.attack(target)
        print(f"Samurai: HP {samurai.get_health()}")
        print(f"Tank: HP {tank.get_health()}")
        print(f"Mage: HP {mage.get_health()}")
        print(f"Hero: HP {hero.get_health()}")
        if samurai.get_health() <= 0 or tank.get_health() <= 0 or mage.get_health() <= 0 or hero.get_health() <= 0:
            print("¡Combate terminado!")
            break

elif mode == "interactivo":
    while True:
        print("\nEstado actual:")
        print(f"Samurai: HP {samurai.get_health()}")
        print(f"Tank: HP {tank.get_health()}")
        print(f"Mage: HP {mage.get_health()}")
        print(f"Hero: HP {hero.get_health()}")
        
        action = input("Seleccione acción (ataque/ability/salir): ").lower()
        if action == "salir":
            break
        elif action == "ataque":
            attacker = input("Quién ataca? (samurai/tank/mage/hero): ").lower()
            target = input("A quién ataca? (samurai/tank/mage/hero): ").lower()
            targets = {"samurai": samurai, "tank": tank, "mage": mage, "hero": hero}
            if attacker in targets and target in targets and attacker != target and targets[target].get_health() > 0:
                targets[attacker].attack(targets[target])
            else:
                print("Opción inválida")
        elif action == "ability":
            character = input("Quién usa habilidad? (samurai/tank/mage/hero): ").lower()
            characters = {"samurai": samurai, "tank": tank, "mage": mage, "hero": hero}
            if character in characters:
                characters[character].ability()
            else:
                print("Opción inválida")
        if samurai.get_health() <= 0 or tank.get_health() <= 0 or mage.get_health() <= 0 or hero.get_health() <= 0:
            print("¡Combate terminado!")
            break

else:
    print("Modo no reconocido")