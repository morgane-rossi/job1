my_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

print("List Before ", my_list)
temp_list = []

for i in my_list:
    if i not in temp_list:
        temp_list.append(i)

my_list = temp_list

print("List After removing duplicates ", my_list)