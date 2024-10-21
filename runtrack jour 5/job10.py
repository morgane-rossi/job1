L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
compteur = 1
for nombre in L :
    if nombre >= 25 and nombre <= 90 :
        compteur *= nombre

print(compteur)