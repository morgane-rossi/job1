def echange(tableau):
    tableau[0], tableau[-1] = tableau[-1], tableau[0]



liste = [1, 2, 3, 4, 5]
print(liste)
echange(liste)
print(liste)