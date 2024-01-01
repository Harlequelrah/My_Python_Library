# 1: fonction qui verifie si un caractere est une voyelle
def voy(x):

 voyelle=['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y', 'Á', 'É', 'Í', 'Ó', 'Ú', 'Ý', 'À', 'È', 'Ì', 'Ò', 'Ù', 'Â', 'Ê', 'Î', 'Ô', 'Û', 'Ä', 'Ë', 'Ï', 'Ö', 'Ü', 'Ÿ', 'Æ', 'Œ', 'á', 'é', 'í', 'ó', 'ú', 'ý', 'à', 'è', 'ì', 'ò', 'ù', 'â', 'ê', 'î', 'ô', 'û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ', 'æ', 'œ']
 if x in voyelle:
     return True
 else:
      return False


# 2: fonction qui renvoie le nombre de voyelle dans une chaine
def nbr_voy(y):
 w=0
 for v in y :
        if voy(v) :
            w=w+1
 return w



#3:fonction qui prend en parametre 3 caracteres et verifie si le  char est compris entre char_1 et char_2
def inter_char(char,char_1,char_2):
    if ord(char) >= ord(char_1) and ord(char) <= ord(char_2):
        return True
    elif ord(char) >= ord(char_1) and ord(char) <= ord(char_2):
        return False
    else :
        return None

#4:fonction qui renvoie True si le caractere est en minuscule , false si il est en majuscule en None si aucun des deux cas
import string
def minusmaj(char):
    if char in string.ascii_lowercase:return True
    elif  char in string.ascii_uppercase:return False
    else :return None

