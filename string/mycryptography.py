import string

#1: code un mot avec l argument operation =1 / decode avec l operation =-1 , avec une clé de chiffrement k
def cesar(mot,operation=1,k=3):
    word=""
    liste_1=string.ascii_lowercase
    liste_2=string.ascii_uppercase

    for i in mot:
        if i in liste_1:
            word+=liste_1[(liste_1.index(i) + k*operation)%26]
        elif i in liste_2:
             word+=liste_2[(liste_2.index(i) + k*operation)%26]
        else:
            word+=i
    return word


#2:  prend en parametre un mot codé et renvoie un dictionnaire composé des mots claires possible
def verif_cesar(mot):
 dic={}
 for i in range(26):
     dic[cesar(mot,-1,i)]=i
 return dic

#3:prend en paramètre  une chaine de caractère codé et renvoie un dictionnaire composé des possibles mot claires
def z_cesar(chaine):

    if chaine.isspace()==False:
            dico={}
            for a in range(26):
                l=[]
                for i in chaine.split(" "):
                    for j,k in verif_cesar(i).items():
                        if a==k:
                          l.append(j)
                if l:
                   dico[a]=" ".join(l)
            return dico
    else:return verif_cesar(chaine)

