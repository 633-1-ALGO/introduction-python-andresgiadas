# Problème : Etant donné une variable a et b, on demande de mettre la valeur de a dans b et celle de b dans a
# Contraintes : Ne pas utiliser de valeurs numériques.
# Données : les variables a et b

a = 11
b = 42

print("a = " + str(a))
print("b = " + str(b))


c = a
a = b
b = c


print("a = " + str(a))
print("b = " + str(b))
