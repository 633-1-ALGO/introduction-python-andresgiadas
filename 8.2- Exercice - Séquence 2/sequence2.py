# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75
tva = 7.7/100

total_ht = nb_articles * prix_ht
total_tva = total_ht * tva

print("Le prix TTC est de " + str(total_ht + total_tva) + " chf.")
