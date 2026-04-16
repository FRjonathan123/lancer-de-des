import random
import matplotlib.pyplot as plt

# on commence à 2 car on ne peut pas avoir un 1 avec 2 des
resultat_des = 2
nb_simul = 15000
list_resultat_des = []
list_resultat = []

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
    list_resultat.append(round(resultat, 2))
    print(resultat_des,":", round(resultat,2), "%")
    resultat_des += 1
    list_resultat_des.append(n+2)

plt.ylim(0,20)
plt.xlim()
plt.plot(list_resultat_des, list_resultat, marker='o', label="pourcentage")
plt.xticks(list_resultat_des)
plt.xlabel('Résultat Dés')
plt.ylabel('Pourcentage apparition')
plt.title('Graphique de la simulation')
plt.legend()
plt.grid()

for i in range(len(list_resultat)):
    plt.text(list_resultat_des[i], list_resultat[i], str(list_resultat[i]), ha='left', va='top', bbox=dict(facecolor='white', alpha=0.5))

plt.show()
