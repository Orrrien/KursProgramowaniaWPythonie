temp = int(input("Podaj temperaturę w C\n"))
if(temp <= 0):
    print("Bardzo zimno")
elif(temp <= 15):
    print("Zimno")
elif(temp <= 25):
    print("Ciepło")
else:
    print("Gorąco")