# aby dodać aktywność należy wpisać "dodaj" gdy program prosi o wykonanie akcji
# aby pokazać czas należy wpisać "czas" gdy program prosi o wykonanie akcji
# aby pokazać top aktywności należy wpisać "top" gdy program prosi o wykonanie akcji
# aby zakończyć program należy wpisać "koniec" gdy program prosi o wykonanie akcji

dict = {}
while 1:
    a = input("Wykonaj akcję: \n")
    if a == 'koniec':
        break
    if a == 'dodaj':
        akt = input("Podaj nazwę aktywności: \n")
        czas = int(input("Podaj czas: \n"))
        if akt in dict:
            dict[akt].append(czas)
            print("Zaktualizowano czas aktywności")
        else:
            dict[akt] = [czas]
            print("Dodano aktywność")
    elif a == 'czas':
        akt = input("Podaj nazwę aktywności: \n")
        print("Całkowity czas: " + str(sum(dict[akt])))
    elif a == 'top':
        l = []
        for i in dict:
            l.append(sum(dict[i]))
        l.sort()
        for i in range(min(3, len(l))):
            for j in dict:
                if sum(dict[j]) == l[len(l)-i-1]:
                    print(str(1+i) + ". " + j)
                    break
