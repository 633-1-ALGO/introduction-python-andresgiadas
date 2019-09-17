# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def ajouter(index):  # p a comme valeur par défaut 1
    tab_lettres[1][index] += 1

def chercher(lettre):
    i = len(tab_lettres[0])
    for index in range(0,i):
        if tab_lettres[0][index] == lettre :
            ajouter(index)

def decortiquer():
    for lettre in texte :
        if lettre != " ":
            chercher(lettre)

decortiquer()
print(*tab_lettres)