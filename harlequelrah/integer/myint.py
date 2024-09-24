# 1:renvoie le nombre en binaire sans le prefixe ob
def binary(x):

    x = bin(x)
    x = x[2:]  # pour effacer le prefixe ob
    x = int(x)
    return x


##2: base decimal d , base hexadecimal x et base binaire b
def base(n, f):

    if f == "b":
        return "{0:b}".format(n)
    elif f == "h":
        return "{0:x}".format(n)
    elif f == "d":
        return "{0:d}".format(n)
    else:
        return None


# 3:renvoie true si le nbr est premier et false sinon
from math import floor, sqrt


def prem(nbr):
    if nbr == 0 or nbr == 1:
        return False
    cpt = 0
    for i in range(2, nbr + 1):
        if nbr % i == 0:
            cpt += 1
    if cpt == 1:
        return True
    else:
        return False


# 4
# renvoie un nombre en produit de facteur premier avec un seul argument
# renvoie le nombre de fois que le second argument est present dans le nombre
# comme la fonction renvoie un dictonnaire on peut faire prd_fct(nbr)[]
def prd_fct(nbr, k=None):
    if k == 0:
        return None
    if k == 1:
        return 1
    liste_1 = [int(i) for i in range(1, int(nbr / 2)) if prem(i)]
    liste_2 = []
    for i in liste_1:
        cpt = 0
        nbr_i = nbr % i
        if nbr_i == 0:
            cpt = cpt + 1
        nbr_i = nbr / i
        while nbr_i % i == 0:
            cpt += 1
            nbr_i /= i
        liste_2.append(cpt)
    dic = {}
    for i in range(len(liste_2)):
        if liste_2[i] != 0:
            dic[liste_1[i]] = liste_2[i]
    if dic and k == None:
        return dic
    if dic and k != 1 and k != None:
        return dic[k]
    if not dic:
        dic[nbr] = 1
        return dic


# 4: uniquement a des fins d affichage : affiche le nombre suivi des produits de facteurs
def aff_prd_fct(nbr):
    a = str(nbr) + " = "
    if prem(nbr):
        return a + str(nbr) + " * 1"
    for j in prd_fct(nbr):
        a += str(j) + "^" + str(prd_fct(nbr, j)) + "*"
    return a[:-1]


# 5:renvoie le nombre de diviseur d un nombre
def nbr_div(nbr):
    if prem(nbr):
        return 1
    a = 1
    for i in prd_fct(nbr):
        a *= prd_fct(nbr)[i] + 1
    return a


# 6:retourne la liste des diviseurs d un nombre
def list_div(nbr):
    liste = []
    for i in prd_fct(nbr):
        liste.append(i)
    for i in prd_fct(nbr):
        liste.append(int(nbr / i))
    liste.append(nbr)
    liste.append(1)
    liste.sort()

    return liste


# 7: renvoie la sequence de fibonacci de 1 jusqu'au nombre entré en paramètre


def fibonacci(n):
    a, b, fib_sequence = 0, 1, []
    while a < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


# 8 renvoie le factoriel d un nombre
def fct(n):

    if n == 0:
        return 1
    else:
        return n * fct(n - 1)
