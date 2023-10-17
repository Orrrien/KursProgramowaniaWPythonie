suma = 0
l = [6, 7, 3.14, "string1", "string2", 9, "string3", 1.0, 3, "string4", 5]
for i in range(len(l)):
    if(type(l[i]) == int):
        suma += l[i]
print(suma)

