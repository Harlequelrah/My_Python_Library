import string
from math import floor
from mychar import minus, majus


# 1: fonction qui prend un entraine une chaine de caractere/ liste et un caractere et renvoie une liste de toutes les occurences du caractere
def ind_ex(phrase_1, char):
    position = []
    for car in range(len(phrase_1)):
        if phrase_1[car] == char:
            position.append(car)
    return position


# 2:supprime toutes les occurences d un element dansune liste/chaine
def supp(liste, element):
    for i in range(len(liste)):
        if i in ind_ex(liste, element):
            del [liste[i]]


# 3:ajoute un element a une position specifique dans une liste
def ajout(liste, element, position):
    liste[position:position] = [element]


# 4:fonction qui renvoie True si la chaine/liste en parametre est un palindrome et False si ce n est pas un palindrome
def pal(nom):
    if nom.lower() == nom.lower()[::-1]:
        return True
    else:
        return False


# 4renvoie le nombre d occurence de chaque lettre dans la chaine
def nbr_let(txt, x=None):
    lettre = {}
    for i in txt:
        lettre[i] = lettre.get(i, 0) + 1
    if x == None:
        return sorted(lettre.items())
    else:
        return lettre[x]


# 5: pred en paramete une liste ou une chaine et renvoie la liste des majuscule et des minuscule avec un seul argument
# renvoie la liste des minuscule avec un second paramètre 0
##renvoie la liste des majuscule avec un second paramètre 1
# renvoie une liste avec le nombre de minuscule et majuscule


def casse(char_liste, casse=None):
    Up = []
    Lw = []
    m = 0
    M = 0

    for char in char_liste:
        if minus(char):
            m += 1
            if char not in Lw:
                Lw.append(char)

        if majus(char):
            M += 1
            if char not in Up:
                Up.append(char)

    if casse == None:
        return sorted(Lw), sorted(Up)
    elif casse == 0:
        return sorted(Lw)
    elif casse == 1:
        return sorted(Up)
    elif casse == -1:
        return [m, M]


# 6: renvoie True si y a 3 consonne de suite dans le mot et false sinon
# la fonction voy  de mychar doit etre importé
from mychar import voy

print(voy("e"))


def tc(mot):
    l = len(mot)
    k = 0
    while k < l:
        c = 0
        for i in mot[k : k + 3]:
            if not voy(i):
                c += 1
        if c == 3:
            return False
        k += 3
    return True
