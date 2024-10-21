tableau = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

#longueur = len(tableau)
#for i in range (0, longueur) :
#    minimum = tableau[i]
#    indiceMin = i
#    for j in range (i, longueur) :
#        if tableau[j] < minimum :
#            minimum = tableau[j]
#            indiceMin = j

#    temp = tableau[indiceMin]
#    tableau[indiceMin] = tableau[i]
#    tableau[i] = temp
tableau = sorted(tableau)

print(tableau)