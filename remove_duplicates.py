n = [2,3,43,3,45,6,3,4,2]

unique =[]
for i in n:
    if i not in unique:
        unique.append(i)
print(unique)