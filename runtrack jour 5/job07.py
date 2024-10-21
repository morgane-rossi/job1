L = [8, 24,48,2,16]
#nbMultiplesTrois = 0
#for nombre in L :
#    if nombre % 3 == 0 :
#        nbMultiplesTrois += 1

count = len([x for x in L if x % 3 == 0])
print(count)
