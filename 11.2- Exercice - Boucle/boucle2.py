# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

print(B)

n = len(B)  # longueur du tableau
for i in range(1, n):  # "i" représentant l'indice courant et range une séquence de [0 à n-1]
    j = i
    while j > 0:
        if B[j-1] > B[j]:
            a = B[j-1]
            B[j-1] = B[j]
            B[j] = a
        j -= 1

print(B)