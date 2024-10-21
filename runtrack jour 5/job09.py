L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
#minimum = min(L)
#maximum = max(L)
minimum = L[0]
maximum = L[0]
for i in range(1, len(L)):
    if maximum < L[i] :
        maximum = L[i]
    elif minimum > L[i] :
        minimum = L[i]


print(f"la valeur max est : {maximum}")
print(f"la valeur min est : {minimum}")