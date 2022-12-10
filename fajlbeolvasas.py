def beolvas(fajlnev):
    fajlom=open(fajlnev, "r", encoding='utf-8')



    #fajl_tartalom = fajlom.readlines()
    #print(fajl_tartalom)
    fejlec= fajlom.readline().strip()
    print(fejlec)
    sorok = fajlom.readlines()
    #print(sorok)
    fajlom.close()
    fajlfeldolgozas(sorok)

nevek = []
nemek = []
korok = []

def fajlfeldolgozas(sorok):
    i = 0
    while (i < len(sorok)):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(', ')
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(int(sor[2]))
        i += 1
    print(nevek)
    print(nemek)
    print(korok)
