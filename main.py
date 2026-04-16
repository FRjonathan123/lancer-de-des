import random

# on commence à 2 car on ne peut pas avoir un 1 avec 2 des
resultat_des = 2
nb_simul = 15000

def simulation():
    compteur = 0
    
    for i in range(nb_simul):
        lancer1 = random.randint(1,6)
        lancer2 = random.randint(1,6)

        total = lancer1 + lancer2

        if total == resultat_des:
            compteur += 1

        pourcentage = (compteur / nb_simul) * 100
    return pourcentage


print(f"on lance 2 des {nb_simul} fois. \nvoici les pourcentages d'apparition que la simulation a calculer \npour chaque resultat de des possible : de 2 jusqu'a 12\n")
print("resultat du des  :   pourcentage d'apparition")
for n in range(11):
    resultat = simulation()
    print(resultat_des,":", round(resultat,2), "%")
    resultat_des += 1
