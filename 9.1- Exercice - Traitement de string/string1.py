# Consigne : Récupérer le mot "chaine" du string s et l'afficher
s = 'un exemple de chaine'

mot = ""
for lettre in s:

    if lettre == " ":
        mot = ""
    else:
        mot += lettre


    if mot == "chaine" :
        print(mot)



