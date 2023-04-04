import random

#ceci est ma premiere approche de solution au jeu de role propose par Docstring.

message_de_bienvenue = """Bienvenue sur le jeu de role le plus cool de l'univers!\n
Le principe du jeu est simple: vous affrontez un ennemi et vous vous infligez a tour de role des dommages.\n
Vous demarrez tous les deux avec 50 points de vie chacun.\n
Vous pouvez soit attaquer (1) ou prendre une potion (2) a chaque tour.\n
L'adversaire vous inflige entre 5 et 15 points de vie et vous lui en infligez entre 5 et 10 points de vie.\n
Vous avez la possibilite de prendre jusqu'a 3 potions pour recuperer entre 15 et 50 points de vie avec chaque potion prise.
"""

print(message_de_bienvenue)


your_name = input("Veuillez entrer votre nom: ")
ennemy_name = input("Entrez le nom de votre adversaire: ")

#Vous demarrez tous deux avec 50 points de vie chacun
your_health, ennemy_health = 50, 50 
potion = 3

#implementation de la logique du jeu
while your_health and ennemy_health > 0:
    print("-" * 100)
    action = int(input(
    f"Tres bien {your_name}, souhaitez vous attaquer(1), prendre une potion(2) ou quitter la partie(3): "))

    if action == 1:
        your_attack = random.randint(5, 10)
        ennemy_attack = random.randint(5, 15)
        ennemy_health -= your_attack
        your_health -= ennemy_attack
        
        print(f"Vous avez infligé une attaque de {your_attack} point(s) a {ennemy_name} et {ennemy_name} vous a infligé une attaque de {ennemy_attack} point(s) en retour.")
        print(f"Score: {your_health} a {ennemy_health}")
        
    elif action == 2:
        if potion > 0:
            potion -= 1
            #si vous prenez une potion vous recuperez entre 15 et 50 points de vie
            points_de_vie = random.randint(15, 50)                    
            ennemy_attack = random.randint(5, 15)
            your_health += points_de_vie
            your_health -= ennemy_attack
            
            print(f"Vous avez récupéré {points_de_vie} points de vies et vous passez le prochain tour. \n{ennemy_name} vous a infligé une attaque de {ennemy_attack} point(s).")   
            # Le score montre renseigne sur les points de vie restant a chacun           
            print(f"Score: {your_health} à {ennemy_health}")
            
            ennemy_attack = random.randint(5, 15)
            your_health -= ennemy_attack

            print(f"Vous avez subi à nouveau une attaque de {ennemy_attack} points.")
            print(f"Score: {your_health} à {ennemy_health}")

        else:
            print("Désolé, vous avez epuise vos 3 potions.")
            print(f"Score: {your_health} à {ennemy_health}")

    elif action == 3:
        print(f"Score: {your_health} à {ennemy_health}")
        print(f"Au revoir {your_name} !.")
        break


    if ennemy_health < 0:
        print(f"Félicitations, vous avez battu {ennemy_name} avec un score de: {your_health} a {ennemy_health}!")
        break

    elif your_health < 0:
        print(f"Dommage, {ennemy_name} vous a battu avec un score de: {your_health} a {ennemy_health}.")
        break

#fin de la partie