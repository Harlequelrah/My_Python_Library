from math import floor


# 1 recopier le contenu d un ficher d une source a une destination


def recopie(ficher_source, ficher_destination, debit):
    with open(ficher_source, "r") as fs:
        fsr = fs.read()
        lfs = len(fsr)
        nbr_recopie = lfs / debit

    with open(ficher_source, "r") as fs:
        for i in range(floor(nbr_recopie) + 1):
            fsr = fs.read(debit)
            with open(ficher_destination, "a") as fd:
                fd.write(fsr)
                fd.close()


# 2 effacer le contenu d un ficher
def filereset(file):
    with open(file, "w") as ficher:
        ficher.close()


# 3:lire une ligne specifique d un ficher(le ficher doit comporter des lignes distinctes)(le premier indice est 1)
def rline(file, line):
    with open(file, "r") as ficher:
        for i in range(line):
            a = ficher.readline()
    print(a)


# 4 efface une ligne specifique d un ficher(le premier indice est 1)
def deline(file, line):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    if 1 <= line < len(a):
        del a[line - 1]
    with open(file, "w") as ficher:
        ficher.writelines(a)


# 5 permet d effacer toutes les lignes d un ficher commençant par un element en particulier
def delfile(file, element):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    for line in a:
        if line.startswith("#"):
            a.remove(line)
    with open(file, "w") as ficher:
        ficher.writelines(a)


# 6 permet de remplacer le contenue d une ligne  a une position precise
def repline(file, line, line_content):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    with open(file, "w") as ficher:
        ficher.writelines(a[0 : line - 1])
        ficher.write(line_content)
        ficher.writelines(a[line:])


# 7 permet d inserer une   ligne  a une position precise
def insline(file, line, line_content):
    with open(file, "r") as ficher:
        a = ficher.readlines()
    with open(file, "w") as ficher:
        ficher.writelines(a[0 : line - 1])
        ficher.write(line_content)
        ficher.writelines(a[line - 1 :])


# 8 verifier si un ficher existe
def existe(file):
    try:
        with open(file, "r") as ficher:
            return True
    except:
        return False
