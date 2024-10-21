#def my_long_word(entier, chaine):
#    chaine = chaine.replace(",", "")
#    resultat = []
#    tableau = chaine.split(" ")
#    for mot in tableau:
#        if len(mot) > 3 :
#            resultat.append(mot)
#    return " ".join(resultat)


def my_long_word(n, s):
    return [word for word in s.split() if len(word) > n]

reuh = my_long_word(3, " La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance ")
print(reuh)