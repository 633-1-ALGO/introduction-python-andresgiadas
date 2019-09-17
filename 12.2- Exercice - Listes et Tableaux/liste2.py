# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

plusGrand = tab[0][0]
nPlusGrand = 0
mPlusGrand = 0

i = len(tab)

for n in range(0,i):
    j = len(tab[n])
    for m in range(0,j):
        test = tab[n][m]
        if test > plusGrand:
            plusGrand = test
            nPlusGrand = n
            mPlusGrand = m

print("La valeur maximum est :  ", plusGrand," et elle se trouve à l'indice [ ", nPlusGrand," ][ ",mPlusGrand," ]")
