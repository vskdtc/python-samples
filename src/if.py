x = int(input("Gebe eine Zahl ein: "))
if x == 2:
    print(x,'Ist eine Primezahl')
elif x == 3:
     print(x,'Ist eine Primezahl')
elif x == 5:
        print(x,'Ist eine Primezahl')
elif x == 7:
        print(x,'Ist eine Primezahl')
elif x%2 == 0:
         print(x,'Ist keine Primezahl, weil', x/2, 'A')
elif x%3 == 0:
         print(x,'Ist keine Primezahl, weil', x/3, 'B')
elif x%5 == 0:
         print(x,'Ist keine Primezahl, weil', x/5,'C')
elif x%7 == 0:
        print(x,'Ist keine Primezahl, weil', x/7, 'D')
elif x < 1000:
        print(x,'Ist eine Primezahl')
