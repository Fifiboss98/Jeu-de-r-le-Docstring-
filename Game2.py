import random
#ceci est ma deuxieme approche de solution au jeu de role propose par Docstring

message_de_bienvenue = """Bienvenue sur le jeu de role le plus cool de l'univers!\n
Le principe du jeu est simple: vous affrontez un ennemi et vous vous infligez a tour de role des dommages.\n
Vous demarrez tous les deux avec 50 points de vie chacun.\n
Vous pouvez soit attaquer (1) ou prendre une potion (2) a chaque tour.\n
L'adversaire vous inflige entre 5 et 15 points de vie et vous lui en infligez entre 5 et 10 points de vie.\n
Vous avez la possibilite de prendre jusqu'a 3 potions pour recuperer entre 15 et 50 points de vie avec chaque potion prise.
"""

print(message_de_bienvenue)

#les points de vie sont initialises a 50 pour chaque joueur
your_health, enemy_health = 50, 50
potion = 3


#fonction implementant votre attaque
def you_attack():
    global enemy_health, your_attack
    your_attack = random.randint(5,10)
    enemy_health -= your_attack


#fonction implementant l'attaque de l'adversaire
def enemy_attack():
    global your_health, their_attack
    their_attack = random.randint(5,15)
    your_health -= their_attack

#fonction implementant la prise de potion
def take_potion():
    global your_health, vie
    vie = random.randint(15,50)
    your_health += vie


while your_health and enemy_health > 0:

    print("-" * 100)
    action = input("Souhaitez vous attaquer(1), prendre une potion(2) ou quitter la partie(3): ")

    if action == "1":
        you_attack()
        enemy_attack()
        print(f"Vous avez infligé {your_attack} points a l'ennemi et lui vous en a infligé {their_attack} en retour. \nLe score est de : {your_health} à {enemy_health}")

    elif action == "2":
        if potion > 0:
            potion -= 1
            take_potion()
            enemy_attack()
            print(f"Vous avez récupéré {vie} points de vie et vous passez ce tour. \nVous avez subi une attaque de {their_attack} points. Le score est de : {your_health} à {enemy_health}")
        else:
            print(f"Oh lala! Vous avez utilise toutes vos 3 potions. \nScore: {your_health} à {enemy_health}")

    elif action == "3":
        print("Vous avez quitté le jeu!")
        break

#au cas ou l'utilisateur entre un choix invalide
    else:
        print("Choix invalide!")

    if your_health < 0:
        print(f"Vous avez perdu avec le score de: {your_health} à {enemy_health}")
        break
    
    elif enemy_health < 0:
        print(f"Vous avez gagné avec le score de: {your_health} à {enemy_health}")
        break

#fin de la partie