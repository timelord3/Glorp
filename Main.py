# main loop
import random

class Human:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

class Enemy:
    def __init__(self, name, health, attack, type):
        self.name = name
        self.health = health
        self.attack = attack
        self.types = type
def battle():
 while mobs and player.health > 0:
    # Mobs attack first

    for mob in mobs:
        if mob.types == "FIR":
            print("Fire")
            # we can put the tag thing for status effects here
        elif mob.types == "ICE":
            print("Ice")
        print(f"Player: {player.health} {player.attack} vs {mob.name}: {mob.health} {mob.attack}")
        player.health -= mob.attack
        if player.health <= 0:
            print("You died")
            break
    if player.health <= 0:
        break

    # Player attacks
    select = input("Choose an enemy to attack: ")
    selected_mob = None
    for mob in mobs:
        if mob.name.lower() == select.lower():
            selected_mob = mob
            break

    if selected_mob:
        selected_mob.health -= player.attack
        if selected_mob.health <= 0:
            print(f"{selected_mob.name} died")
            mobs.remove(selected_mob)
    else:
        print("Invalid selection")

 if player.health > 0 and not mobs:
    print("All enemies defeated!")
 elif player.health <= 0:
    print("Game Over")

player = Human("Player", 100, 10)
mobs = [Enemy("Goblin", 100, 10,"FIR"), Enemy("Orc", 250, 20,"FIR"), Enemy("Troll", 300, 30,"ICE")]
battle()
