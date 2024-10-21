L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
compteur = 0
for nombre in L :
    if nombre % 2 == 0 :
        compteur += nombre

print(compteur)