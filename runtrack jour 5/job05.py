def remplace(tableau):
    tableau[3] = tableau[2] + tableau[4]

L = [12, 42, 3, -5, 3]
print(L[1])
remplace(L)
print(L)
print(L[4])

"""
on peut : 
new_value = L [2] + L[4]
L.pop(3)
L.insert(3, new_value)
"""
