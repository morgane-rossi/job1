def arrondit_trie(liste) :
    for i in range(len(liste)) :
        entier = int(liste[i])
        if liste[i] - entier >= 0.5 :
            entier += 1
        liste[i] =entier    

    for i in range (0, len(liste)) :
        minimum = liste[i]
        indiceMin = i
        for j in range (i, len(liste)) :
            if liste[j] < minimum :
                minimum = liste[j]
                indiceMin = j

        temp = liste[indiceMin]
        liste[indiceMin] = liste[i]
        liste[i] = temp

    return liste


liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

for i in range(len(liste)):
    liste[i] = int(liste[i] + 0.5)
for i in range(len(liste)):
    for j in range(i+1, len(liste)):
        if liste[i] > liste[j]:
            liste[i], liste[j] = liste[j], liste[i]


print(liste)
#print(arrondit_trie(liste))

# [4, 5, 9, 11, 12, 14, 16, 18, 22]