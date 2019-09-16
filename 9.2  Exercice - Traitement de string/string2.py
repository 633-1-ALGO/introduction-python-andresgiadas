# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

cpt = 0
mot = ""
liste = []
for lettre in texte:

    if lettre == " " or lettre == "'" or lettre == ".":
        liste.append(mot)
        mot += lettre
        mot = ""
    else:
        mot += lettre


    if mot == "exemple" :
        cpt += 1

print("nb exemple : ", cpt)
liste[1] = "représente"
print(liste)
